# DATA_CONTRACTS · audit

## Entidades y campos
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Snapshotting: demostrar cómo era algo antes de cambios (precio/fotos/listing).
- Ledger contable como fuente de movimientos (Ledger mueve dinero; auditoría responde “quién ordenó moverlo”).
- Ledger registra movimientos; auditoría registra:
- En ORDER_CREATED se guarda product_snapshot asociado a la orden:
- Seller cambia foto después: no afecta el snapshot ya guardado.
- Ideal: DB/tabla separada donde ni SuperAdmin pueda borrar/modificar.
- 6.1 audit_logs (tabla estandarizada)

## Constraints y claves de negocio
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- WORM/append-only: un registro de auditoría nunca se edita ni se borra.
- Foto PoD: URL firmada privada; accesible solo roles autorizados.
- GET /audit/certificate/order/:order_id genera PDF/CSV con timeline:Creación → Pago → Chats → Intentos de entrega → PIN → Liberación de fondosIncluye hash de integridad del documento y referencias a evidencias.
- evidence_links[] (PoD foto firmada, chat PDF, docs)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- audit insert: idempotente por event_id (si se usa outbox) o por (request_id, action_type, resource_id, created_at_bucket) según fuente.


## Control operativo verificable

- Owner: `Equipo audit`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-AUDIT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/audit/dominio-audit-operacion`
  - `https://jira.aventide.gift/browse/OPS-AUDIT-241`

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
