### Sistema de Analítica v2.0 (corregido y unificado)

**Fuente de verdad:** Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.\
**Objetivo del rewrite:** convertir la analítica en un sistema **audit-able, multi-país, RBAC+scoping estricto, SSOT**, con separación clara entre **Analítica vs Observabilidad**, y sin conflictos con el **motor financiero/ledger**, **Jerarquía**, **Usuarios**, **App Camaleón/Policy Engine**.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema de Analítica es el “HUB central” que captura, consolida y expone métricas de negocio y operación del marketplace, derivadas de:

- **Eventos críticos server-side** (inmutables, append-only).

- **Estados finales de órdenes y snapshots financieros** (para evitar descuadres ante cambios futuros de fees/reglas).

- **Modelos analíticos (facts/dims) y rollups** para BI y operación near-real-time.

**Objetivos:**

1. **SSOT:** dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).

2. **Multi-país nativo:** toda métrica cortable por country/hub/zone, currency, timezone local, y normalización a moneda base (USD).

3. **RBAC + scoping al nivel de consulta:** Seller solo lo suyo; Ops Lead su país/hubs; Admin global. No solo UI.

4. **Real-time operativo / eventual para BI profundo:** operación “hoy/última hora” near-real-time; cohortes/finanzas pesadas con jobs.

5. **Analítica ≠ Observabilidad:** analítica = salud negocio/crecimiento/fraude/costos; observabilidad = salud técnica; se correlacionan por trace_id/request_id.

6. **Gobernanza métrica:** definiciones “de hierro”, versionadas, conciliables con ledger/snapshots.

---

## 2) Alcance (incluye / excluye)

### Incluye

- Backbone de eventos analíticos `analytics_events_raw` (append-only) con idempotencia.

- Modelo analítico: **dimensions + facts** (fact_orders, fact_payments, fact_payouts, fact_disputes, fact_promos, fact_loyalty, etc.).

- Rollups (agregados) diarios/horarios por país/seller/zona/funnel/cohort.

- Anomaly Engine (operativo + fraude/abuso) con baselines y acciones integradas.

- Dashboards por rol: Admin Global, Country Ops Lead, Seller, Soporte/Moderación/Auditoría.

- Data Governance: catálogo de métricas, quality gates, retención, privacidad.

### Excluye

- Observabilidad técnica completa (logs, traces, health checks) como sistema primario: solo enlace/correlación.

- Auditoría legal WORM como repositorio de evidencia: analítica referencia `case_id`/`audit_ref`, pero no sustituye evidencia.

---

## 3) Actores y permisos (RBAC) + guards (aplicado a Analítica)

### 3.1 Actores

- **SUPER_ADMIN / Admin Global:** visión multi-país, comparativos, cambios globales, gobernanza de métricas.

- **COUNTRY_OPS_LEAD (Regional OS):** operación + crecimiento de su país/hub/zone.

- **SELLER:** performance, conversiones, catálogo, cumplimiento, dinero (solo su data).

- **SUPPORT / MODERATION / AUDIT:** timelines, evidencia referenciada, calidad, fraude.

- **SYSTEM/BOT:** inserción de eventos y jobs.

### 3.2 Scoping estricto (regla dura)

- Todo endpoint/query analítico exige `scope_context` (country/hub/zone/seller_id) resuelto por claims.

- Enforcement **a nivel query** (RLS/filters server-side). La UI solo refleja.

**Permisos sugeridos por namespace (mínimos):**

- `analytics.read.global` (Admin)

- `analytics.read.country` (Ops Lead scoped)

- `analytics.read.seller` (Seller)

- `analytics.events.ingest` (System)

- `analytics.metrics.manage` (Admin, catálogo KPI)

- `analytics.anomaly.manage` (Ops/Risk/Admin, según policy)

### 3.3 Guards canónicos (backend)

1. Auth

2. PermissionGuard (`analytics.read.*`)

3. ScopeGuard (country/hub/zone/seller)

4. PolicyGuard (si el país habilita módulos/experimentos/cortes)

5. DataPrivacyGuard (bloquea PII y aplica anonimización)

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Ingesta de eventos (server-side primero)

**Happy path**

1. Ocurre transición confirmada (ej. PAYMENT_SUCCEEDED).

2. Backend emite evento analítico inmutable con `event_id` y `trace_id/request_id`.

3. Se guarda en `analytics_events_raw` (append-only).

4. Jobs/materialización actualizan facts/rollups.

**Edge cases**

- Reintento de evento: dedupe por `event_id` (idempotencia).

- Evento llega sin `country/hub/zone`: **rechazado** o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).

- Eventos client-side (HOME_VIEW, clicks): permitidos, pero **no** fuente final de revenue/GMV (SSOT).

### 4.2 Construcción de Facts (conciliables)

- `fact_orders`: 1 fila por orden, con timestamps clave y snapshot financiero “locked”.

- `fact_payments`: intentos, success rate, error_codes, proveedor.

- `fact_payouts`: payouts, fallos, latencias.

- `fact_disputes`: casos, outcomes, montos, tiempos.

**Edge cases críticos (finanzas)**

- Refund/cancel: ORDER_CANCELLED + REFUND_ISSUED deben ajustar KPIs según reglas del KPI (ej. GMV reconocido en COMPLETED vs creado).

- Cambios futuros de fee rules: **no cambian** el pasado; se usa snapshot en la orden (evita descuadres).

### 4.3 Rollups para operación y BI

- `rollup_hourly_ops`: salud operativa (pagos, cancelaciones, SLA)

- `rollup_daily_kpis`: GMV, orders, conversion, AOV, dispute rate, etc.

- `build_weekly_cohorts`: cohortes de compradores y sellers.

- `anomaly_detection_job`: anomalías + acciones.

---

## 5) Reglas y políticas (límites, validaciones, consistencia)

### 5.1 SSOT “de hierro”

- Revenue/GMV/ventas se calculan desde **fact_orders + snapshots financieros** y eventos server-side críticos.

- Eventos de UI se usan para funnel/UX, no para contabilidad del negocio.

### 5.2 Multi-país obligatorio por evento

Cada evento y fila de facts/rollups debe incluir:

- `country_code`, `hub_id`, `zone_id`

- `currency`, `amount_usd`, `fx_rate`

- `ts_local`, `timezone` y `ts_utc`

### 5.3 Compatibilidad con el sistema de fees / descuentos (conflicto evitado)

- Loyalty → **Fee Credits** solo descuentan **Platform Fee**, nunca afectan al Seller y no tocan fees “non-discountable” (pasarela / Ops Lead / etc.).

- Cupones del seller → costo atribuible al seller (se mide como costo/estrategia del seller).

### 5.4 RBAC + scoping a nivel de consulta

- No se permite exportar o consultar data sin filtros de scope.

### 5.5 Analítica vs Auditoría (regla dura)

- Analítica guarda métricas, agregados y timelines de negocio.

- Evidencia legal/forense vive en Auditoría; analítica solo enlaza referencias (case_id).

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 Capa A — Eventos Raw

**Tabla:** `analytics_events_raw`\
Campos (mínimo obligatorio):

- `event_id` (UUID, unique) — idempotencia

- `event_name`

- `ts_utc`, `ts_local`, `timezone`

- `actor_role`, `actor_user_id`

- `country_code`, `hub_id`, `zone_id`

- `session_id`, `device_id`, `app_version`, `channel`

- `order_id`, `seller_id`, `product_id`, `category_id` (nullable)

- `money` JSON `{amount, currency, amount_usd, fx_rate}`

- `policy_context` JSON `{policy_version, ui_config_version, fee_rule_id}`

- `props` JSONB extendido

- `trace_id`, `request_id`

**Índices recomendados:**

- unique(`event_id`)

- (`event_name`, `ts_utc`)

- (`country_code`, `hub_id`, `zone_id`, `ts_utc`)

- (`seller_id`, `ts_utc`)

- (`order_id`)

### 6.2 Capa B — Dimensions

- `dim_country`, `dim_hub`, `dim_zone`

- `dim_user` (sin PII)

- `dim_seller`, `dim_category`, `dim_product`

- `dim_policy_version` (comparar cambios multi-país / Camaleón)

- `dim_marketing_channel`

### 6.3 Capa B — Facts (conciliables)

- `fact_orders` (1 fila por orden; estados + timestamps; snapshot financiero locked)

- `fact_payments` (intentos, éxito, error codes)

- `fact_payouts`, `fact_disputes`, `fact_promos`, `fact_loyalty`, `fact_moderation`, `fact_search`

### 6.4 Capa C — Rollups

- `agg_kpi_daily_country`

- `agg_kpi_daily_seller`

- `agg_funnel_daily_country`

- `agg_cohorts_weekly_country`

- `agg_quality_daily`

- `agg_finance_daily`

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Taxonomía mínima obligatoria (por sistema)

**Core marketplace** (mínimo):\
USER_SIGNUP, USER_LOGIN, HOME_VIEW, CATEGORY_VIEW, PRODUCT_VIEW, SEARCH_PERFORMED, ADD_TO_CART, CHECKOUT_STARTED, PAYMENT_ATTEMPTED, PAYMENT_SUCCEEDED, PAYMENT_FAILED, ORDER_CREATED, ORDER_ACCEPTED, ORDER_PREPARING, ORDER_OUT_FOR_DELIVERY, ORDER_DELIVERED, PIN_VERIFIED, ORDER_COMPLETED, ORDER_CANCELLED, REFUND_ISSUED

**Soporte/Disputas/Auditoría:**\
TICKET_CREATED, TICKET_RESOLVED, DISPUTE_OPENED, DISPUTE_OUTCOME_SELECTED, DISPUTE_CLOSED, PAYOUT_RELEASED, PAYOUT_FAILED, ADMIN_ACTION_RECORDED

**Moderación/Riesgo:**\
USER_REPORTED, PRODUCT_REVIEWED, CONTENT_TAKEDOWN, ACCOUNT_SUSPENDED, FRAUD_FLAGGED, TRUST_SCORE_UPDATED

**Promos & Loyalty:**\
LOYALTY_POINTS_EARNED (solo en ORDER_COMPLETED), LOYALTY_POINTS_REVOKED, LOYALTY_POINTS_REDEEMED_TO_FEE_CREDIT, FEE_CREDIT_APPLIED (max_applied = platform_fee_amount), FEE_CREDIT_EXPIRED

**Cupones seller-driven:**\
SELLER_COUPON_CREATED/UPDATED/EXPIRED, SELLER_COUPON_APPLIED/REJECTED, SELLER_COUPON_COST_BOOKED

**Referidos:**\
REFERRAL_INVITE_SENT, REFERRAL_LINK_CLICKED, REFERRAL_SIGNUP_ATTRIBUTED, REFERRAL_FIRST_ORDER_COMPLETED, REFERRAL_REWARD_GRANTED/REVOKED

### 7.2 Idempotencia (regla dura)

- Unicidad por `event_id` (UUID) en raw.

- En facts: dedupe por (`order_id`, `state_transition`) o por `event_id` que materializa el cambio.

- En rollups: recomputables (jobs deterministas) + watermark por ventana (hour/day).

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### 8.1 Motor financiero / órdenes

- Input: `locked_financial_meta` en orden (snapshot de reglas/fees/taxes) → se copia a `fact_orders` y `agg_finance_daily` para consistencia histórica.

### 8.2 App Camaleón / Policy Engine

- Cada evento guarda `policy_version` y `ui_config_version` para medir impacto de cambios (experimentos/config).

### 8.3 Observabilidad

- `trace_id/request_id` en eventos permite correlación: caída técnica ↔ caída conversión/GMV.

### 8.4 Auditoría / Casos

- Analítica referencia `case_id` y metadatos mínimos; evidencia vive fuera.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Analítica

**Nota:** aquí es “observabilidad del sistema de analítica” (pipeline), no la observabilidad global del producto.

### Logs

- ingest: `event_id`, `event_name`, `country_code`, `result`, `error_code`, `trace_id`, latencia

- jobs: `job_name`, ventana, filas procesadas, watermark, errores, retries

### Métricas

- `analytics_ingest_events_total{event_name,country}`

- `analytics_ingest_failed_total{reason}`

- `analytics_event_lag_seconds` (ts_utc → disponible en rollup)

- `analytics_job_runtime_seconds{job}`

- `analytics_rollup_rowcount{table,window}`

### Alertas

- Lag > umbral en operación (near-real-time roto).

- Caída brusca en ingest de eventos críticos (PAYMENT_SUCCEEDED / ORDER_COMPLETED).

- Divergencia de conciliación (GMV facts vs snapshot esperado).

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

### 10.1 Privacidad (regla dura)

- `dim_user` sin PII; PII vive fuera del lago analítico.

- Eventos pueden incluir hashes (ej. coupon_code_hash), no valores sensibles.

### 10.2 RBAC/RLS

- Vistas/queries aplican filtros por `seller_id` y/o `country_code/hub/zone`.

- Exportaciones: registradas (audit) con `who/what/when/scope`.

### 10.3 Retención

- raw: retención corta/media (90–180d) y luego compactación o borrado.

- facts/rollups: retención larga (años) para histórico del negocio.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Jerarquía:** scoping por país/hub/zona y enforcement en backend, no UI.

- **Usuarios:** actor_role/actor_user_id, sesiones, device/app_version, sin PII en analítica.

- **Motor financiero / Ledger:** snapshots locked para evitar descuadres retroactivos; KPIs conciliables.

- **App Camaleón:** cortes por `policy_version` y `ui_config_version`.

- **Soporte/Moderación/Auditoría:** eventos + facts para KPIs; evidencia referenciada por case_id.

---

### Conflictos/incoherencias corregidas (dentro de Analítica)

1. **Métricas “financieras” desde UI events** → corregido: SSOT = server-side + estado final + snapshot financiero.

2. **Multi-país incompleto en eventos** → corregido: country/hub/zone/currency/timezone obligatorios o el evento no entra al SSOT.

3. **RBAC solo por UI** → corregido: scoping al nivel de consulta (RLS/filters) obligatorio.

4. **Confusión Analítica vs Observabilidad** → corregido: separación conceptual + correlación por trace_id/request_id.

5. **Descuentos/loyalty afectando seller** → corregido: fee credits solo platform fee; cupones del seller se imputan como costo del seller.

---