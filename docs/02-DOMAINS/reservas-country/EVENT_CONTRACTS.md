# EVENT_CONTRACTS · reservas-country

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (Reserva Nacional + Waterfall)
- Regla exacta de qué eventos alimentan inflow a reserve además del routing por vacancia (p.ej., diferencial cap-earn si Rate Engine lo define).
- Si quieres, lo siguiente es convertir este sistema a contratos “copy-paste para ingeniería”: endpoints admin exactos, enums purpose_code, eventos definitivos, y un set mínimo de tests UAT (vacancia, disbursement, pérdida y recovery).
- Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)
- Fuentes de verdad:
- “resumen-260207_1014” (Continuidad, vacancia, routing a reserva, break-glass, four-eyes, monitoreo).
- “waterfall-engine-v10-260207_0941” (Waterfall de pérdidas, layers, loss_case, recovery al COL, guardrails, ledger doble-entry).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


## Control operativo verificable

- Owner: `Equipo reservas-country`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RESERVASCOUN-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reservas-country/dominio-reservas-country-operacion`
  - `https://jira.aventide.gift/browse/OPS-RESERVASCOUN-241`

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
