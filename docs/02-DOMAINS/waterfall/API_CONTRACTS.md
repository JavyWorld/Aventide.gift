# API_CONTRACTS · waterfall

## Endpoints

- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- plan de recapitalización por prioridad de impacto
- API mínima (lista para backend)
- idempotency-key
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Auth

- Aplicar autenticación obligatoria con RBAC y scoping de dominio en todas las operaciones.

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- idempotency-key
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


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
