### Sistema de Órdenes v2.0 (corregido y unificado)

**Fuente de verdad:** documento “Sistema de Órdenes (Aventide Gift)”.\
**Objetivo del rewrite:** convertir Órdenes en un **motor operativo determinista** (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema que convierte un checkout en una entrega real con:

- **Snapshot inmutable** de precios/fees/items/dirección/promesa.

- **Máquina de estados estricta** (no saltos).

- **Reglas cerradas de cancelación** por estado (y ventanas).

- **Evidencia de entrega (Tridente)**: PIN + GPS + Foto como verdad operacional.

- **Escrow**: dinero retenido hasta cierre de entrega.

- **SLA**: aceptación rápida, producción, pickup, entrega, con alertas/acciones.

- **Action Stream / timeline** como columna vertebral para notificaciones, soporte e investigación.

**Objetivos:**

1. “Estado manda”: ninguna acción fuera de transición válida.

2. “Dinero retenido”: seller no toca fondos antes de entrega confirmada.

3. “Evidencia > opiniones”: disputas se resuelven con rastro (PIN+GPS+Foto+logs).

4. “SLA medible”: evitar debates; todo se mide por deadlines.

---

## 2) Alcance (incluye / excluye)

### Incluye

- Checkout → creación de orden con snapshot.

- Pago y transición a escrow.

- Coordinación seller/fulfillment (producción, pickup, tránsito, entrega).

- Cancelaciones y auto-cancel por SLA.

- Evidencias PoD (delivery_proof).

- Timeline/Action Stream y vistas (Seller Kanban + Buyer tracking).

- Acople con refund flow (máquina separada).

### Excluye

- Cálculo profundo de fees/impuestos (solo se **snapshottea** su resultado).

- Motor de reembolsos/decisión: Soporte/Disputas decide outcomes; Órdenes ejecuta transiciones y bloqueos.

- Motor de logística/driver como sistema completo (Órdenes emite/consume eventos).

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Actores

- **BUYER**: crea orden, cancela en pre-aceptación, trackea, confirma/abre disputa.

- **SELLER**: acepta (SLA), produce, marca ready, gestiona handoff.

- **DRIVER/FULFILLMENT** (si aplica): pickup, tránsito, entrega, captura evidencia.

- **SUPPORT_AGENT**: opera casos, aplica outcomes (pero no inventa estados).

- **COUNTRY_OPS_LEAD**: supervisa SLAs y excepciones por país/zona.

- **SYSTEM/BOT**: timers, auto-cancel, notificaciones, conciliación.

### 3.2 Permisos mínimos (namespaces)

- `orders.create` (buyer)

- `orders.cancel.pre_accept` (buyer)

- `orders.cancel.request_post_accept` (buyer → crea caso, no cancela directo)

- `orders.accept` (seller)

- `orders.update_status.production` (seller)

- `orders.update_status.ready_for_pickup` (seller)

- `orders.update_status.in_transit` (driver/system)

- `orders.mark_delivered` (driver/seller según modelo)

- `orders.confirm_delivery` (system/buyer según validación)

- `orders.capture_proof` (driver/seller)

- `orders.support.apply_outcome` (support) — restringido por policy/outcomes

- `orders.ops.override` (ops/admin) — solo vía break-glass/policy si existe

### 3.3 Guards (backend manda)

Cadena canónica:

1. Auth

2. PermissionGuard

3. OwnershipGuard (buyer_id/seller_id según endpoint)

4. ScopeGuard (country/hub/zone para internos)

5. PolicyGuard (reglas por país: ventanas, SLAs, allowed cancel reasons)

6. StateGuard (validación de transición)

7. MoneyGuard (escrow/release y antifraude)

8. EvidenceGuard (requisitos PoD para cerrar)

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Checkout → Creación de orden (snapshot)

**Happy path**

1. Buyer inicia checkout.

2. Sistema valida entregabilidad/capacidad (depende de Contenido/Capacidad).

3. Se crea `order` en estado `CREATED` con snapshot:

    - items + add-ons,

    - pricing final,

    - fees/taxes resultantes,

    - dirección,

    - promesa (ETA/ventana),

    - contexto geo (country/hub/zone),

    - policy_version/config_version.

**Edge cases**

- Si zona no activa / sin capacidad para la ventana: no se permite crear o se crea como “no confirmable” (según policy); en cualquier caso, no se debe pagar si no es entregable. (Integración obligatoria con Capacidad/Logística; aquí se fija el enforcement en el gate de checkout, coherente con “lo visible debe ser comprable”.)

### 4.2 Pago → Escrow

**Happy path**

- `CREATED → PAID_IN_ESCROW` cuando pago se autoriza y el dinero queda retenido.

**Edge cases**

- Pago falla: orden queda `CREATED` y expira por timer.

- Reintentos: idempotencia por `payment_attempt_id`.

### 4.3 SLA de aceptación → Seller handling

**Happy path**

- `PAID_IN_ESCROW → ACCEPTED` cuando el seller acepta dentro de SLA (“Acepta en 5 min”).

- `ACCEPTED → IN_PRODUCTION`

- `IN_PRODUCTION → READY_FOR_PICKUP`

**Edge cases (críticos)**

- SLA vencido sin respuesta:

    - evento “no atendida”,

    - notificar buyer,

    - escalar a soporte/ops para decisión (cancelar o reasignar por policy).

- Seller intenta saltar estados (ej. ACCEPTED→READY_FOR_PICKUP): denegado por StateGuard.

### 4.4 Logística / entrega (cuando aplica)

**Happy path**

- `READY_FOR_PICKUP → IN_TRANSIT` cuando fulfillment toma la orden.

- `IN_TRANSIT → DELIVERED_PENDING_RELEASE` al marcar entregada (pero aún sin liberar escrow).

- `DELIVERED_PENDING_RELEASE → COMPLETED` cuando se valida entrega y se libera escrow.

**Edge cases**

- Entrega marcada pero sin evidencia: permanece en `DELIVERED_PENDING_RELEASE` hasta PoD válido o caso de soporte.

- GPS con baja precisión: EvidenceGuard puede exigir recaptura o señal adicional.

### 4.5 Evidencias (Proof of Delivery) — Tridente

**Regla dura:** para completar orden se requiere PoD fuerte:

- Foto obligatoria

- GPS automático (lat/lng/accuracy)

- PIN ingresado (hash)

Se crea `delivery_proof` ligado a `order_id` con:\
`photo_url, gps_lat, gps_lng, gps_accuracy, pin_hash, captured_at, captured_by_user_id, device_fingerprint, ...`

### 4.6 Refunds/Reembolsos (máquina separada)

**Regla dura:** estado de orden ≠ estado de refund.\
Refund flow (ejemplo): `REQUESTED → UNDER_REVIEW → APPROVED/REJECTED → PARTIAL_REFUND`\
La orden puede estar `DELIVERED_PENDING_RELEASE` o `COMPLETED` mientras corre el refund.

---

## 5) Reglas y políticas (límites, ventanas, validaciones)

### 5.1 Principios sagrados (enforcement)

- **Estado manda** (no saltos).

- **Escrow hasta entrega real** (release solo tras validación).

- **Evidencia manda en disputa** (PoD).

- **SLA ejecutable** (timers + acciones).

### 5.2 Cancelación por Buyer (reglas cerradas del doc)

- **Sin penalidad** si estado:

    - `CREATED` o `PAID_IN_ESCROW` y aún **no** está `ACCEPTED`.

- **Restringida/penalizada** si ya está:

    - `ACCEPTED`, `IN_PRODUCTION`, `READY_FOR_PICKUP`, `IN_TRANSIT`, `DELIVERED_PENDING_RELEASE`\
        En estos estados:

    - no hay “botón libre”,

    - exige reason_code,

    - crea caso,

    - reversa financiera según policy/outcome (Soporte/Disputas decide).

### 5.3 Cancelación por Seller (controlada)

- Permitida solo con reason_codes (stock roto, accidente, incapacidad…).

- Todo queda en timeline + impacta SLA/reputación.

### 5.4 Auto-cancel / escalamiento por SLA

- Si vence `accept_by`: evento + notificación + escalamiento a ops/soporte.\
    **Suposición:** la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)

### 5.5 Lead time, cut-off y promesa (persistido en snapshot)

En checkout se calcula promesa con:

- lead time por producto/seller,

- cut-off por día/ventana,\
    y se guardan timestamps:\
    `accept_by`, `production_due_at`, `ready_for_pickup_due_at`.

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 Order (core)

`orders`

- `order_id` (UUID)

- `buyer_id`, `seller_id`

- `country_code`, `hub_id`, `zone_id`

- `status` (enum)

- `created_at`, `updated_at`

- `promises` JSON `{accept_by, production_due_at, ready_for_pickup_due_at, eta_window}`

- `address_snapshot` JSON (inmutable)

- `items_snapshot` JSON (items + add-ons + qty)

- `pricing_snapshot` JSON `{subtotal, discounts, fees, taxes, total, currency, fx_rate, total_usd}`

- `policy_snapshot` JSON `{policy_version, ui_config_version, fee_rule_id}`

- `escrow` JSON `{provider, escrow_id, amount, currency, status}`

- `cancel_meta` JSON `{requested_by, reason_code, requested_at, outcome_case_id}`

**Índices:**

- `(seller_id, status, created_at)`

- `(buyer_id, created_at)`

- `(country_code, hub_id, zone_id, status, created_at)`

- unique `(order_id)`

### 6.2 Timeline / Action Stream (append-only)

`order_events`

- `event_id` (UUID unique)

- `order_id`

- `event_name`

- `ts_utc`

- `actor_type` (buyer|seller|driver|support|system)

- `actor_id`

- `from_status`, `to_status` (nullable para eventos no estado)

- `payload` JSON (reason_code, evidence refs, etc.)

- `trace_id`, `request_id`

### 6.3 Proof of Delivery

`delivery_proofs`

- `order_id` (unique)

- `photo_url`

- `gps_lat`, `gps_lng`, `gps_accuracy`

- `pin_hash`

- `captured_at`

- `captured_by_user_id`

- `device_fingerprint`

- `validation_status` (PENDING|VALID|INVALID)

### 6.4 Refund requests (separado)

`refund_requests`

- `refund_id`

- `order_id`

- `state` (REQUESTED/UNDER_REVIEW/APPROVED/REJECTED/PARTIAL_REFUND)

- `requested_by`

- `reason_code`

- `amount_requested`, `amount_approved`

- `case_id` (Soporte/Disputas)

- timestamps

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Eventos mínimos del dominio Órdenes

- `ORDER_CREATED`

- `PAYMENT_AUTHORIZED_ESCROWED` (CREATED→PAID_IN_ESCROW)

- `ORDER_ACCEPTED` (→ACCEPTED)

- `ORDER_IN_PRODUCTION`

- `ORDER_READY_FOR_PICKUP`

- `ORDER_DRIVER_ASSIGNED` (si aplica)

- `ORDER_PICKED_UP` (→IN_TRANSIT)

- `ORDER_DELIVERED_MARKED` (→DELIVERED_PENDING_RELEASE)

- `DELIVERY_PROOF_CAPTURED`

- `DELIVERY_PROOF_VALIDATED`

- `ESCROW_RELEASED`

- `ORDER_COMPLETED`

- `ORDER_CANCEL_REQUESTED`

- `ORDER_CANCELLED`

- `REFUND_REQUESTED/UPDATED`

### 7.2 Triggers críticos

- Timer `accept_by` → `ORDER_ACCEPTANCE_SLA_BREACHED`

- Al pasar `READY_FOR_PICKUP` → emitir evento consumible por Logística: `ORDER_READY_FOR_PICKUP`

### 7.3 Idempotencia

- `event_id` unique en `order_events`

- endpoints mutables con `idempotency_key`

- transiciones dedupe por `(order_id, to_status)` + ventana temporal

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### 8.1 Pagos/Escrow

- Input: resultado de autorización.

- Output: `PAID_IN_ESCROW` + `escrow_id`.

- Release: solo al validar PoD y transición a COMPLETED.

### 8.2 Contenido/Capacidad/Logística (antes y durante)

- Checkout consulta entregabilidad + ventanas.

- En orden se persiste `promises` y `items_snapshot` con add-ons (operación).

### 8.3 Soporte/Disputas

- Post-aceptación: cancel requests → caso.

- Refund requests → caso y outcome.

### 8.4 Analítica

- Cada transición emite evento analítico (server-side) y alimenta facts/rollups.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Logs

- Transiciones con `order_id`, `from/to`, `actor`, `reason_code`, `trace_id`

- Evidencia: captura/validación (sin exponer PII)

### Métricas

- `orders_created_total{country}`

- `orders_acceptance_sla_breached_total{country}`

- `orders_time_to_accept_seconds`

- `orders_time_to_complete_seconds`

- `orders_cancelled_total{reason,country}`

- `delivery_proof_invalid_total{reason}`

### Alertas

- Spike de SLA breached por seller/zona.

- Delivery proofs inválidos > umbral (fraude o UX rota).

- Escrow release lag > umbral (dinero retenido injustificadamente).

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

### Auditoría fuerte

- Toda transición y cancelación exige registro en `order_events`.

- Acciones de soporte/ops dejan reason_code y referencia a caso.

- Evidencia (foto) via storage con URLs firmadas y ABAC “need-to-know”.

### Integridad

- Order snapshot inmutable: cualquier ajuste debe crear **evento compensatorio**, no “editar el pasado”.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Contenido:** add-ons reflejados en order snapshot; producto publicado implica capacidad/logística válida.

- **Capacidad/Logística:** promesa y cut-off determinan deadlines; “lo visible debe ser comprable/entregable”.

- **Usuarios/Jerarquía:** RBAC + scopes para paneles; seller solo lo suyo; ops por país.

- **Soporte/Disputas:** cancel post-aceptación y refunds por casos/outcomes.

- **Analítica:** eventos server-side por transición (SSOT).

---

### Conflictos/incoherencias corregidas (dentro de Órdenes)

1. **Cancelar “en cualquier momento”** → corregido: pre-aceptación libre; post-aceptación crea caso y outcome.

2. **Completar sin evidencia** → corregido: `DELIVERED_PENDING_RELEASE` exige PoD válido para `COMPLETED` y release de escrow.

3. **Estado y refund mezclados** → corregido: máquina de refund separada acoplada a orden.

4. **SLA “de palabra”** → corregido: deadlines persistidos + timers + eventos de breach.

5. **Editar el pasado** → corregido: snapshots inmutables + eventos compensatorios.

---