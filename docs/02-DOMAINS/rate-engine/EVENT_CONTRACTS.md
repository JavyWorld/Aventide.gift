# EVENT_CONTRACTS · rate-engine

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)
- Fuente de verdad: “Motor Unificado de Rates para Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Motor único que gobierna, de forma dinámica, determinista y auditable, todos los porcentajes (rates) que impactan el dinero de una orden, separando estrictamente:
- lo que ve el buyer (buyer-facing, estable y acotado),
- lo que se distribuye internamente (platform fee, payout al Country Ops Lead y Reserva Nacional por país) dentro de guardrails.
- Este motor sustituye la lógica dispersa del “Take-Rate Engine OS” y del “Revenue Rate Engine” por un solo cerebro que produce un RateVector y lo “compila” a un breakdown financiero y a un blueprint de ledger/settlement, Operación definida y validada con snapshot por orden.


## Control operativo verificable

- Owner: `Equipo rate-engine`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RATEENGINE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/rate-engine/dominio-rate-engine-operacion`
  - `https://jira.aventide.gift/browse/OPS-RATEENGINE-241`

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
