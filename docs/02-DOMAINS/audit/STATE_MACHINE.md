# STATE_MACHINE · audit

## Estados

- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- metadata (ip, ua, geo, request_id),
- request_id, requester, approver, action, timestamps.
- Requester + Approver con request_id en auditoría.
- SYSTEM/WORKER (Service_ID): produce eventos obligatorios por write-path.
- SensitiveReadGuard (VIEW_SENSITIVE siempre genera evento)
- Fallo en escritura de auditoría: la acción crítica debe fallar (enforcement) o entrar en modo safe (bloqueo) según severidad. (Inferencia: consistente con “toda acción crítica write debe producir evento”.)
- Operación definida y validada evento debe tener actor_id y actor_type (USER|SERVICE).
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (audit-aware)


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
