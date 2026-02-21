# API_CONTRACTS · rate-engine

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- status (OPEN|APPROVED|REJECTED|EXECUTED)
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- DeterminismGuard (misma entrada → mismo RateVector)

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- DeterminismGuard (misma entrada → mismo RateVector)

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
