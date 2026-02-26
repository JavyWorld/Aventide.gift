### Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado

**Fuente de verdad:** “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema que valida si una entrega es **físicamente viable** antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: `country_id + hub_id + zone_id?`.

**Objetivos:**

1. Evitar órdenes imposibles: **sin cobertura no hay calendario, no hay checkout y no hay pago**.

2. Multi-modal sin romper modelo: soportar hoy `HYPER_LOCAL` (radio) y mañana `WORLDWIDE_SHIPPING` (courier) con reglas separadas.

3. Consistencia total con Búsqueda/Catálogo: lo “comprable” debe ser exactamente lo que Coverage Guard aprobaría.

4. Proveer evidencia operacional: snapshot logístico por orden (distancia, geocode meta, resultado cobertura).

---

## 2) Alcance (incluye / excluye)

### Incluye

- Jerarquía territorial operativa: `Country → Hub (Ciudad) → Zone (opcional)` con resolución obligatoria por dirección/orden.

- Address Intelligence: normalización + geocoding **obligatorio** y scoring de calidad.

- Cobertura seller hiper-local por radio y opcional por “rings” (anillos) con reglas/costos/horarios.

- Coverage Guard (middleware) ejecutado antes de scheduler/capacidad.

- Integración con Búsqueda (ST_DWithin) y Ordenes (snapshot logístico).

- Modo futuro `WORLDWIDE_SHIPPING` (deshabilitado por defecto).

### Excluye

- Scheduler de slots/capacidad (solo dependencia; Coverage decide si llega o no).

- Cálculo financiero total (solo entrega `delivery_fee_calculated` y metadata logística).

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Actores

- **BUYER:** crea/edita direcciones, elige “Entregar en…”, consulta cobertura implícita.

- **SELLER:** configura cobertura (radio/rings), horarios, cutoffs, blackout dates.

- **COUNTRY_OPS_LEAD:** administra hubs/zones (activación, saturación, kill switch).

- **SUPPORT:** ve evidencia de geocode, distancia, historial de cambios de dirección; audita overrides (si existen).

- **SYSTEM/BOT:** geocoding, cálculo distancia, check cobertura, snapshot, cache invalidation, jobs de re-geocoding.

### 3.2 Permisos mínimos

- `addresses.validate` (buyer)

- `addresses.create/update/delete` (buyer; ownership)

- `coverage.check` (system/buyer en checkout)

- `seller.coverage.update` (seller; ownership)

- `geo.admin.manage_hubs_zones` (ops lead; scoped)

- `coverage.audit.read` (support/ops)

- `coverage.override` (si se habilita; ver 5.9)

### 3.3 Guards (Coverage Guard)

1. AuthGuard

2. OwnershipGuard (address_id para buyer / seller_id para seller)

3. TerritoryGuard (resolve `country/hub/zone` y valida que el hub esté activo)

4. AddressGuard: **sin lat/long validado → FAIL**

5. FulfillmentGuard: ruta por `fulfillment_type` (HYPER_LOCAL vs WORLDWIDE)

6. AuditGuard: registra `coverage_check_run` con versión algoritmo y resultado.

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Address Intelligence (validate → save)

**Happy path**

1. Buyer usa `POST /addresses/validate` con `raw_address`.

2. Sistema llama proveedor (Google Places/Mapbox) y devuelve:

- `normalized_address`

- `location (lat/long)`

- `country_code`

- `address_quality_score`

- `geocode_provider_meta (place_id, confidence)`

1. Buyer confirma y guarda con `POST /addresses`.\
    **Regla dura:** no se guarda sin lat/long validado.

**Edge cases**

- `address_quality_score` bajo: permitir guardar pero marcar `needs_review=true` (para antifraude/soporte), y exigir confirmación extra (Suposición: consistente con “score opcional para antifraude y soporte”).

- Cambio de dirección durante checkout: fuerza re-evaluación cobertura + re-cotización delivery_fee.

### 4.2 Coverage Guard — HYPER_LOCAL (default actual)

**Happy path**

1. `GET /coverage/check?seller_id&address_id&date_time`

2. Valida address con lat/long.

3. Calcula distancia `distance_meters` (Haversine; o ruta si se integra).

4. Evalúa:

- si `distance <= seller.coverage_radius` → PASS

- si no → FAIL con `coverage_reason=OUT_OF_RADIUS`

1. Si PASS y seller usa rings:

- determina `ring_id` por distancia

- calcula `delivery_fee_calculated`

- aplica reglas temporales (`available_days`, `cutoff_time`, `blackout_dates`) para entregar a Scheduler (no decide slots; solo habilita/inhabilita).

**Edge cases**

- Seller sin `location` o `coverage_radius`: FAIL `SELLER_NOT_CONFIGURED`.

- Dirección sin lat/long: FAIL `ADDRESS_NOT_GEO_CODED` (regla dura).

- Distancia cercana al límite (99–101%): registrar para auditoría “near_limit”.

### 4.3 Coverage Guard — WORLDWIDE_SHIPPING (futuro)

**Happy path**

1. No evalúa radio.

2. Valida `destination_country ∈ seller.shipping_countries`.

3. Devuelve PASS/FAIL + ETA estimado (3–5 días hábiles) y exige tracking/POD por webhook (sin PIN).

---

## 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

### 5.1 Regla dura #1: Dirección sin coordenadas = no compra

- `lat/long` validado es requisito.

### 5.2 Regla dura #2: Coverage Guard corre antes de slots/capacidad

- No se consulta calendario si Coverage falla.

### 5.3 Regla dura #3: Search y Coverage usan el mismo motor

- Search filtra por `ST_DWithin` y Coverage valida con el mismo radio/datos (evita “te muestro algo comprable pero luego te bloqueo”).

### 5.4 Contexto territorial canónico

Toda dirección/orden se resuelve a:

- `country_id + hub_id + zone_id?`\
    Esto se usa para:

- filtrar catálogo/búsqueda,

- validar cobertura,

- calcular costos,

- aplicar horarios/cutoffs por región.

### 5.5 fulfillment_type define el “motor” de reglas

- `HYPER_LOCAL` por radio + scheduler + PIN + geo-cerca.

- `WORLDWIDE_SHIPPING` por países permitidos + tracking/POD.

### 5.6 Cobertura por rings (tiered) — recomendada

Rings:

- Ring1: 0–3km

- Ring2: 3–10km

- Ring3: 10–Xkm\
    Cada ring puede definir:

- `delivery_fee`

- `available_days`

- `cutoff_time`

- `max_orders_per_day` (si se acopla a capacidad)

### 5.7 Reglas temporales del seller (cuándo)

- `delivery_days`

- `delivery_windows`

- `same_day_enabled` + `cutoff_time`

- `blackout_dates`

- `zone_or_ring_specific_rules`

### 5.8 Costo de envío por distancia

- Se calcula en checkout y se suma al total (`delivery_fee_calculated`).

### 5.9 Overrides manuales (si existen)

El documento menciona “si existiera” override: debe ser excepcional y auditado.\
**Regla dura (corrección):**

- Solo `COUNTRY_OPS_LEAD` o `SUPER_ADMIN` con `coverage.override`

- Requiere `reason_code` y crea `coverage_override_event`

- Snapshot de orden marca `coverage_result=OVERRIDDEN` con actor/razón\
    **Suposición:** el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 seller_profiles (cobertura)

Campos mínimos:

- `seller_id`

- `country_id`, `hub_id`, `zone_id`

- `location (POINT)`

- `coverage_radius_meters`

- `fulfillment_mode` (HYPER_LOCAL|WORLDWIDE|BOTH)

- `shipping_countries` JSON (futuro)

- `coverage_rings` JSON (opcional)

- `delivery_rules` JSON (days/windows/cutoffs/blackouts)

Índices:

- (`country_id`,`hub_id`)

- GIST(`location`) para queries geoespaciales

### 6.2 buyer_addresses

Campos mínimos:

- `address_id`, `buyer_id`

- `country_code`

- `raw_address` JSON

- `normalized_address`

- `location (POINT)` (validado)

- `address_quality_score`

- `geocode_provider_meta` (place_id, confidence)

- `is_default`, `label`, `created_at`

Índices:

- (`buyer_id`,`created_at desc`)

- GIST(`location`)

### 6.3 countries / hubs / zones

- `countries`: `address_schema`, moneda, unidades (km/millas), reglas macro.

- `hubs`: `timezone`, `map_center`, `status`.

- `zones`: `polygon (PostGIS)`, `status (ACTIVE/INACTIVE/SATURATED)`.

### 6.4 order_logistics_snapshot

Campos mínimos:

- `order_id`

- `fulfillment_type`

- `seller_location`, `buyer_location`

- `distance_meters`

- `coverage_pass` boolean

- `coverage_reason` enum

- `resolved_country/hub/zone`

- `delivery_fee_calculated`

- `geocode_provider_meta`

- `snapshot_created_at`

Índices:

- unique(`order_id`)

- (`resolved_country`,`hub_id`,`snapshot_created_at desc`)

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### 7.1 Eventos mínimos

- `ADDRESS_VALIDATED` (con meta de geocode)

- `ADDRESS_SAVED`

- `COVERAGE_CHECK_RUN` (audit)

- `COVERAGE_RESULT_PASS/FAIL`

- `ZONE_STATUS_CHANGED` (kill switch / saturated)

- `SELLER_COVERAGE_UPDATED`

- `ORDER_LOGISTICS_SNAPSHOT_CREATED`

### 7.2 Idempotencia

- `addresses/validate`: idempotente por `(buyer_id, raw_address_hash)` si se cachea.

- `coverage/check`: idempotente por `(seller_id, address_id, date_bucket, algo_version)` para caching controlado.

- `order_snapshot`: idempotente por `(order_id)`.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Búsqueda

- Query geoespacial: `ST_DWithin(seller.location, buyer.location, seller.radius)` para mostrar solo lo comprable.

- Entrada por link directo: si fuera de zona, mostrar “fuera de área de servicio”.

### Órdenes

- En `ORDER_CREATED` o **antes del pago** se guarda `order_logistics_snapshot`.

- Si falla cobertura: **no se crea escrow/pago**.

### Seguridad

- En HYPER_LOCAL, coverage y address location son insumo para **geo-check \~300m + PIN**.

### Soporte/Disputas

- Consola muestra:

    - distancia calculada,

    - place_id/confidence,

    - historial de cambios de dirección,

    - override auditado (si existió).

### Reputación

- Métricas logísticas alimentan score:

    - fallas por dirección inválida,

    - tardanzas por distancia,

    - cancelaciones por fuera de cobertura (deben tender a 0 si Guard es correcto).

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Métricas mínimas

- `coverage_checks_total{country,hub,result,reason}`

- `coverage_pass_rate{country,hub}`

- `address_validate_fail_total{country,reason}`

- `near_limit_cases_total{country,hub}`

- `zones_saturated_total{country,hub}`

- `seller_coverage_updates_total{country,hub}`

- `order_snapshot_missing_total` (invariante roto)

### Alertas

- Caída abrupta del pass_rate (proveedor geocode caído o hubs desconfigurados)

- Aumento de `ADDRESS_NOT_GEO_CODED` (UI rota o geocode)

- Zonas `SATURATED` creciendo (capacidad operativa)

- `order_snapshot_missing_total > 0` (bug crítico)

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Se registra `coverage_check_run` con actor, seller_id, address_id, distancia, resultado, versión algoritmo.

- Cambios de `seller.location`, `coverage_radius` y estados de `zones` se auditan.

- Overrides (si existen) siempre auditados con razón y actor.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Búsqueda:** filtrado ST_DWithin y mismo motor que Coverage Guard.

- **Órdenes/Pagos:** snapshot logístico y bloqueo de pago si FAIL.

- **Seguridad (Tridente):** geo-cerca + PIN en HYPER_LOCAL.

- **Soporte/Disputas:** evidencia geocode/distancia y auditoría de overrides.

- **Reputación:** métricas logísticas como drivers.

---

### Conflictos/incoherencias corregidas (dentro de Cobertura)

1. **Guardar direcciones sin lat/long** → prohibido (sin coordenadas no hay cobertura).

2. **Mostrar productos “comprables” que luego fallan en checkout** → corregido: Búsqueda usa ST_DWithin y Coverage usa el mismo motor/radio.

3. **Coverage evaluada después de slots/pagos** → corregido: Coverage Guard corre antes de scheduler y antes de dinero.

4. **Direcciones caóticas sin evidencia para soporte** → corregido: Address Intelligence guarda place_id/confidence + snapshot logístico por orden.

5. **Overrides sin trazabilidad** → corregido: override solo con permiso, razón, evento y snapshot marcado.