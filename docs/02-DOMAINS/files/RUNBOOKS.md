# RUNBOOKS · files

## Operación
- alerta,
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Accesos no auditados → corregido: file_access_log append-only (incluye emisión de signed URL) + break-glass con razón y alerta.
- Sistema de Archivos v2.0 (Storage & Attachments) — corregido y unificado
- Fuente de verdad: “Sistema de Archivos (Storage & Attachments)”.

## Incidentes, rollback y backfill
- Reintentos: emisión de URL se loguea cada vez; no afecta el objeto.
- Sistema de Archivos v2.0 (Storage & Attachments) — corregido y unificado
- Fuente de verdad: “Sistema de Archivos (Storage & Attachments)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema central de almacenamiento para media pública, adjuntos privados, evidencia operativa, y documentos legales/fiscales, con:
- control estricto RBAC+ABAC (“need-to-know”),
- entrega por Signed URLs para contenido privado,
- retención diferenciada por clase de dato,


## Control operativo verificable

- Owner: `Equipo files`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-FILES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/files/dominio-files-operacion`
  - `https://jira.aventide.gift/browse/OPS-FILES-241`

## Trazabilidad
- Documento origen: `sistema-de-archivos-260207_0840.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo files`
- **Owner negocio/regulatorio:** `Product + Compliance (files)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

