### Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado

**Fuente de verdad:** “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Mensajería es un chat **in-app**, **contextual a una orden**, diseñado para que el flujo ideal sea **cero conversación** (“silencio por defecto”) y el chat se active **solo por excepción**, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.

**Objetivos (duros):**

1. Mantener el marketplace seguro: impedir bypass off-platform (teléfonos, pagos externos), acoso, spam y fraude.

2. Ser evidencia operativa/legal: **inmutable**, auditable y exportable para Soporte/Disputas.

3. Ser eficiente: plantillas rápidas por estado y auto-replies por horario.

4. Integración estricta: Órdenes (scope), Notificaciones (bridge), Moderación (pipeline), Soporte (ticket+freeze), Auditoría (logs).

---

## 2) Alcance (incluye / excluye)

### Incluye

- Chat **buyer ↔ seller** por **order_id** (trazable y auditable).

- Adjuntos: fotos de evidencia (y otros adjuntos solo si policy lo permite).

- Plantillas rápidas por estado + auto-replies + “horario de silencio” (derivado de schedule).

- Moderación síncrona en envío (PII/off-platform/acoso/spam) con acciones: `ALLOW`, `ALLOW_WITH_REDACTION`, `QUARANTINE`, `BLOCK`.

- Conversión chat → ticket y **congelamiento** (FROZEN) como control anti-manipulación.

- Bridge a Notification Center: evento canónico `NEW_CHAT_MESSAGE`.

### Excluye (por diseño)

- Chat global libre sin contexto de orden.

- Intercambio directo de email/teléfono (siempre enmascarado; nunca PII).

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Actores

- **BUYER:** envía/lee mensajes en conversaciones de sus órdenes; reporta problema.

- **SELLER:** envía/lee mensajes en conversaciones de sus órdenes; usa plantillas; reporta problema.

- **SYSTEM:** mensajes de sistema, auto-replies, eventos; emite notificaciones.

- **SUPPORT:** convierte a ticket, lee evidencia, congela/gestiona; acceso auditado.

- **MODERATOR / TRUST & SAFETY:** revisa mensajes bloqueados/PII redactions y abuso.

- **ADMIN/OPS LEAD:** auditoría/operación (scoped por país).

### 3.2 Permisos mínimos

- `chat.conversation.read.own`

- `chat.message.send` (buyer/seller)

- `chat.attachment.send`

- `chat.report_problem` (buyer/seller)

- `chat.conversation.freeze` (support/system)

- `chat.conversation.read.support` (support; scoping por ticket)

- `chat.moderation.queue.read/decide` (moderator/T&S)

- `chat.audit.read` (audit/admin)

### 3.3 Guards (canónicos)

1. AuthGuard

2. OrderScopeGuard: conversación solo existe si hay orden válida y el actor es buyer o seller de esa orden.

3. StatusGuard: si `Conversation.status=FROZEN` ⇒ solo lectura; solo `SYSTEM/SUPPORT` pueden emitir `SYSTEM_EVENT`.

4. ModerationGuard (síncrono) antes de persistir/entregar.

5. RateLimitGuard (por conversación y por usuario).

6. AttachmentGuard (mime/size) + StorageGuard (URLs firmadas).

7. AuditGuard (acciones y accesos).

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Creación de conversación (Order-scoped)

**Regla dura:** la conversación **solo** se crea cuando existe una orden válida.

**Happy path**

- En `ORDER_CREATED` o en el primer intento de “Contactar al comprador”:\
    `Conversation(scope_type=ORDER, order_id, buyer_id, seller_id, status=OPEN)`.

**Edge cases**

- Órdenes canceladas: conversación puede archivarse temprano o bloquear envío (policy), pero nunca debe permitir chat “sin orden”.

### 4.2 Envío de mensaje (TEXT/TEMPLATE/ATTACHMENT)

**Happy path**

1. `POST /conversations/:id/messages` con `type` y payload.

2. Moderación síncrona:

- `ALLOW` → persistir.

- `ALLOW_WITH_REDACTION` → persistir versión redactada + log de redacción.

- `QUARANTINE` → persistir como no-entregable y mandar a cola humana.

- `BLOCK` → no persistir o persistir como “blocked event” (ver 7) según auditoría.

1. Persistir mensaje (inmutable) y emitir `NEW_CHAT_MESSAGE` a Notification Center.

2. Entrega:

- si receptor está online en socket → realtime,

- si offline > 30s → push,

- si push falla o sigue offline > 10 min → email resumen.

**Edge cases**

- Mensaje con PII/contacto: `ALLOW_WITH_REDACTION` (oculta PII) o `BLOCK` según gravedad.

- Flood: RateLimitGuard bloquea; se registra `MESSAGE_BLOCKED` con reason.

### 4.3 Escenario A “Orden silenciosa” (mayoría)

- Buyer paga → seller acepta/prepara → entrega → PIN/QR → fondos liberados.

- No se envían mensajes.

### 4.4 Escenario B “Excepción” (bridge)

- Seller pulsa “Contactar al Comprador”, elige plantilla rápida; si buyer no está activo, notificación y deep link a conversación.

### 4.5 Auto-replies + horario de silencio

**Happy path**

- Buyer escribe fuera del horario del seller → `SYSTEM` responde automático:\
    “El vendedor no está disponible… tu mensaje ha sido notificado…”.

**Regla dura:** horario de silencio no bloquea el envío; solo cambia el comportamiento de notificación y auto-reply.

### 4.6 Chat → Ticket (Reportar Problema) + Freeze

**Happy path**

1. Buyer o seller presiona “Reportar Problema”.

2. Se crea `SupportTicket(order_id, conversation_id)` y se adjunta historial completo como evidencia.

3. `Conversation.status = FROZEN` (solo lectura).

4. Se notifica a Soporte (y a Country Ops Lead si aplica).

**Edge cases**

- Reapertura excepcional: solo soporte con razón auditada (break-glass), y se registra `CONVERSATION_UNFROZEN`.

### 4.7 Archivo por retención

- Se archiva automáticamente X días después de `ORDER_COMPLETED`.

- Default: `RETENTION_DAYS_AFTER_COMPLETED = 90` (configurable por país/policy).

---

## 5) Reglas y políticas (límites, validaciones, privacidad)

### 5.1 Orden-scope como invariante

- Solo existe conversación si hay `order_id`.

- Solo buyer/seller de esa orden pueden escribir.

### 5.2 Inmutabilidad (evidencia)

- Mensajes no se editan ni se borran.

- Corrección = nuevo mensaje.

### 5.3 Estados de entrega

- `SENT`: persistido

- `DELIVERED`: entregado al cliente

- `READ`: leído

- `FAILED`: falla push/email; el mensaje queda en chat igual

### 5.4 Privacidad y relay

- No intercambio de teléfonos/emails; todo sale desde sistema (noreply) y no revela PII.

- UI muestra identidad marketplace-safe (nombre de tienda / alias).

### 5.5 Adjuntos (seguridad)

- Solo fotos de evidencia por defecto.

- Storage seguro:

    - URLs firmadas TTL corto

    - ACL por `conversation_id` y `order_id`

    - expiración alineada a retención del chat

- Notificación externa nunca incluye binario ni preview sensible.

### 5.6 Anti-acoso / anti-spam / anti-fuga (off-platform)

- Moderación síncrona en cada envío.

- Rate limiting por conversación y por usuario.

- Reincidencia: escalado a Moderación/Trust (shadow limit, pre-moderación, suspensión).

### 5.7 “Freeze” como control legal y operativo

- En disputa/ticket: FROZEN es solo lectura para evitar manipulación/elevación.

- Solo SYSTEM/SUPPORT agrega `SYSTEM_EVENT` en frozen (p.ej. “Ticket creado”).

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 Conversation (order-scoped)

Campos explícitos:

- `conversation_id`

- `scope_type = ORDER`

- `order_id` (FK)

- `seller_id`, `buyer_id`

- `status` ENUM: `OPEN | FROZEN | ARCHIVED`

- `created_at`, `last_message_at`

- `frozen_reason_code` (nullable)

Índices:

- unique(`order_id`) (1 conversación por orden)

- (`seller_id`,`last_message_at desc`)

- (`buyer_id`,`last_message_at desc`)

- (`status`,`last_message_at desc`)

### 6.2 Message (inmutable)

Campos explícitos:

- `message_id`, `conversation_id`

- `sender_role` ENUM: `BUYER | SELLER | SYSTEM | SUPPORT`

- `type` ENUM: `TEXT | TEMPLATE | ATTACHMENT | SYSTEM_EVENT`

- `body_text` (nullable)

- `attachment_id` (nullable)

- `created_at`

Estados de entrega (tabla separada):\
`message_delivery_status(message_id, recipient_id, status, updated_at)` con `SENT/DELIVERED/READ/FAILED`.

Índices:

- (`conversation_id`,`created_at asc`)

- (`conversation_id`,`message_id`)

- (`recipient_id`,`status`,`updated_at desc`)

### 6.3 ChatAttachment (referencia a Sistema de Archivos)

- `attachment_id`

- `file_id` (Storage)

- `conversation_id`, `order_id`

- `uploaded_by_role`

- `mime`, `size_bytes`

- `created_at`

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Eventos auditables mínimos (obligatorios)

Listado explícito:

- `MESSAGE_SENT`

- `MESSAGE_BLOCKED`

- `PII_REDACTED`

- `ATTACHMENT_UPLOADED`

- `CONVERSATION_FROZEN`

- `TICKET_CREATED`

- `AGENT_VIEWED_CONVERSATION`

### 7.2 Evento canónico de notificaciones

- `NEW_CHAT_MESSAGE` publicado al Notification Center.

### 7.3 Idempotencia

- Send message: idempotencia por `client_message_id` por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).

- Ticket create: idempotente por `(order_id, conversation_id)`.

- Freeze: idempotente por `(conversation_id, status=FROZEN)`.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Órdenes

- `order_id` es el scope.

- Plantillas dependen del estado de orden (`IN_TRANSIT`, `DELIVERED`, etc.).

### Notificaciones

- Consumo de `NEW_CHAT_MESSAGE`:

    - socket realtime si online

    - push si offline > 30s

    - email si push falla o offline > 10 min

### Moderación & Cumplimiento

- `send_message` pasa por moderación síncrona.

- Acciones: allow/redact/quarantine/block.

### Soporte

- “Reportar Problema” crea ticket y congela chat.

- Adjunta historial completo como evidencia.

### Auditoría

- Acceso de agentes/admin queda registrado (AGENT_VIEWED_CONVERSATION).

### Archivos

- Adjuntos van a storage seguro con URLs firmadas TTL corto y ACL por conversación/orden.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `chat_conversations_created_total{country}`

- `chat_messages_sent_total{type,country}`

- `chat_messages_blocked_total{reason,country}`

- `pii_redacted_total{country}`

- `chat_attachments_uploaded_total{country}`

- `chat_delivery_latency_ms_p50/p95`

- `chat_offline_push_sent_total{country}`

- `chat_offline_email_sent_total{country}`

- `chat_conversations_frozen_total{reason,country}`

- `chat_tickets_created_total{country}`

### Alertas

- Spike en `chat_messages_blocked_total{reason=OFF_PLATFORM}` (intento de bypass)

- Spike en `pii_redacted_total` (fuga/ataque)

- Crecimiento de `delivery_latency` (socket/infra)

- Spike de freezes (operación/disputas) anormal

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Inmutabilidad de mensajes como evidencia.

- Auditoría obligatoria de acciones clave y accesos.

- Freeze en ticket/disputa para preservar evidencia y evitar manipulación.

- Retención por país; default 90 días post `COMPLETED` con archivado automático.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Órdenes:** scope por `order_id`, plantillas por estado.

- **Notificaciones:** `NEW_CHAT_MESSAGE` y reglas de bridging.

- **Moderación:** envío pasa por pipeline anti-PII/off-platform/acoso/spam.

- **Soporte:** ticket + freeze con evidencia completa.

- **Auditoría:** eventos mínimos auditables.

- **Archivos:** adjuntos privados con URLs firmadas y ACL por conversación.

---

### Conflictos/incoherencias corregidas (dentro de Mensajería)

1. **Chat usado como requisito de la orden** → corregido: “silencio por defecto”; chat es excepción, no dependencia.

2. **Chat global sin contexto (riesgo fraude/acoso)** → eliminado: solo order-scoped.

3. **Edición/borrado de mensajes (rompe evidencia)** → prohibido: mensajes inmutables.

4. **PII y off-platform sin control** → corregido: moderación síncrona + redacción/bloqueo + rate limit + escalamiento a Trust.

5. **Manipulación durante disputa** → corregido: “Reportar Problema” crea ticket y congela conversación (FROZEN) para preservar evidencia.