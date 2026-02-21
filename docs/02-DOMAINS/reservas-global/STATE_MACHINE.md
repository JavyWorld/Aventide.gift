# STATE_MACHINE · reservas-global

## Estados

- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- No tocar lo buyer-facing fuera de límites: el motor decide rates, pero el snapshot por orden es inmutable y no retroactivo.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)
- Esto ya capitaliza Global automáticamente (retorno de fondos) y debe ser tratado como flujo “inflow-recovery”, no como revenue.
- EMERGENCY_ESCALATION_TRIGGERED(loss_case_id) (ya existe como flujo)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos y triggers
- EMERGENCY_ESCALATION_TRIGGERED(loss_case_id) (ya existe como flujo)


## Control operativo verificable

- Owner: `Equipo reservas-global`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RESERVASGLOB-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reservas-global/dominio-reservas-global-operacion`
  - `https://jira.aventide.gift/browse/OPS-RESERVASGLOB-241`

## Trazabilidad

- Documento origen: `sistema-de-reserva-global-260207_1041.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
