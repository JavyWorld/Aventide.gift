### Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)

**Fuente de verdad:** “Genie y Memory”. En esta entrega se usa **solo** la sección Memory y sus reglas/entidades asociadas.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Memory es el sistema que crea un **perfil de regalos** (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en **preferencias estructuradas** reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory **no recomienda** por sí solo; Memory **provee contexto**.

**Objetivos (duros):**

1. Reuso: reducir fricción en compras repetidas (cumples, aniversarios, Navidad).

2. Consistencia: una única fuente de verdad para preferencias del destinatario.

3. Privacidad: controlar “qué ve el seller” vs “qué guarda el buyer” y soportar “Admirador Secreto” como política transversal.

4. Seguridad/compliance: PII y datos sensibles con clases de datos y retención; acceso mínimo y auditado.

5. Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.

---

## 2) Alcance (incluye / excluye)

### Incluye

- **Recipient Directory**: destinatarios (personas) creados por un buyer con metadatos y relación.

- **Gift Memory Profile** por destinatario:

    - preferencias (categorías, estilos, colores),

    - restricciones (alergias, dislikes),

    - detalles prácticos (tallas, rango de presupuesto),

    - fechas (cumpleaños, aniversario),

    - historial de regalos (gift_history).

- **Occasions & Reminders**: recordatorios asociados a recipient + fecha + zona/país (timezone).

- **Signal ingestion**: captura de señales desde:

    - acciones del buyer (guardar, ver, comprar, devolver),

    - inputs explícitos (formularios),

    - notas manuales.

- **Privacy controls**:

    - campos marcados como privados,

    - niveles de compartición (solo buyer / compartible con seller / compartible con soporte).

### Excluye (en “Solo Memory”)

- Wizard “3 preguntas” y ranking de recomendaciones (eso es Genie).

- Modelos “automáticos” de recomendación en runtime; aquí solo almacenamos preferencias y señales estructuradas.

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Actores

- **BUYER:** crea recipients, edita perfiles, registra preferencias, guarda regalos hechos, configura recordatorios.

- **SYSTEM/BOT:** ingesta señales post-compra (order_completed, refunds), agenda recordatorios, normaliza tags.

- **SUPPORT (limitado):** acceso solo con ticket/razón para ayudar a corregir datos o investigar problemas (VIEW_SENSITIVE).

- **ADMIN/OPS:** configura taxonomía/validadores por país (categorías, tallas, campos permitidos).

### 3.2 Permisos mínimos

- `memory.recipient.create/read/update/delete.own`

- `memory.profile.read/update.own`

- `memory.history.add/remove.own`

- `memory.reminders.create/update/delete.own`

- `memory.signals.ingest` (system)

- `memory.taxonomy.read` (app)

- `memory.taxonomy.manage` (ops/admin)

- `memory.view_sensitive` (support; requiere reason)

- `memory.audit.read` (audit/admin)

### 3.3 Guards

1. AuthGuard

2. OwnershipGuard: buyer solo accede a recipients propios.

3. DataClassGuard: campos sensibles (alergias, notas privadas) requieren scopes estrictos.

4. PrivacyGuard: por defecto **no compartir** nada con sellers; solo campos explícitamente marcados “shareable”.

5. AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Crear destinatario (Recipient)

**Happy path**

1. Buyer crea recipient: nombre/alias, relación (pareja, mamá, amigo), país/ciudad opcional, zona horaria.

2. Sistema genera `recipient_id` scoped al buyer (no global).

3. Se crea un `memory_profile` vacío con defaults.

**Edge cases**

- Duplicados: si el buyer crea dos recipients con nombres parecidos, se permite, pero se sugiere merge (merge requiere acción explícita y queda auditado). (Suposición: el doc no detalla merge; se define el control mínimo consistente con evitar pérdida de historial).

### 4.2 Capturar preferencias explícitas (Profile update)

**Happy path**

1. Buyer edita:

- `likes_tags[]` (p. ej. “romántico”, “gaming”),

- `dislikes_tags[]`,

- `colors[]`,

- `sizes` (ropa/zapato),

- `budget_range`,

- `allergies` (si aplica),

- `notes_private`.

1. Se valida contra taxonomía por país (evita tags sucios).

2. Se escribe evento `MEMORY_PROFILE_UPDATED` con diff.

**Edge cases**

- Alergias/datos sensibles: marcados como `PII_VAULT` o `PRIVATE` (según clase definida en el proyecto) y con acceso restringido.

### 4.3 Ingesta automática desde compras (Signals → Memory)

**Happy path**

1. En `ORDER_COMPLETED`, si el buyer asignó un recipient a la orden:

- se agrega a `gift_history` (qué se regaló, categoría, precio, fecha),

- se incrementa “señales” para tags/categorías relacionadas (sin recomendar aún).

1. Si hay `REFUND/RETURN`: se registra outcome para no repetir.

**Edge cases**

- Orden sin recipient: no se guarda en memory (evita inferencias erróneas).

- Múltiples destinatarios en una sola orden: si el core no soporta split, no se inventa; se permite asignación manual posterior por el buyer (Suposición: consistente con “no inventar features”).

### 4.4 Recordatorios (Occasions & Reminders)

**Happy path**

1. Buyer guarda fecha (cumpleaños/aniversario).

2. Configura recordatorios (p. ej. 14 días antes, 3 días antes).

3. Scheduler emite `REMINDER_DUE` y el sistema de Notificaciones lo entrega (Inbox como verdad).

**Edge cases**

- Timezone: se usa timezone del hub/país del buyer o del recipient si existe (policy).

- Usuario desactiva marketing: recordatorios transaccionales siguen si son “utilidad personal” (Suposición: el doc menciona recordatorios; la distinción marketing/transaccional depende del sistema Notificaciones).

### 4.5 Privacidad y “Admirador Secreto”

**Happy path**

- Memory guarda preferencias aunque el checkout sea anónimo.

- Seller **no** ve el perfil del recipient; solo ve lo necesario para cumplir la entrega (dirección, instrucciones permitidas) desde el core de orden.

**Edge cases**

- Si el buyer marca un campo como “shareable”, solo se comparte en contextos definidos (p. ej. “mensaje en tarjeta”); nunca alergias o notas privadas.

---

## 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

### 5.1 Propiedad y aislamiento (regla dura)

- Recipients y perfiles son **por buyer** (no globales, no compartidos cross-user).

### 5.2 Privacidad por defecto (regla dura)

- Todo campo es **private_by_default**.

- “Shareable” debe ser explícito por campo (whitelist).

### 5.3 Datos sensibles y clases

- Notas privadas, alergias, tallas: tratar como datos sensibles y restringir acceso.

- Acceso staff requiere reason + `VIEW_SENSITIVE` auditado.

### 5.4 Taxonomía controlada (calidad)

- Tags/categorías deben venir de un catálogo controlado por país (multi-país).

### 5.5 Retención

- Historial de regalos: retención larga (útil) pero sujeta a políticas de borrado de cuenta.

- Si el usuario solicita borrado:

    - se elimina el perfil/recipients donde legalmente permitido,

    - si existe evidencia financiera asociada (órdenes), se conserva lo legal en bóveda fiscal/ledger (fuera de Memory).

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 recipients

Campos mínimos

- `recipient_id`

- `buyer_id`

- `display_name` (alias)

- `relationship_type` (enum)

- `timezone` (nullable)

- `country_code` (nullable)

- `created_at`, `updated_at`

Índices:

- unique(`buyer_id`,`recipient_id`)

- (`buyer_id`,`created_at desc`)

### 6.2 memory_profiles

Campos mínimos

- `profile_id`

- `buyer_id`, `recipient_id`

- `likes_tags[]`

- `dislikes_tags[]`

- `preferred_categories[]`

- `preferred_colors[]`

- `sizes_json` (ropa, zapato, anillo)

- `budget_min`, `budget_max`, `currency`

- `allergies_json` (sensible)

- `notes_private` (sensible)

- `shareable_fields_json` (whitelist)

- `version`

- `created_at`, `updated_at`

Índices:

- unique(`buyer_id`,`recipient_id`)

- GIN en arrays/tags para consultas rápidas (solo internas)

### 6.3 gift_history

Campos mínimos

- `history_id`

- `buyer_id`, `recipient_id`

- `order_id`

- `product_id`

- `category_id`

- `gifted_at`

- `price_amount`, `currency`

- `outcome` (KEPT|REFUNDED|RETURNED)

- `notes` (opcional)

Índices:

- (`buyer_id`,`recipient_id`,`gifted_at desc`)

- unique(`buyer_id`,`order_id`) (si 1 recipient por order)

### 6.4 occasions

Campos mínimos

- `occasion_id`

- `buyer_id`, `recipient_id`

- `occasion_type` (BIRTHDAY|ANNIVERSARY|OTHER)

- `date_mm_dd` o `date_full` (según política)

- `timezone`

- `created_at`

Índices:

- (`buyer_id`,`date_mm_dd`)

- (`recipient_id`,`occasion_type`)

### 6.5 reminders

Campos mínimos

- `reminder_id`

- `buyer_id`, `recipient_id`, `occasion_id`

- `offset_days` (14, 3, 1…)

- `next_fire_at`

- `channel_preferences` (opcional; se respeta Notificaciones)

- `status` (ACTIVE|PAUSED)

- `created_at`

Índices:

- (`next_fire_at`,`status`)

- (`buyer_id`,`status`)

### 6.6 memory_signals (event-sourced ligero)

Campos mínimos

- `signal_id`

- `buyer_id`, `recipient_id` (nullable si no asignado)

- `source_event_type` (VIEW|SAVE|ORDER_COMPLETED|REFUND)

- `entity_type` (PRODUCT|CATEGORY|TAG)

- `entity_id`

- `weight`

- `created_at`

Índices:

- (`buyer_id`,`recipient_id`,`created_at desc`)

- (`source_event_type`,`created_at desc`)

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Eventos del dominio Memory

- `RECIPIENT_CREATED/UPDATED/DELETED`

- `MEMORY_PROFILE_UPDATED`

- `GIFT_HISTORY_ADDED/REMOVED`

- `OCCASION_CREATED/UPDATED`

- `REMINDER_SCHEDULED` / `REMINDER_DUE`

- `MEMORY_SIGNAL_INGESTED`

### 7.2 Idempotencia

- `GIFT_HISTORY_ADDED` idempotente por `(buyer_id, order_id)` (si 1 recipient por orden).

- `MEMORY_SIGNAL_INGESTED` idempotente por `(source_event_id, entity_type, entity_id)` (Suposición: el doc no fija claves; necesario para reintentos).

- `REMINDER_DUE` idempotente por `(reminder_id, fire_at)`.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Órdenes

- Input: `order_completed` + `recipient_id` (si el buyer lo seleccionó).

- Output: `gift_history` + señales.

### Notificaciones

- `REMINDER_DUE` → Notification Center (Inbox como fuente).

### Gobernanza multi-país

- Taxonomías, validadores de tallas/campos, timezone defaults por país/hub.

### Seguridad/Auditoría

- Lecturas sensibles y cambios de perfil auditados (WORM).

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `memory_recipients_created_total{country}`

- `memory_profiles_updated_total{country}`

- `gift_history_added_total{country}`

- `memory_signals_ingested_total{source_event}`

- `reminders_scheduled_total`

- `reminders_fired_total`

- `reminder_delivery_fail_total{channel}`

- `memory_sensitive_reads_total{role}`

### Alertas

- Spike de `memory_sensitive_reads_total` (posible abuso interno)

- `reminder_delivery_fail_total` alto (proveedor notificaciones)

- Crecimiento anormal de signals sin recipient (UX: users no asignan recipient)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Default privado; sellers no acceden a Memory.

- Campos sensibles bajo DataClassGuard; `VIEW_SENSITIVE` obligatorio para staff.

- Auditoría de cambios con diff (qué cambió en preferencias/tallas/fechas).

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Usuarios:** buyer_id canónico; Memory no duplica identidad.

- **Órdenes:** fuente para `gift_history` y outcomes.

- **Notificaciones:** recordatorios y campañas utilitarias.

- **Auditoría:** eventos y lecturas sensibles trazables.

- **Gobernanza multi-país:** taxonomía/validaciones/localización.

---

### Conflictos/incoherencias corregidas (en “Solo Memory”)

1. **Memory como recomendador** → corregido: Memory solo almacena preferencias/señales; recomendación es Genie/Search.

2. **Compartición accidental con sellers** → corregido: privado por defecto + whitelist de campos shareable.

3. **Recipients globales (riesgo de privacidad)** → corregido: recipients son scoped al buyer.

4. **Datos sensibles sin control** → corregido: DataClassGuard + VIEW_SENSITIVE + auditoría WORM.

5. **Señales automáticas sin destinatario (inferencias peligrosas)** → corregido: ingesta post-compra solo si el buyer asignó recipient; si no, no se infiere.

6. **Recordatorios sin timezone/política multi-país** → corregido: timezone gobernado por país/hub/recipient y disparo determinista.

**Inferencia (marcada):** el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).