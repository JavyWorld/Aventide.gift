# STATE_MACHINE · waterfall

## Estados

- estado de recuperación
- loss_case creado en estado OPEN.
- Estados del caso:OPEN -> APPLIED -> RECOVERY_ACTIVE -> RECOVERY_CLOSEDo OPEN -> EMERGENCY_ESCALATION si Global no alcanza.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Triggers

- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- eventos Kafka/Webhook (loss.created, waterfall.applied, recovery.settled, etc.),
- Recibe eventos de pérdida:
- Eventos de default


## Control operativo verificable

- Owner: `Equipo waterfall`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-WATERFALL-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/waterfall/dominio-waterfall-operacion`
  - `https://jira.aventide.gift/browse/OPS-WATERFALL-241`

## Trazabilidad

- Documento origen: `waterfall-engine-v10-260207_0941.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
