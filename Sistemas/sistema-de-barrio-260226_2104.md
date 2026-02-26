### Sistema Barrio v2.0 (Círculos privados) — corregido y unificado

**Basado en:** definición “Social layer: Barrio (o Círculos)” + sus componentes (recipients compartidos, fechas opt-in, wishlists temáticas, notificación de regalo entrante).

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Barrio es una **capa social privada** encima de **Usuarios + Memory (recipients/perfil/agenda)** que permite organizar familiares/amigos en grupos (“barrios/círculos”) y habilitar:

- lista de recipients dentro del grupo (usuarios Aventide o externos),

- **fechas importantes compartidas (opt-in)**,

- **wishlists temáticas** (preferencias, no productos específicos),

- y “apps hablándose”: opción de **notificar al recipient que le llegará un regalo** (sin revelar qué) respetando sorpresa y “Admirador Secreto”.

**Objetivos (duros):**

1. Crear “red social ligera” sin romper privacidad ni el core transaccional.

2. Aumentar retención: agenda compartida + recordatorios + network effect (“cada regalo puede traer 1 usuario nuevo”).

3. No duplicar sistemas: Barrio **no reemplaza** Memory/Recipients; los **referencia** o crea “recipients externos” dentro del círculo. (Inferencia consistente con “capa social encima del Perfil + Usuarios”).

4. Control total de consentimientos (opt-in por campo/fecha, y por notificación de regalo entrante).

---

## 2) Alcance (incluye / excluye)

### Incluye

- Creación y gestión de **Círculos (Barrios)** privados.

- Miembros del círculo (usuarios Aventide) + **invitación/aceptación** (evento explícito).

- Inclusión de **recipients** en el círculo:

    - recipients que son usuarios Aventide,

    - recipients **externos** (no usuarios).

- **Fechas compartidas (opt-in)** por recipient/occasión.

- **Wishlists temáticas** (gustos/temas, no “quiero X producto”).

- “Notificación de regalo entrante” opcional si el recipient es usuario Aventide (sin revelar qué).

### Excluye

- Feed público, follows, likes globales, contenido viral (no definido).

- Transferencia de puntos: la capa social **no** hace “puntos transferibles”; lo regalable serían cupones/gift cards si existen (mencionado como regla de diseño social/gamificado).

---

## 3) Actores y permisos (RBAC) + guards

### Actores

- **CircleOwner (buyer)**: crea el barrio, invita, configura privacidad/fechas compartidas, gestiona recipients del círculo.

- **CircleMember (buyer)**: ve lo compartido, sugiere/actualiza (según permisos), usa la agenda compartida.

- **RecipientUser**: usuario Aventide que puede recibir notificación de “te llegará un regalo” (opt-in).

- **SYSTEM**: dispara recordatorios/notificaciones a partir de eventos del círculo, y emite auditoría.

### Permisos mínimos (RBAC/ABAC)

- `circle.create`

- `circle.read` (solo miembros)

- `circle.update` (owner/admins del círculo)

- `circle.delete` (owner + condiciones)

- `circle.invite.send` / `circle.invite.revoke`

- `circle.invite.accept` / `circle.invite.reject`

- `circle.member.remove` (owner)

- `circle.recipient.link` / `circle.recipient.unlink`

- `circle.shared_dates.manage` (opt-in por recipient/fecha)

- `circle.wish_theme.manage`

- `circle.gift_incoming_notify.configure` (checkout; por orden)

### Guards (reglas duras)

1. **Private-by-default**: nada del círculo es visible fuera (incluye recipients externos). (Inferencia: consistente con “grupo privado”).

2. **ConsentGuard (opt-in)**:

    - fechas compartidas requieren consentimiento explícito.

    - notificación de regalo entrante es opción en checkout.

3. **Anonimato guard**: si el buyer está en modo anónimo, se respeta (no revelar identidad).

4. **Data minimization**: miembros solo ven “temas” y “fechas compartidas”, no PII sensible (direcciones, alergias, notas privadas). (Inferencia: consistente con privacidad/Admirador Secreto).

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Crear Barrio

**Happy path**

1. Buyer crea `circle` (nombre, foto opcional, reglas de visibilidad internas).

2. Buyer queda como `OWNER`.

3. Círculo inicia vacío o con recipients existentes del buyer (link).

**Edge cases**

- Buyer intenta compartir recipient sin consentimiento del dueño del dato (si recipient pertenece a otro miembro): prohibido; cada miembro comparte solo lo suyo. (Inferencia: evita fuga de datos)

### 4.2 Invitar y unir miembros (circle_invite_sent/accepted)

**Happy path**

1. Owner envía invitación a usuario Aventide (por user_id/phone/email según Usuarios).

2. Sistema emite evento `circle_invite_sent`.

3. Invitado acepta → `circle_invite_accepted` y se crea `circle_member`.

**Edge cases**

- Invite expirado: requiere re-invitar (TTL).

- Invite a usuario inexistente: opcional “invitar por link” (no definido en doc; **no se implementa** aquí).

### 4.3 Compartir fechas importantes (opt-in)

**Happy path**

1. Un miembro selecciona un recipient y marca qué ocasiones comparte (cumple, aniversario, etc.).

2. Otros miembros ven solo: fecha (o solo mes/día según privacidad) + tipo de ocasión.

3. Recordatorios: Notificaciones se disparan a miembros según configuración. (Inferencia: consistente con “agenda/recordatorios” y capa social)

**Edge cases**

- Privacidad: permitir compartir “mes/día” sin año (edad). (Inferencia: práctica estándar; no contradice el doc)

### 4.4 Wishlists temáticas (no objetivas)

**Happy path**

1. Por recipient o por círculo, se crean “wish themes”: lista de gustos/temas (café, cozy, gadgets útiles…).

2. Esos temas alimentan `recipient_fit` para recomendaciones (Genie/Search), sin convertirse en catálogo fijo. (Inferencia: el doc lo afirma conceptualmente).

**Edge cases**

- Moderación: evitar temas sensibles/abusivos (dependencia Moderación).

### 4.5 Notificación “te va a llegar un regalo” (sin revelar qué)

**Happy path**

1. En checkout, si recipient es usuario Aventide, aparece opción: notificar o sorpresa total.

2. Si notificar: se emite evento a Notificaciones: “incoming gift” sin detalles del producto.

3. Si buyer está en modo anónimo, se respeta (no se revela identidad).

**Edge cases**

- Recipient no es usuario: no hay notificación in-app; opcional SMS/email no está definido → fuera.

---

## 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

### Reglas de privacidad (canónicas)

- **Círculos siempre privados**: no indexables, no descubribles.

- **Share granular**:

    - Fechas: opt-in por ocasión.

    - Temas: opt-in por recipient/círculo.

- **Sorpresa/anónimo**:

    - notificación entrante no revela “qué”

    - anonimato se respeta siempre.

### Límites (para anti-abuso) — Suposición

- `max_circles_per_user`, `max_members_per_circle`, `max_recipients_per_circle`, `max_wish_themes_per_recipient` versionados en policy engine (consistente con gobernanza).

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 circles

- `circle_id`

- `owner_user_id`

- `name`

- `status` (ACTIVE|ARCHIVED)

- `created_at`, `updated_at`

Índices:

- (`owner_user_id`, `created_at desc`)

### 6.2 circle_members

- `circle_id`

- `user_id`

- `role` (OWNER|ADMIN|MEMBER)

- `status` (ACTIVE|LEFT|REMOVED)

- `joined_at`

Índices:

- unique(`circle_id`,`user_id`)

- (`user_id`,`joined_at desc`)

### 6.3 circle_invites

- `invite_id`

- `circle_id`

- `invited_by_user_id`

- `invitee_user_id` (si existe)

- `invitee_contact` (hash/normalizado si es por teléfono/email; si aplica)

- `status` (SENT|ACCEPTED|REJECTED|EXPIRED|REVOKED)

- `expires_at`, `created_at`

Eventos: `circle_invite_sent/accepted` (mencionado explícitamente).

### 6.4 circle_recipients (link a Memory)

- `circle_id`

- `owner_user_id` (quién “aporta” este recipient)

- `recipient_ref_type` (AVENTIDE_USER|EXTERNAL_RECIPIENT)

- `recipient_ref_id` (user_id o recipient_id de Memory)

- `display_name_in_circle` (opcional)

- `created_at`

Índices:

- unique(`circle_id`,`owner_user_id`,`recipient_ref_type`,`recipient_ref_id`)

### 6.5 circle_shared_occasions

- `circle_id`

- `owner_user_id`

- `recipient_ref_type`, `recipient_ref_id`

- `occasion_type`

- `date_mm_dd` (y `year` nullable)

- `share_level` (MM_DD_ONLY|FULL_DATE)

- `created_at`, `updated_at`

Soporta “fechas importantes compartidas (opt-in)”.

### 6.6 wish_themes

- `theme_id`

- `circle_id` (nullable si es personal)

- `owner_user_id`

- `recipient_ref_type`, `recipient_ref_id`

- `themes[]` (tags/strings normalizados)

- `created_at`, `updated_at`

Wishlists temáticas “no objetivas”.

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### Eventos de dominio (mínimos)

- `CIRCLE_CREATED`

- `CIRCLE_UPDATED`

- `CIRCLE_INVITE_SENT` / `CIRCLE_INVITE_ACCEPTED`

- `CIRCLE_MEMBER_REMOVED`

- `CIRCLE_RECIPIENT_LINKED`

- `CIRCLE_SHARED_OCCASION_OPTED_IN` / `...OPTED_OUT`

- `CIRCLE_WISH_THEME_UPDATED`

- `GIFT_INCOMING_NOTIFICATION_REQUESTED` (checkout)

### Idempotencia (Suposición necesaria)

- Invite: idempotente por `(circle_id, invitee_user_id/contact_hash, active_window)`

- Accept: idempotente por `(invite_id)`

- Link recipient: idempotente por unique key en `circle_recipients`.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Memory (Recipients/Agenda)

- Barrio **no guarda** perfiles completos; referencia recipients y consume/produce:

    - links a recipients (usuario Aventide o externo)

    - ocasiones compartidas (subset)

    - wish themes (subset)

### Notificaciones

- “Gift incoming” para recipient usuario Aventide (sin revelar qué)

- Respeta anónimo/sorpresa

### Usuarios

- identidad y membresía son por `user_id`.

- invitaciones usan mecanismos definidos en Usuarios (contactos/lookup). (Inferencia: dependencia natural)

### Genie/Search

- `wish_themes` alimentan `recipient_fit` (no convierte en catálogo fijo).

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `circles_created_total`

- `circle_invites_sent_total` / `circle_invites_accepted_total`

- `circle_members_active_total`

- `circle_shared_occasions_total`

- `wish_themes_updated_total`

- `gift_incoming_notify_opt_in_rate`

### Alertas

- Spike de invites (abuso/spam)

- Tasa de aceptación anómala por círculo (posible granja)

- Errores de notificación “gift incoming” (dependencia Notificaciones)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Auditoría append-only de:

    - creación/edición de círculos,

    - invitaciones,

    - cambios de opt-in/opt-out de fechas,

    - cambios de wish themes,

    - disparo de “gift incoming” (con marca de “anon/sorpresa”).

- Retención:

    - datos sociales (círculos/temas) siguen la política de “perfil/marketing” (si aplica crypto-shredding por solicitud) y se separan de lo financiero. (Inferencia: consistente con el enfoque general del proyecto, pero no está detallado en la sección Barrio)

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Memory:** recipients, ocasiones (agenda), señales y preferencias; Barrio referencia/subset.

- **Usuarios:** identidad, control de acceso, invitaciones.

- **Notificaciones:** “regalo entrante” opt-in y sorpresa/anónimo.

- **Genie/Search:** wish themes alimentan “recipient_fit” sin catálogo fijo.

---

### Conflictos/incoherencias corregidas (en Barrio)

1. **“Barrio” confundido con “Zone/Barrio geográfico”** → corregido: Barrio aquí es **capa social (Círculos)**; lo geográfico es **Zone** en Cobertura/Gobernanza (otra entidad).

2. **Compartir PII sensible dentro del grupo** → corregido: solo se comparte subset (fechas opt-in y temas), no direcciones/alergias/notas. (Inferencia consistente con “privado + Admirador Secreto”).

3. **Notificación de regalo revelando detalles** → corregido: notificación “te va a llegar un regalo” **sin revelar qué**, y se respeta sorpresa total/anónimo.

4. **Invitaciones sin ciclo de vida** → corregido: `SENT/ACCEPTED/REJECTED/EXPIRED/REVOKED` + eventos `circle_invite_sent/accepted` explícitos.

5. **Wishlists “objetivas” tipo marketplace (rompe dinámica)** → corregido: wishlists son **temáticas** (gustos), no lista rígida de productos específicos.

**Inferencia (marcada):** la documentación define el concepto y componentes, pero no especifica esquema de tablas, TTLs de invitación, ni campos exactos; se propuso un modelo mínimo compatible con el estilo del proyecto (eventos, privacidad, dependencias, idempotencia) sin inventar funcionalidades públicas no descritas.