# EVENT_CONTRACTS · rate-engine

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)
- Fuente de verdad: “Motor Unificado de Rates para Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Motor único que gobierna, de forma dinámica, determinista y auditable, todos los porcentajes (rates) que impactan el dinero de una orden, separando estrictamente:
- lo que ve el buyer (buyer-facing, estable y acotado),
- lo que se distribuye internamente (platform fee, payout al Country Ops Lead y Reserva Nacional por país) dentro de guardrails.
- Este motor sustituye la lógica dispersa del “Take-Rate Engine OS” y del “Revenue Rate Engine” por un solo cerebro que produce un RateVector y lo “compila” a un breakdown financiero y a un blueprint de ledger/settlement, todo con snapshot por orden.

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
