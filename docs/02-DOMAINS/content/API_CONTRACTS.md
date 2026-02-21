# API_CONTRACTS · content

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Jerarquía/RBAC: Ops Lead scoped por país para revisión; seller solo lo suyo.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- QualityGateGuard (capacidad + logística + assets + atributos requeridos + estado de seller)

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Jerarquía/RBAC: Ops Lead scoped por país para revisión; seller solo lo suyo.
- QualityGateGuard (capacidad + logística + assets + atributos requeridos + estado de seller)

## Códigos de error

- Rechazo: estado REJECTED con razón específica (“foto borrosa”, “descripción engañosa”).

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo content`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-CONTENT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/content/dominio-content-operacion`
  - `https://jira.aventide.gift/browse/OPS-CONTENT-241`

## Trazabilidad

- Documento origen: `sistema-de-contenido-260206_2344.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
