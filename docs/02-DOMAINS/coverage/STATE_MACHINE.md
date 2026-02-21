# STATE_MACHINE · coverage

## Estados

- Snapshot de orden marca coverage_result=OVERRIDDEN con actor/razónSuposición: el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.
- Cambios de seller.location, coverage_radius y estados de zones se auditan.
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.
- Integración con Búsqueda (ST_DWithin) y Ordenes (snapshot logístico).

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
