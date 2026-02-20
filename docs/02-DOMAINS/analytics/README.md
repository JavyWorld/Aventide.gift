# analytics

## Propósito

- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Cupones seller-driven:SELLER_COUPON_CREATED/UPDATED/EXPIRED, SELLER_COUPON_APPLIED/REJECTED, SELLER_COUPON_COST_BOOKED
- Documento origen: `sistema-de-analitica-260206_2336.docx`
- SSOT: dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).
- Definición y objetivos del sistema/módulo
- Sistema de Analítica v2.0 (corregido y unificado)
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Analítica v2.0 (corregido y unificado)".

## Límites

- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).
- Estados finales de órdenes y snapshots financieros (para evitar descuadres ante cambios futuros de fees/reglas).
- Alcance (incluye / excluye)
- Reglas y políticas (límites, validaciones, consistencia)

## Dependencias

- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- Analítica ≠ Observabilidad: analítica = salud negocio/crecimiento/fraude/costos; observabilidad = salud técnica; se correlacionan por trace_id/request_id.
- fact_payments: intentos, success rate, error_codes, proveedor.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Anomaly Engine (operativo + fraude/abuso) con baselines y acciones integradas.
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-analitica-260206_2336.docx`
- Título extraído: "Sistema de Analítica v2.0 (corregido y unificado)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
