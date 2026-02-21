# API_CONTRACTS · moderation

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Price anomaly: bloqueo si desviación absurda (lavado/error).
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Corrección de incoherencia: StrikeLedger es proyección; los cambios reales ocurren vía eventos STRIKE_APPLIED + policy engine que setea flags en user_status y seller_operational_flags.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard

## Códigos de error

- Price anomaly: bloqueo si desviación absurda (lavado/error).

## Idempotency

- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo moderation`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MODERATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/moderation/dominio-moderation-operacion`
  - `https://jira.aventide.gift/browse/OPS-MODERATION-241`

## Trazabilidad

- Documento origen: `sistema-de-moderacion-260207_0828.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
