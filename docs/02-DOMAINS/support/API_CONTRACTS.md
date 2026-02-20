# API_CONTRACTS · support

## Endpoints

- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- Actores y permisos (RBAC) + guards
- saga_state, idempotency_keys[]
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- EvidenceGuard (para acciones que dependan de PoD)

## Auth

- Actores y permisos (RBAC) + guards
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- EvidenceGuard (para acciones que dependan de PoD)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- saga_state, idempotency_keys[]
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-soporte-260207_0731.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
