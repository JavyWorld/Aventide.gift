# RUNBOOKS · audit

## Operación
- Alerta por escalada inusual (ej. finanzas a soporte).
- Índices mínimos (operación real):
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.

## Incidentes, rollback y backfill
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Objetivos (no negociables):
- WORM/append-only: un registro de auditoría nunca se edita ni se borra.
- Snapshotting: demostrar cómo era algo antes de cambios (precio/fotos/listing).
- Atribución estricta: no existen acciones “anónimas” del sistema: siempre User_ID o Service_ID.


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

## Ownership & Escalation

- **Owner técnico:** `Equipo audit`
- **Owner negocio/regulatorio:** `Product + Compliance (audit)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

