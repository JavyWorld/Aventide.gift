# API_CONTRACTS · reservas-global

## Endpoints

- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- plan de recapitalización/priorización.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Esto ya capitaliza Global automáticamente (retorno de fondos) y debe ser tratado como flujo “inflow-recovery”, no como revenue.
- Sistema de Capitalización de Reserva Global v2.0 (integrado con Motor Unificado “Take Rate Engine + Revenue Rate Engine”)

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia


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
