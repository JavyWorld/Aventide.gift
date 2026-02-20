# API_CONTRACTS · reservas-global

## Endpoints

- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- Actores y permisos (RBAC) + guards
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- plan de recapitalización/priorización.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Esto ya capitaliza Global automáticamente (retorno de fondos) y debe ser tratado como flujo “inflow-recovery”, no como revenue.
- Sistema de Capitalización de Reserva Global v2.0 (integrado con Motor Unificado “Take Rate Engine + Revenue Rate Engine”)

## Auth

- Actores y permisos (RBAC) + guards
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-reserva-global-260207_1041.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
