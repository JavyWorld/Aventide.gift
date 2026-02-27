### Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado

**Fuente de verdad:** “Sistema de Reputación (Trust Engine) — Aventide Gift”.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema que calcula un **Buyer Trust Score** (0–100) y lo expone al seller como **Trust Level + Trust Badge** (semi-visible) para equilibrar **privacidad** (incl. “Admirador Secreto”) con **seguridad** operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.

**Objetivos:**

1. Reducir fraude/chargebacks, abuso de cancelaciones y disputas maliciosas sin matar conversión.

2. Ser resistente a abuso: anti-review bombing, anti-multicuentas y anti-extorsión en chat.

3. Ser explicable y auditable: score con subscores, historial diario y reason codes.

4. Integración consistente con Órdenes, Disputas, Moderación y Búsqueda: el score define **fricción inteligente** y límites (no mueve dinero directamente).

---

## 2) Alcance (incluye / excluye)

### Incluye

- **Buyer Trust Score interno 0–100** con pesos y ventanas (30/90/180) y agregación final (ver 5).

- **Trust Levels visibles al seller**: Alto/Medio/Bajo, con badge (“Comprador verificado / Trust alto”).

- **Buyer Reviews (reviews_buyer)** como insumo de integridad (no “rating público” del buyer).

- Acciones por nivel: límites de cancelación tardía, fricción adicional en alto valor, hold de reviews si riesgo, verificación adicional, suspensión por chargebacks.

- Señales de chat/abuso/extorsión y moderación de reviews.

### Excluye

- Seller Reputation (ya definido en Seller Only).

- Motor completo de Moderación (solo integración).

- Motor de Pagos/Refunds (solo señales y efectos de policy).

---

## 3) Actores y permisos (RBAC) + guards

### Actores

- **BUYER:** crea órdenes, puede reseñar; ve su estado básico (sin revelar score exacto si no se desea).

- **SELLER:** ve Trust Level + badge del buyer (incluyendo órdenes anónimas).

- **SYSTEM/BOT:** calcula score, aplica fricción y límites, genera eventos, mantiene historial.

- **TRUST & SAFETY / OPS:** revisa casos, aplica sanciones/bloqueos por fraude.

### Permisos mínimos

- `buyer.trust.read.own` (buyer; opcional mostrar “nivel” sin score exacto)

- `buyer.trust.read.for_seller` (seller; solo Trust Level + badge)

- `buyer.trust.policy.read/write` (admin/ops; scoped país/ciudad)

- `buyer.trust.penalties.enforce` (system/admin; auditado)

- `buyer.trust.audit.read` (audit/admin)

### Guards (runtime)

1. AuthGuard

2. ContextGuard (seller solo ve trust de buyer si hay relación de orden o pre-check de checkout)

3. ScopeGuard (ops/admin por país)

4. PolicyGuard (thresholds y fricción por país/ciudad)

5. AuditGuard (cambios de score/penalty/badge)

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Cálculo continuo por eventos (event-driven)

**Happy path**

1. Eventos relevantes actualizan `buyer_metrics_rollup` (ventanas 30/90/180) y luego recalculan score:

- `ORDER_COMPLETED`

- `ORDER_CANCELED`

- `DISPUTE_CLOSED`

- `MODERATION_ACTION`

- `CHAT_FLAGGED`

1. Se guarda snapshot diario `buyer_score_history` con subscores, score final, delta y drivers.

**Edge cases**

- Duplicados: idempotencia por `(buyer_id, event_id)` en rollups.

- “Eventos tardíos” (chargeback meses después): recalcula ventanas afectadas y emite `BUYER_TRUST_RECALCULATED` con audit trail.

### 4.2 Visibilidad al seller (semi-visible)

**Regla dura:** el seller ve solo:

- `TrustLevel: ALTO | MEDIO | BAJO`

- `TrustBadge` (ej. “Comprador Verificado”)

**En órdenes anónimas (Admirador Secreto):**

- no se revela identidad, pero el seller sigue viendo el Trust Badge/Level para tomar decisiones seguras.

### 4.3 Fricción inteligente según Trust Level

Trust Alto (80–100)

- fricción mínima.

Trust Medio (60–79)

- defensas suaves:

    - límites de cancelación tardía,

    - confirmaciones extra en fechas pico (high-demand).

Trust Bajo (<60)

- defensas fuertes al seller:

    - limitar órdenes de alto valor,

    - hold de publicación de reviews (anti-bombing),

    - verificación adicional (teléfono/2FA/ID si aplica),

    - si hay chargebacks: suspensión.

**Corrección de incoherencia:** estas acciones no se aplican “a mano”; se expresan como **policy flags** (limits/friction) consumidos por Órdenes/Checkout/Moderación, con auditoría.

### 4.4 Integridad de reviews (buyer)

**Happy path**

- Si se detecta:

    - spam/copy-paste masivo,

    - ráfagas anómalas de 1★,

    - violaciones moderación\
        ⇒ baja `review_integrity_score`, puede poner `review_hold` temporal y envía `CHAT_FLAGGED/MODERATION_ACTION` como señales.

---

## 5) Reglas y políticas (pesos, thresholds, validaciones)

### 5.1 Buyer Trust Score (0–100) — pesos oficiales

Pesos default:

- **Pago confiable (chargebacks, métodos verificados)** — 25%

- **Comportamiento de órdenes (cancelaciones tardías, retención de PIN)** — 25%

- **Disputas/reclamos (perdidas pesan más)** — 25%

- **Conducta en chat/abuso** — 15%

- **Integridad de reviews** — 10%

### 5.2 Trust Levels visibles al seller (thresholds)

- **ALTO:** 80–100

- **MEDIO:** 60–79

- **BAJO:** <60

### 5.3 Ventanas y score final (consistencia con Seller Score)

**Ventanas:** 30d / 90d / 180d\
**Agregación final:**\
`Final = 0.30*Score_30d + 0.60*Score_90d + 0.10*Score_180d`

### 5.4 Señales exactas por subscore (definiciones operables)

A) Payment Reliability (25%)

Inputs:

- `chargeback_rate` (90d y 180d, pesa más 90d)

- `verified_payment_methods_count`

- `payment_fingerprint_risk` (si existe)

Reglas:

- Cualquier chargeback reciente degrada fuerte; múltiples ⇒ Trust Bajo + suspensión.

B) Order Behavior (25%)

Inputs:

- `late_cancel_rate` (cancelación tardía)

- `pin_withheld_events` (retención/negativa del PIN sin causa)

Reglas:

- Cancelaciones tardías repetidas ⇒ límites + confirmaciones extra.

- Retener PIN sistemáticamente ⇒ penalización alta (riesgo extorsión/fraude).

C) Disputes/Complaints (25%)

Inputs:

- `disputes_lost_rate` (buyer-at-fault)

- `complaint_rate_validated` (si soporte valida mala fe)

Reglas:

- Las disputas perdidas pesan más que disputas abiertas; severidad pondera.

D) Chat Conduct (15%)

Inputs:

- `chat_abuse_rate`

- `extortion_flags`

Reglas:

- Abuso/exhortación ⇒ caída y posible suspensión.

E) Review Integrity (10%)

Inputs:

- `review_integrity_score`

- `review_bombing_flags`

- `copy_paste_detected`

Reglas:

- Review bombing ⇒ hold de publicación de reviews + degradación del trust.

### 5.5 Multi-país (policy engine)

Parámetros configurables por país/ciudad (sin hardcode):

- thresholds de Trust Level

- penalizaciones y fricción

- ventanas / half-life de penalizaciones

- definición de “alto valor” por país (monto/categoría)

- grace windows para cancelación tardía según logística

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 reviews_buyer

`reviews_buyer(id, order_id, buyer_id, seller_id, stars, tags[], text, status, flagged_reason, created_at)`\
Índices:

- unique(`order_id`,`seller_id`) (una review seller→buyer por orden si aplica bilateral)

- (`buyer_id`,`status`,`created_at desc`)

### 6.2 buyer_metrics_rollup

`buyer_metrics_rollup(buyer_id, window(30|90|180), chargeback_rate, late_cancel_rate, disputes_lost_rate, chat_abuse_rate, review_integrity_score, updated_at)`\
Índices:

- unique(`buyer_id`,`window`)

### 6.3 buyer_score_history

`buyer_score_history(buyer_id, date, score_final, subscores_json, delta, top_drivers_json, updated_at)`\
Índices:

- (`buyer_id`,`date desc`)

### 6.4 badge_assignments (Buyer)

`badge_assignments(entity_type=Buyer, entity_id=buyer_id, badge_code, status, granted_at, revoked_at)`

### 6.5 penalty_events (Buyer)

`penalty_events(entity_type=Buyer, entity_id, penalty_code, severity, reason_codes[], starts_at, ends_at, created_by(AUTO|ADMIN), audit_ref)`

---

## 7) Eventos y triggers + idempotencia

### Eventos mínimos (buyer trust)

- `ORDER_COMPLETED` → actualiza rollups

- `ORDER_CANCELED` → late_cancel_rate

- `DISPUTE_CLOSED` → disputes_lost_rate

- `MODERATION_ACTION` → review status / integrity

- `CHAT_FLAGGED` → chat_abuse/extorsión

Eventos derivados:

- `BUYER_TRUST_RECALCULATED`

- `BUYER_TRUST_LEVEL_CHANGED`

- `BUYER_FRICTION_POLICY_CHANGED`

- `BUYER_SUSPENDED/UNSUSPENDED`

### Idempotencia

- Rollups: `(buyer_id, window, event_id)`

- Snapshot diario: `(buyer_id, date)`

- Penalización: `(buyer_id, penalty_code, window_key)`

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Checkout / Órdenes

Consume:

- `buyer_trust_level`

- `friction_flags` (extra confirms, high-value limit)

Produce:

- eventos de cancelación tardía / PIN withheld, etc.

### Disputas

Consume:

- buyer trust como señal (prioridad, fricción)\
    Produce:

- outcomes/fault attribution alimentan métricas.

### Moderación

Consume:

- señales de review bombing / abuso\
    Produce:

- `MODERATION_ACTION` con removals/holds.

### Chat

Produce:

- `CHAT_FLAGGED` por abuso/extorsión.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `buyer_trust_score_avg{country}`

- `buyer_trust_level_distribution{country}`

- `buyer_chargeback_rate_avg{country}`

- `buyer_late_cancel_rate_avg{country}`

- `buyer_disputes_lost_rate_avg{country}`

- `buyer_chat_abuse_flags_total{country}`

- `buyer_review_integrity_holds_total{country}`

### Alertas

- Spike de chargebacks (fraude o provider issue)

- Spike de cancelaciones tardías (operación/logística rota)

- Spike de review bombing flags (ataque coordinado)

- Caída masiva de trust (bug de scoring)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Solo “verdad verificada” cuenta: `COMPLETED`, outcomes, chargebacks y eventos auditables.

- Trust Level visible pero no score exacto al seller; protege privacidad, especialmente en pedidos anónimos.

- Cambios de score/level/penalty quedan en auditoría con:

    - actor (AUTO/ADMIN),

    - before/after,

    - reason_codes,

    - evidencia (order/dispute/chat/mod_action).

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Órdenes:** señales de cancelación tardía y retención de PIN alimentan score; fricción se aplica en checkout.

- **Disputas:** outcomes alimentan disputes_lost y pueden disparar sanciones.

- **Moderación:** integridad de reviews y abuso.

- **Anonimato (Admirador Secreto):** seller ve Trust Badge/Level sin identificar buyer.

---

### Conflictos/incoherencias corregidas (dentro de Buyer Reputation/Trust)

1. **Trust público (exposición del buyer)** → corregido: semi-visible al seller como nivel+badge, no score público.

2. **Score sin base verificable** → corregido: solo eventos auditables (COMPLETED, disputes, cancelaciones, chat flags, moderation).

3. **Fricción aplicada “a mano”** → corregido: fricción deriva de policy flags consumidos por checkout/órdenes.

4. **Review bombing sin defensa** → corregido: integridad de reviews como subscore + holds/penalizaciones.

5. **Admirador Secreto sin señal de seguridad** → corregido: Trust Badge visible al seller aun en anonimato.