### Sistema de Notificaciones v2.0 (Notification Center + Inbox) — corregido y unificado

**Fuente de verdad:** “Sistema de Notificaciones”.\
**Dependencia directa:** “Sistema de Mensajería” (evento `NEW_CHAT_MESSAGE`).

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide **canal + plantilla + destinatarios**, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y **siempre** guarda una copia en el **Inbox in-app**, que es la **fuente de verdad auditable**.

**Objetivos (duros):**

1. Garantizar consistencia: **Inbox = verdad**, canales externos = delivery (no garantizado).

2. Confiabilidad: **Outbox pattern** para no perder notificaciones bajo fallos/reintentos.

3. Anti-spam: rate limits + batching + dedupe.

4. Multi-país: plantillas, idioma, legal footers y quiet hours por región/hub y por rol.

5. Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.

---

## 2) Alcance (incluye / excluye)

### Incluye

- **Notification Orchestrator** (rules engine + renderer + dispatcher + inbox writer + audit log).

- **Outbox Pattern** acoplado a transacciones de dominio (orden/pago/disputa).

- Canales: Push (FCM/APNs), Email, SMS, WhatsApp, Inbox in-app.

- Catálogo de eventos notificados (Órdenes, Pagos, Disputas, Payouts, Seguridad/Identidad).

- Preferencias del usuario (opt-ins por canal, idioma, quiet hours, marketing separado).

- Guardrails editor de plantillas por Ops Lead (localización sin tocar código, con whitelist de variables + versioning + rollback).

- “Smart notifications” desde Chat (evento `NEW_CHAT_MESSAGE` con reglas online/offline).

### Excluye

- Chat como feature (es Mensajería; aquí solo consume eventos).

- Marketing completo (P3) si no está habilitado; se soporta en diseño pero requiere opt-in estricto y quiet hours.

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Actores

- **BUYER / SELLER:** receptores; gestionan preferencias.

- **DRIVER/COURIER:** receptor opcional (si aplica).

- **SUPPORT_AGENT / COUNTRY_OPS_LEAD:** receptores internos operativos (alertas P0/P1).

- **FINANCE/AUDIT:** lectura compliance (si habilitado).

- **SYSTEM/BOT:** orquestación, envío, reintentos, escritura Inbox, auditoría.

### 3.2 Permisos mínimos

- `notifications.inbox.read.own`

- `notifications.preferences.read/update.own`

- `notifications.send.system` (solo system)

- `notifications.templates.read`

- `notifications.templates.edit` (ops lead; scoped por país)

- `notifications.audit.read` (audit/finance/admin)

- `notifications.break_glass` (solo admin; razón obligatoria)

### 3.3 Guards

1. AuthGuard

2. OwnershipGuard (inbox/preferencias)

3. ScopeGuard (plantillas por país/hub; staff)

4. PolicyGuard (quiet hours, severidad, canal permitido, legales)

5. DedupeGuard (dedupe_key)

6. RateLimitGuard (por canal/rol)

7. AuditGuard (log obligatorio)

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Emisión desde un evento de dominio (Outbox → Orchestrator)

**Happy path**

1. Un servicio de dominio (Órdenes/Pagos/Disputas) ejecuta su transacción.

2. En la **misma transacción** escribe un registro en `outbox_events` (event_id, event_type, payload).

3. Worker consume `outbox_events` → llama al Orchestrator.

4. Orchestrator:

    - Rules Engine (canal+plantilla+destinatarios)

    - Template Renderer

    - Inbox Writer (siempre)

    - Dispatcher (proveedor por canal)

    - Audit Log (WORM-style)

**Edge cases**

- Reintento del worker: no duplica envíos por dedupe_key.

- Saga de Disputas: no se notifica “resuelto” si falla un paso (refund). En su lugar:

    - `DISPUTE_STEP_FAILED` P0 a Soporte.

### 4.2 Notificación Chat → Bridge (Smart Notifications)

**Happy path**

1. Mensajería emite `NEW_CHAT_MESSAGE`.

2. Notification Center aplica reglas:

- Online en socket ⇒ no push.

- Offline > 30s ⇒ push.

- Push falla o offline > 10 min ⇒ email resumen.

**Edge cases**

- Mensaje con foto/sensible: push/email no muestra preview; solo “entra a la app”.

### 4.3 Preferencias y quiet hours

**Happy path**

- Usuario configura opt-ins por canal y quiet hours (timezone por país/hub).

- Rules Engine respeta preferencias **excepto P0**, que puede bypass quiet hours (seguridad/PIN/OTP/disputa crítica).

### 4.4 Batching / agrupación inteligente

**Happy path**

- 5 cambios de estado seguidos → agrupar en 1 notificación (“Preparando → En camino”).

**Edge cases**

- P0 nunca se agrupa con otros eventos (mantener urgencia y claridad).

---

## 5) Reglas y políticas (prioridades, canales, límites, validaciones)

### 5.1 Regla de oro (invariante)

- **Inbox = fuente de verdad (auditable).**

- Canales externos = delivery best-effort.

### 5.2 Severidad / Priority

- **P0 Crítico:** seguridad, PIN/OTP, fraude, payout failed, `DISPUTE_STEP_FAILED`.

- **P1 Importante:** pago confirmado, orden aceptada/rechazada, en camino.

- **P2 Normal:** preparando, recordatorios suaves.

- **P3 Marketing:** solo opt-in explícito + quiet hours estrictas.

### 5.3 Selección de canal (estrategia canónica)

**P0**

- Inbox + Push

- WhatsApp (si opt-in) o SMS fallback

- Email si trae documento o requiere registro formal

**P1**

- Inbox + Push

- Email solo para “documento/recibo/contrato”

**P2**

- Inbox primero

- Push opcional según preferencias

**P3**

- Solo marketing_opt_in y quiet hours

### 5.4 Preferencias de usuario (perfil)

Campos:

- `opt_in_push, opt_in_email, opt_in_sms, opt_in_whatsapp`

- `quiet_hours_start/end` (timezone del hub)

- `language_preference` (default país)

- `marketing_opt_in` (separado)

### 5.5 Anti-spam / Rate limits (por canal)

Ejemplos definidos:

- Push: 10/h

- WhatsApp/SMS: 3/h

- Email: 5/d (transaccional puede exceder si necesario, gobernado por P0/P1)

**Corrección de incoherencia:** los límites se aplican en el Orchestrator (no en cada servicio de dominio) para que el enforcement sea único.

### 5.6 Dedupe (evitar duplicados por reintento)

**Regla dura:**\
`dedupe_key = event_id + template_id + recipient_id`

### 5.7 Guardrails de plantillas (no permitir “inventar”)

- Variables permitidas: whitelist (por event_type).

- Plantillas P0 (seguridad/disputa) bloqueadas para edición libre; solo cambios controlados/versionados.

- Preview + simulador antes de publicar; versioning + rollback.

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 outbox_events (por servicio de dominio)

Campos mínimos:

- `event_id` (UUID)

- `event_type`

- `aggregate_type`, `aggregate_id`

- `payload_json`

- `created_at`

- `published_at` (nullable)

- `status` (NEW|PUBLISHED|FAILED)

Índices:

- (`status`,`created_at`)

- (`aggregate_type`,`aggregate_id`,`created_at`)

### 6.2 inbox_messages (fuente de verdad)

Campos definidos:

- `id`

- `recipient_user_id`

- `role_context` (BUYER|SELLER|STAFF)

- `event_id`, `event_type`

- `title`, `body`

- `rich_payload_json` (chips/timeline/flags)

- `actions_json` (deep links, subir evidencia, ver orden)

- `severity` (P0–P3)

- `read_at`, `archived_at`

- `created_at`

Índices:

- (`recipient_user_id`,`created_at desc`)

- (`recipient_user_id`,`read_at`)

- (`event_id`,`recipient_user_id`) (dedupe/lookup)

### 6.3 notification_log (auditoría de delivery)

Campos definidos:

- `job_id`

- `event_id`

- `recipient_id`

- `channel`

- `provider`

- `template_version`

- `rendered_hash`

- `status` (queued/sent/delivered/failed)

- `provider_message_id`

- `error_code`

- `retry_count`

- `created_at`, `sent_at`

Índices:

- (`event_id`,`recipient_id`)

- (`status`,`created_at desc`)

- (`provider`,`error_code`,`created_at desc`)

### 6.4 notification_preferences

- `user_id`

- `opt_in_push/email/sms/whatsapp`

- `quiet_hours_start/end`

- `timezone`

- `language_preference`

- `marketing_opt_in`

### 6.5 template_registry (versionado)

Campos definidos:

- `template_id`

- `country_code` (o GLOBAL)

- `channel`

- `role`

- `event_type`

- `language`

- `subject` (email)

- `body`

- `cta_actions_json`

- `legal_footer`

- `version`

- `is_active`

- `created_by`, `created_at`

Índices:

- unique(`country_code`,`channel`,`role`,`event_type`,`language`,`version`)

- (`country_code`,`event_type`,`is_active`)

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Catálogo mínimo de eventos notificados (definido)

**Órdenes**

- `ORDER_CREATED`

- `ORDER_ACCEPTED` / `ORDER_REJECTED`

- `ORDER_PREPARING`

- `ORDER_OUT_FOR_DELIVERY`

- `ORDER_DELIVERED_PENDING_PIN`

- `PIN_CONFIRMED`

- `ORDER_CANCELLED`

**Pagos**

- `PAYMENT_AUTHORIZED`

- `PAID_IN_ESCROW`

- `PAYMENT_FAILED`

**Disputas (Saga 65/15/20)**

- `DISPUTE_OPENED`

- `DISPUTE_NEED_INFO`

- `DISPUTE_STEP_FAILED` (P0 a soporte)

- `DISPUTE_RESOLVED` (solo si saga completa)

**Payouts**

- `PAYOUT_SCHEDULED`

- `PAYOUT_SENT`

- `PAYOUT_FAILED`

**Seguridad/Identidad**

- `PHONE_VERIFIED`

- `KYC_REQUIRED`

- `KYC_APPROVED`

- `SUSPICIOUS_LOGIN`

- `ACCOUNT_LOCKED`

**Chat (bridge)**

- `NEW_CHAT_MESSAGE`

### 7.2 Idempotencia (reglas duras)

- Delivery: dedupe_key fijo `event_id + template_id + recipient_id`.

- Inbox: idempotente por `(event_id, recipient_user_id, template_id)` (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).

- Outbox publish: idempotente por `event_id`.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Proveedores por canal

- Push: FCM/APNs

- Email: proveedor SMTP/ESP

- SMS: proveedor (caro; uso estricto)

- WhatsApp: proveedor BSP (LATAM canal principal)

### Facturación & Documentos

- `PAID_IN_ESCROW` → Email puede incluir PDF (recibo/factura) generado por motor fiscal, referenciado como attachment (links firmados).

### Disputas

- Saga: `DISPUTE_STEP_FAILED` debe alertar soporte inmediatamente y bloquear “resuelto” hasta completar.

### Mensajería

- Consume `NEW_CHAT_MESSAGE` y aplica reglas online/offline + deep-link.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `notifications_queued_total{channel,severity,country}`

- `notifications_sent_total{channel,provider,country}`

- `notifications_failed_total{channel,provider,error_code,country}`

- `inbox_written_total{severity,country}`

- `outbox_backlog_count`

- `delivery_latency_ms_p50/p95{channel}`

- `dedupe_hits_total{channel}`

- `rate_limit_drops_total{channel,severity}`

- `batching_applied_total{event_type}`

### Alertas

- Fallo masivo proveedor (picos `notifications_failed_total`)

- Backlog outbox creciendo (worker caído)

- Spike de P0 (seguridad/fraude)

- `DISPUTE_STEP_FAILED` > umbral (refunds fallando)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Inbox conserva contenido completo + acciones (deep links) como evidencia de “sí se notificó”.

- `notification_log` guarda `rendered_hash` + template_version + provider ids (prueba forense).

- P0 bypass quiet hours pero respeta opt-ins donde legalmente requerido (Suposición: el doc fija bypass por severidad; el matiz legal se mantiene por policy país).

- Preferencias marketing separadas (compliance).

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Órdenes/Pagos:** outbox en la misma transacción; notifica lifecycle y pago.

- **Disputas:** saga gating (no “resolved” si refund falló) + alerta a soporte.

- **Facturación:** adjunta o enlaza documentos en email/inbox.

- **Mensajería:** `NEW_CHAT_MESSAGE` → push/email fallback + deep link.

- **Auditoría/Archivos:** logs WORM-style y attachments mediante storage seguro.

---

### Conflictos/incoherencias corregidas (dentro de Notificaciones)

1. **Push/Email como fuente de verdad** → corregido: Inbox es la verdad; canales externos son best-effort.

2. **Pérdida de notificaciones por fallos transaccionales** → corregido: Outbox pattern dentro de la transacción + worker consumidor.

3. **Duplicados por reintentos** → corregido: dedupe_key `event_id + template_id + recipient_id`.

4. **Soporte marca disputa “resuelta” aunque el refund falló** → corregido: `DISPUTE_STEP_FAILED` P0 a soporte y no se dispara resolved hasta completar la saga.

5. **Plantillas editables sin barandas** → corregido: registry versionado + whitelist variables + bloqueo P0 + preview/simulador + rollback.