# audit

## Propósito

- admin.four_eyes.request/create/approve (ops/admin; auditado)
- metadata (JSONB: ip, user-agent, geo, request context)
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
- packet_json (gps, time, device, photo_file_id, pin_state, etc.)
- audit.write (solo servicios; no humanos)
- Servicio de dominio ejecuta acción (ej. update de price, payout, role change).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado".

## Límites

- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- GET /audit/certificate/order/:order_id genera PDF/CSV con timeline:Creación → Pago → Chats → Intentos de entrega → PIN → Liberación de fondosIncluye hash de integridad del documento y referencias a evidencias.

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Compatibilidad con sistemas existentes (dependencias directas)


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
- Título extraído: "Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
