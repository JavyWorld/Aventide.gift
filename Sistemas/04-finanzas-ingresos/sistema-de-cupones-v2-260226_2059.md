### Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado

**Fuentes de verdad:**

- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos → 10.2 Cupones del Seller”

- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”

- “Sistema de Pagos — Torre de Precios (orden de cálculo)”

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema que permite a un **seller** crear y administrar cupones (seller-funded) para que buyers los apliquen en checkout, cumpliendo reglas de elegibilidad, targeting territorial y límites de uso. El descuento **reduce el ingreso del seller** (nunca lo absorbe la plataforma).

**Objetivos:**

1. Coherencia financiera: el cupón **reduce el subtotal base del seller** y sobre ese neto se calculan fees posteriores.

2. No romper invariantes: no afecta taxes/processing/ops fee/FS; solo afecta la porción “items” del seller (o delivery si el tipo es free delivery y el delivery es seller-funded).

3. Anti-abuso operativo: rate limit y señales obligatorias para first-time buyer-only.

4. Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por `checkout_id` en la aplicación.

---

## 2) Alcance (incluye / excluye)

### Incluye

- **CRUD de cupones** por seller (vía Seller Console) con condiciones robustas.

- **Validación y aplicación en checkout** con orden correcto (“Torre de Precios”).

- **Cálculo de** `seller_coupon_discount` respetando `max_discount_amount` en cupones % y demás constraints.

- **Targeting** por `country/hub/zone` y por `delivery_mode` (ASAP/Programado).

- **Stacking policy** (por defecto NO apilable).

- **Anti-abuso mínimo** + señal a Trust/Moderation ante patrones.

### Excluye

- FS/Fee Credits (Lealtad): es otro sistema; cupones no se mezclan con FS salvo en el orden de cálculo.

- Cupones financiados por plataforma (si existen en el futuro): este sistema es explícitamente **seller-funded**.

---

## 3) Actores y permisos (RBAC) + guards

### Actores

- **SELLER:** crea/edita/pausa cupones, ve métricas básicas.

- **BUYER:** aplica cupón en checkout.

- **OPS LEAD / ADMIN:** auditoría y enforcement (p.ej. suspender coupon por abuso) con scope. (El rol ops/admin ya es estándar del proyecto).

- **SYSTEM/BOT:** valida, calcula descuento, emite eventos, snapshottea la orden.

### Permisos mínimos

- `coupons.seller.create`

- `coupons.seller.update`

- `coupons.seller.pause`

- `coupons.seller.read`

- `coupons.apply` (buyer)

- `coupons.admin.enforce` (ops/admin; scoped)

### Guards

1. AuthGuard

2. Role/PermissionGuard

3. OwnershipGuard (seller_id) en endpoints seller

4. ScopeGuard (country/hub/zone) para enforcement ops

5. PolicyGuard (reglas del país/territorio)

6. RateLimitGuard (apply attempts)

7. AuditGuard (cambios y acciones de enforcement)

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Creación de cupón (Seller Console)

**Happy path**

1. Seller crea cupón con `type`, `value`, ventana `valid_from/to`, límites de uso, targeting, productos/categorías, stacking, delivery modes.

2. Backend guarda `code_hash` (no el código plano) y estado `ACTIVE`.

**Edge cases**

- `valid_to < valid_from` → reject.

- targeting vacío → por default restringir al territorio operativo del seller (Suposición: consistente con targeting country/hub/zone y con governance multi-país; si se desea global, debe ser explícito en policy).

### 4.2 Aplicación en checkout (Buyer)

**Happy path**

1. Buyer ingresa código en checkout.

2. Backend valida elegibilidad:

    - ventana de validez,

    - límites de uso total y por buyer,

    - `min_order_subtotal`,

    - elegibilidad por productos/categorías,

    - `first_time_buyer_only`,

    - delivery_mode permitido,

    - targeting country/hub/zone,

    - stacking_policy.

3. Backend calcula `seller_coupon_discount` (si % respeta `max_discount_amount`).

4. Recalcula breakdown siguiendo el **orden oficial** (ver 5).

5. Persiste el estado del checkout **idempotente** y emite evento analítico `SELLER_COUPON_APPLIED`.

**Edge cases**

- Código inválido/expirado → respuesta con `reject_reason` estandarizado (ver 5.8).

- Cupón excedió `usage_limit_total` en carrera (race) → se resuelve con contador atómico/locking; si pierde, `reject_reason=LIMIT_REACHED`.

- Reintento/redoble click → no “consume” dos veces: idempotencia por `checkout_id`.

### 4.3 Consumo definitivo (al pagar)

**Happy path**

1. En `ORDER_CREATED→PAID_IN_ESCROW`, el sistema **snapshottea**:

    - `coupon_id`, `discount_amount`, `coupon_policy_version` en `order_promo_snapshot`.

2. Se marca `coupon_redemption` como `CONSUMED`.

**Edge cases**

- Pago falla o reservation expira: no se consume definitivamente; se libera hold y no cuenta como redención final (Suposición: consistente con patrón de reservas TTL del proyecto).

### 4.4 Refund/Disputa

- El cupón ya aplicado no “se devuelve” como crédito: era descuento seller-funded y ya afectó el net del seller en el snapshot de la orden.

- La reversión financiera ocurre vía Disputas/Refunds según buckets; el cupón permanece como dato histórico del snapshot.

---

## 5) Reglas y políticas (límites, validaciones, caps)

### 5.1 Principio duro (invariante)

**Cupón del seller = seller-funded.** El descuento baja el net del seller; la plataforma no absorbe el costo.

### 5.2 Tipos de cupón (soportados)

- `% OFF`

- `$ OFF`

- `Free delivery` **solo si** el delivery fee en el modelo es seller-funded

- (Opcional pro) `Bundle/BOGO`

### 5.3 Atributos soportados (robusto)

- `valid_from`, `valid_to`

- `usage_limit_total`, `usage_limit_per_buyer`

- `min_order_subtotal`

- `max_discount_amount` (para %)

- `eligible_products`, `eligible_categories`

- `first_time_buyer_only`

- `allowed_delivery_modes` (ASAP/Programado)

- `stacking_policy` (default **NO apilable**)

- `country/hub/zone targeting`

### 5.4 Orden correcto en checkout (“Torre de Precios”)

Orden obligatorio:

1. `items_subtotal`

2. `cupón seller-funded → reduce items`

3. `delivery`

4. `taxes`

5. `ops lead fee (no-discountable)`

6. `processing fee (no-discountable)`

7. `platform fee`

8. `membership benefits (si aplica)`

9. `Fee Shields (solo contra platform fee)`

### 5.5 Stacking policy (anti-incoherencias)

- Default: **NO apilable**.

- Si se habilita apilado por policy, debe existir regla determinística: `ONLY_ONE_SELLER_COUPON` + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.

### 5.6 Reglas de “first_time_buyer_only”

- Requiere señales mínimas: teléfono verificado + consistencia.

- Si no cumple, `reject_reason=FTB_NOT_ELIGIBLE`.

### 5.7 Anti-abuso mínimo (obligatorio)

- Rate limit a intentos de aplicar cupones.

- Detección de patrones (muchas redenciones con cuentas nuevas) → señal a Trust/Moderation.

### 5.8 Rechazos estandarizados (contracto)

`reject_reason` (enum):

- `CODE_INVALID`

- `EXPIRED`

- `NOT_STARTED`

- `LIMIT_REACHED_TOTAL`

- `LIMIT_REACHED_PER_BUYER`

- `MIN_SUBTOTAL_NOT_MET`

- `NOT_ELIGIBLE_PRODUCT_CATEGORY`

- `DELIVERY_MODE_NOT_ALLOWED`

- `TERRITORY_NOT_ALLOWED`

- `STACKING_NOT_ALLOWED`

- `FTB_NOT_ELIGIBLE`

- `COUPON_INACTIVE`

(Suposición: los motivos exactos no están enumerados en la documentación; este set es consistente con las condiciones soportadas.)

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 seller_coupons (definición)

Campos mínimos (explícitos en docs):

- `coupon_id`

- `seller_id`

- `code_hash`

- `type`

- `value`

- `valid_from`, `valid_to`

- `usage_limit_total`, `usage_limit_per_buyer`

- `min_order_subtotal`

- `max_discount_amount`

- `eligible_products`, `eligible_categories`

- `first_time_buyer_only`

- `allowed_delivery_modes`

- `stacking_policy`

- `target_country`, `target_hub`, `target_zone`

- `status` (DRAFT|ACTIVE|PAUSED|DISABLED)

Índices recomendados:

- unique(`seller_id`, `code_hash`)

- (`seller_id`, `status`, `valid_from`, `valid_to`)

- (`target_country`, `target_hub`, `target_zone`, `status`)

### 6.2 coupon_redemptions (consumo y límites)

- `redemption_id`

- `coupon_id`

- `buyer_id`

- `checkout_id`

- `order_id` (nullable hasta pago)

- `status` (HELD|CONSUMED|RELEASED|EXPIRED)

- `discount_amount_snapshot`

- `created_at`, `consumed_at`

Índices:

- unique(`checkout_id`, `coupon_id`) para idempotencia

- (`coupon_id`, `status`)

- (`coupon_id`, `buyer_id`) para `usage_limit_per_buyer`

### 6.3 order_promo_snapshot (por orden)

Debe incluir mínimo: `coupon_id`, `discount_amount`, `coupon_policy_version` (además de membership/loyalty/campaign).

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Eventos (mínimos)

- `SELLER_COUPON_APPLIED` (analítico)

- `SELLER_COUPON_REJECTED` (con `reject_reason`)

- `SELLER_COUPON_REMOVED` (cuando buyer lo quita)

- `SELLER_COUPON_CONSUMED` (al pago)

- `SELLER_COUPON_RELEASED` (pago fallido/cancelación/hold expirado)

### 7.2 Idempotencia

- Aplicar cupón debe ser idempotente por `checkout_id`.

- Consumo definitivo debe ser idempotente por `order_id` (si llega doble confirmación de pago).

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Checkout / Motor financiero

- Input: cart snapshot + delivery_intent + contexto territorial.

- Output: `seller_coupon_discount` y breakdown recalculado con orden oficial.

### Lealtad (FS)

- Solo interacción por el orden de cálculo: cupón primero (reduce items), FS al final (solo platform fee).

### Analytics

- Emisión `SELLER_COUPON_APPLIED` + snapshot por orden para atribución y costo.

### Trust/Moderation

- Señales de abuso por patrón de redención → ticket/señal a Trust/Moderation.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `coupon_apply_attempts_total{country}`

- `coupon_apply_success_total{country}`

- `coupon_apply_rejected_total{reason,country}`

- `coupon_redemptions_consumed_total{coupon_id}`

- `coupon_limit_conflicts_total{coupon_id}` (colisiones en contador)

- `coupon_abuse_signals_total{country}`

### Alertas

- Spike `coupon_apply_rejected_total{reason=CODE_INVALID}` (fraude o campañas de fuerza bruta)

- Spike `coupon_abuse_signals_total`

- Conflictos altos en consumo (posible bug de locking/idempotencia)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- `code_hash` en storage; no guardar código en texto plano. (Suposición: consistente con prácticas del proyecto y con seguridad anti-abuso.)

- Audit log para:

    - create/update/pause/disable coupon (seller/admin),

    - enforcement ops,

    - apply/remove/consume/release (system; con `checkout_id/order_id`).

- Rate limit obligatorio en apply.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Pagos / Torre de Precios:** cupón reduce net del seller y se aplica antes de fees; FS al final solo contra platform fee.

- **Lealtad:** EOV usa `seller_coupon_discount` para cálculo de puntos; por eso el descuento debe quedar snapshotteado.

- **Analítica:** `order_promo_snapshot` obligatorio por orden.

- **Trust/Moderation:** señales de abuso desde redenciones.

---

### Conflictos/incoherencias corregidas (dentro de Cupones)

1. **“¿Quién paga el cupón?”** → definido duro: siempre seller-funded; baja net del seller.

2. **Orden de cálculo inconsistente (rompe docs/ledger/BI)** → fijado por Torre de Precios.

3. **% OFF sin cap** → obligatorio `max_discount_amount` y respeto en backend.

4. **Aplicación duplicada por reintentos** → idempotencia por `checkout_id` + consumo por `order_id`.

5. **Abuso de cupones** → rate limit + señales first-time buyer + escalación a Trust/Moderation.