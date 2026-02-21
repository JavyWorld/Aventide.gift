# INVARIANTS · audit

Reglas no negociables del dominio:
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Objetivos (no negociables):
- WORM/append-only: un registro de auditoría nunca se edita ni se borra.
- Atribución estricta: no existen acciones “anónimas” del sistema: siempre User_ID o Service_ID.
- Trazabilidad completa para disputas/chargebacks/auditorías fiscales: acciones administrativas, dinero, catálogo y evidencia logística/legal (PoD + chat).
- 4 capas auditadas obligatorias:
- Exportabilidad: “Certificado de Auditoría” por orden (PDF/CSV) con timeline completo.
- Ledger contable como fuente de movimientos (Ledger mueve dinero; auditoría responde “quién ordenó moverlo”).


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
