### Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado

**Fuente de verdad:** “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.\
**Objetivo del rewrite:** eliminar improvisación (“call center infinito”), separar correctamente **Incidencias vivas vs Disputas post-entrega**, prohibir montos manuales, hacer ejecución financiera **determinista + auditable**, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como **orquestador** de:

- Tickets (gestión operativa y comunicación),

- Casos de disputa (state machine formal),

- Evidencia (Audit Timeline + Tridente),

- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).

**Objetivos:**

1. Resolver **80%** con automatización + procesos (L0) y evitar escalamiento innecesario.

2. Separar claramente:

    - **Incidencias vivas** (durante entrega, intervención inmediata)

    - **Disputas post-entrega** (proceso formal con veredicto y ejecución monetaria).

3. “Regla de oro”: Soporte **no inventa montos**; selecciona un outcome y el sistema calcula.

4. Evidencia manda: PoD (PIN+GPS+Foto) y timeline auditado para resolver objetivamente.

5. Seguridad operativa: doble aprobación para reembolsos grandes/sensibles.

---

## 2) Alcance (incluye / excluye)

### Incluye

- Ticketing (Kanban/inbox), clasificación, SLAs, macros y automatización L0.

- Order Dashboard 360° (caja negra): timeline + tridente + señales de riesgo.

- Acciones operativas controladas (botones con guardrails): reenvío de PIN, extender timers, congelar fondos, solicitar reembolso (no ejecuta libre).

- Disputas: apertura, hold de fondos, recopilación de evidencia, veredicto por outcomes, ejecución financiera por saga, chargebacks.

- Integración con Trust & Safety: colusión/abuso/extorsión, moderación de reseñas conflictivas.

### Excluye

- Determinar la “verdad de entrega” fuera del sistema de Órdenes: Support OS **consume** la máquina de estados y evidencia, no la reemplaza.

- Calcular fees/impuestos desde cero: usa snapshot financiero locked de la orden.

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Niveles de soporte (capas)

- **L0 (Self-service/Bot):** flujos guiados, macros, resolución sin agente.

- **L1 (Agente estándar):** atiende tickets comunes, consulta evidencia, acciones limitadas.

- **L2 (Agente avanzado):** aplica decisiones de disputa **solo** eligiendo outcomes predefinidos.

- **L3 (Country Ops Lead):** intervención fuerte en incidentes críticos + Force Complete controlado.

- **Finance Reviewer:** doble aprobación para reembolsos grandes/sensibles.

- **Trust & Safety Specialist:** fraude/colusión/extorsión, reseñas conflictivas, medidas anti-abuso.

### 3.2 Permisos (namespaces sugeridos y obligatorios)

- `support.ticket.read/write` (L1+)

- `support.ticket.assign/escalate` (L1+ con límites)

- `support.order_dashboard.view` (L1+)

- `support.actions.resend_pin` (L1+)

- `support.actions.extend_timer` (L2/L3 o policy)

- `support.actions.freeze_funds` (L2/L3, con razón)

- `support.dispute.open` (L1/L2 según policy)

- `support.dispute.select_outcome` (L2+)

- `support.dispute.execute_saga` (system; L2 dispara “request execution”)

- `support.force_complete` (L3+; break-glass/policy)

- `support.finance.approve_large_refund` (Finance Reviewer)

- `support.tns.escalate` (L2+)

- `support.ugc.review_moderate` (T&S)

### 3.3 Guards (backend manda)

1. Auth

2. PermissionGuard

3. ScopeGuard (country_code obligatorio para operación)

4. PolicyGuard (ventanas, thresholds “large refund”, force-complete enabled, etc.)

5. EvidenceGuard (para acciones que dependan de PoD)

6. MoneyGuard (bloquea montos manuales; valida bucketización)

7. AuditGuard (razón obligatoria + WORM append-only)

---

## 4) Flujos end-to-end (happy path + edge cases)

### Flujo A — Incidencias vivas (durante entrega)

A1) Trigger & routing

Se activa por señales como: seller no llega, buyer no responde, dirección dudosa, riesgo de fallo del tridente, bloqueo operativo. Se enruta con alta prioridad a L3 (Country Ops Lead).

A2) Acciones operativas típicas

- Contacto seller / confirmar ETA / documentar en timeline.

- Autorizar reintento, reemplazo urgente o cancelación operativa (si hay dinero ya: se abre disputa/outcome).

A3) Force Complete / Override (excepción controlada)

Usar solo si falla automático (ej. GPS malo) pero hay evidencia fuerte (foto válida). Lo ejecuta L3 y queda auditado.

**Edge cases**

- Buyer extorsiona (“pago extra o disputa”): se revisa GPS/PIN/foto + patrón; escalar a T&S.

---

### Flujo B — Disputas post-entrega (núcleo financiero)

B1) Apertura + hold de fondos

Cuando buyer reclama no recibido/calidad/item incorrecto:

- Orden pasa a `DISPUTED` (en el dominio órdenes),

- fondos quedan bloqueados hasta resolución,

- se solicita evidencia a buyer y seller.

B2) Regla de oro (anti-improvisación)

El agente **elige outcome** (scenario_id + severity_band + affected_items\[\]). El sistema calcula montos desde snapshot + policies.

B3) Resolución expresada en buckets (siempre)

Nunca “% bonitos” ni “monto libre”; todo es bucket contable:

- `BuyerRefundCash`

- `BuyerCreditNonCash`

- `SellerPayoutRelease`

- `PlatformFee` (keep/waive parcial/total)

- `OpsFee` (keep/waive)

- `ExternalCosts` (processing/chargeback/dispute fees)

B4) Earned schedule del Platform Fee (devengado por hitos)

- `PAID_IN_ESCROW` → 0% earned

- `IN_PRODUCTION` → 50% earned

- `OUT_FOR_DELIVERY` → 80% earned

- `DELIVERED_VERIFIED` → 100% earned

Reglas por atribución de culpa (`fault_attribution`):

- `SELLER_FAULT/PLATFORM_FAULT` → normalmente se waivea incluso parte earned (policy)

- `BUYER_FAULT/FRAUD` con `DELIVERED_VERIFIED` → se permite keep completo o casi completo

- `FORCE_MAJEURE/UNKNOWN` → aplicar earned schedule neutral

B5) External Cost Shield

External costs pueden hacer net negativo; se modelan como bucket formal y se asignan según culpa con caps y policies.

**Edge cases**

- Chargeback externo: congelar, registrar fee, adjuntar paquete WORM, mapear a `ExternalCosts` + outcome.

---

## 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

### 5.1 Invariantes no negociables

- No editar números manuales.

- Cálculo determinístico desde snapshot financiero locked.

- Cada outcome produce buckets auditables + acciones automáticas (ledger/refund/release/credit/trust).

### 5.2 Doble aprobación (antifraude interno)

- “Reembolsos grandes o sensibles” requieren Finance Reviewer antes de ejecutar la saga. El umbral y criterios son policy-driven por país.

### 5.3 Force Complete (uso restringido)

- Solo L3, solo cuando el fallo fue técnico y hay evidencia fuerte; requiere razón obligatoria y marca especial en auditoría.

### 5.4 Catálogo de outcomes (biblioteca base MVP robusto)

El doc define una biblioteca inicial (A–F) que se implementa como catálogo versionado por país/policy, con inputs controlados y sin montos manuales.

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 Ticket (soporte general)

`support_tickets` (mínimo):

- `ticket_id`, `created_at`, `updated_at`

- `status` (NEW/TRIAGED/IN_PROGRESS/PENDING_USER/ESCALATED/RESOLVED/CLOSED)

- `priority` (P0–P3), `queue` (country_code + tipo)

- `requester_type` (BUYER/SELLER/INTERNAL), `requester_id`

- `order_id` (opcional pero común), `category`, `subcategory`, `reason_code`

- `assignee_level` (L0/L1/L2/L3), `assignee_user_id`

- `sla_first_response_at`, `sla_resolution_at`

- `internal_notes[]`, `public_messages[]`, `attachments[]`, `tags[]`

Índices:

- `(country_code, status, priority, created_at)`

- `(order_id)`

- `(assignee_user_id, status)`

### 6.2 Dispute Case (formal, separado del ticket)

`dispute_cases`:

- `dispute_case_id`, `ticket_id`, `order_id`

- `opened_by` (BUYER/SELLER/SYSTEM), `opened_at`

- `reason_code`

- `fault_attribution` (SELLER_FAULT/BUYER_FAULT/PLATFORM_FAULT/FORCE_MAJEURE/UNKNOWN)

- `evidence_status`

- `status` (state machine)

- `scenario_id`, `severity_band`, `affected_items[]`

- `selected_outcome_id`, `resolution_summary`, `resolved_at`

- `saga_state`, `idempotency_keys[]`

### 6.3 Catálogo de outcomes (configurable/versionado)

`dispute_outcomes_catalog`:

- `outcome_id`, `country_code`, `scenario_id`

- `inputs_schema` (allowed severity, allowed affected_items)

- `bucket_formula_ref` (referencia a fórmula/policy)

- `enabled`, `version`, `valid_from/to`

**Dependencia crítica (no duplicar):** `financial_snapshot_locked` de la orden se referencia por `order_id` y es el input determinista del cálculo.

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Eventos principales

- `support.ticket_created/updated/escalated/resolved`

- `support.dispute_opened`

- `support.dispute_evidence_requested/received`

- `support.dispute_outcome_selected`

- `support.dispute_finance_approval_requested/approved/denied`

- `support.dispute_saga_started/step_succeeded/step_failed/completed`

- `support.force_complete_executed`

- `support.chargeback_received`

### 7.2 Idempotencia

- `ticket_id` y `dispute_case_id` como identifiers.

- Saga: `idempotency_keys[]` por step; reintentos no duplican refunds/releases/credits.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### 8.1 Órdenes + Evidencia (Tridente)

Support OS consume:

- `order_events`/timeline (“Audit Timeline”)

- eventos `pin_attempt_failed`, `geo_mismatch`, `photo_uploaded`

- PoD: PIN+GPS+Foto y timestamps.

### 8.2 Ledger/Finanzas (ejecución por saga)

- Inputs: snapshot financiero locked.

- Outputs: buckets aplicados como movimientos contables y acciones (refund cash, credit non-cash, release payout, fee keep/waive).

### 8.3 Trust & Safety

- Escalamiento por colusión/abuso/extorsión.

- Señales internas: “usuario con 30% disputas”, “seller con reportes de calidad” y detector de colusión por IP/dispositivo/GPS patrón.

### 8.4 UGC Moderation

- Reviews conflictivas: panel para aprobar/rechazar; “blind review held” si extorsión/lenguaje ofensivo.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas operativas clave

- % tickets resueltos por L0 (objetivo alto)

- SLA first response p95 por cola/país

- SLA resolution p95 por categoría

- % disputas por outcome + win-rate por fault_attribution

- Lag de saga financiera (tiempo desde outcome_selected → saga_completed)

- Ratio de “force_complete” (debe ser bajo y auditado)

### Alertas

- Spike en disputes por seller/zona

- Spike en chargebacks por método de pago

- Uso inusual de force_complete

- Reembolsos grandes sin aprobación (debe ser 0)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

### Auditoría WORM (append-only)

Cada disputa genera paquete WORM:

- timeline de eventos,

- evidencias (referencias),

- veredicto/outcome,

- ejecución de saga (cada step),

- aprobaciones (finance).

### Controles antifraude interno

- “Four-eyes” para reembolsos grandes.

- Todo override registra reason_code obligatorio.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Órdenes:** soporte opera sobre la máquina de estados (DISPUTED) y no “edita estados” fuera de transiciones válidas; force_complete es excepción controlada.

- **Evidencia/Tridente:** pin/gps/foto como base objetiva para veredictos.

- **Ledger/Finanzas:** snapshot locked + buckets + saga idempotente (no montos manuales).

- **Jerarquía:** escalamiento por niveles y scope país (L1/L2/L3).

- **Analítica:** outcomes y tiempos alimentan KPIs (dispute rate, seller quality, fraud).

---

### Conflictos/incoherencias corregidas (dentro de Soporte)

1. **Soporte como “call center infinito”** → corregido: 2 dominios (incidente vivo vs disputa) + L0 fuerte.

2. **Montos manuales por agentes** → prohibido: outcomes + buckets + snapshot + cálculo determinístico.

3. **Overrides sin control** → force_complete solo L3, con evidencia y auditoría; reembolsos grandes con doble aprobación.

4. **Decisión sin evidencia** → caja negra + tridente + señales de riesgo como base objetiva.

5. **Ejecución financiera frágil** → saga + idempotencia + WORM (audit legal).