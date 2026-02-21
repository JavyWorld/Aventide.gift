# INVARIANTS · orders

Reglas no negociables del dominio:
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.
- Snapshot inmutable de precios/fees/items/dirección/promesa.
- Reintentos: idempotencia por payment_attempt_id.
- address_snapshot JSON (inmutable)
- 6.2 Timeline / Action Stream (append-only)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- endpoints mutables con idempotency_key
- 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)
- Auditoría fuerte


## Control operativo verificable

- Owner: `Equipo orders`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ORDERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/orders/dominio-orders-operacion`
  - `https://jira.aventide.gift/browse/OPS-ORDERS-241`

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
