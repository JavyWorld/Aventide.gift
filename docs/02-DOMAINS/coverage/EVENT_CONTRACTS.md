# EVENT_CONTRACTS · coverage

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Requiere reason_code y crea coverage_override_event
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos mínimos
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Objetivos:
- Evitar órdenes imposibles: sin cobertura no hay calendario, no hay checkout y no hay pago.


## Control operativo verificable

- Owner: `Equipo coverage`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-COVERAGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/coverage/dominio-coverage-operacion`
  - `https://jira.aventide.gift/browse/OPS-COVERAGE-241`

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
