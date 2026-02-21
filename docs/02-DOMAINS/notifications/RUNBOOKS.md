# RUNBOOKS · notifications

## Operación
- Guardrails editor de plantillas por Ops Lead (localización sin tocar código, con whitelist de variables + versioning + rollback).
- SUPPORT_AGENT / COUNTRY_OPS_LEAD: receptores internos operativos (alertas P0/P1).
- Preview + simulador antes de publicar; versioning + rollback.
- Saga: DISPUTE_STEP_FAILED debe alertar soporte inmediatamente y bloquear “resuelto” hasta completar.
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas

## Incidentes, rollback y backfill
- Confiabilidad: Outbox pattern para no perder notificaciones bajo fallos/reintentos.
- Guardrails editor de plantillas por Ops Lead (localización sin tocar código, con whitelist de variables + versioning + rollback).
- SYSTEM/BOT: orquestación, envío, reintentos, escritura Inbox, auditoría.
- Reintento del worker: no duplica envíos por dedupe_key.
- 5.6 Dedupe (evitar duplicados por reintento)
- Preview + simulador antes de publicar; versioning + rollback.
- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).
- Duplicados por reintentos → corregido: dedupe_key event_id + template_id + recipient_id.


## Control operativo verificable

- Owner: `Equipo notifications`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-NOTIFICATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/notifications/dominio-notifications-operacion`
  - `https://jira.aventide.gift/browse/OPS-NOTIFICATION-241`

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo notifications`
- **Owner negocio/regulatorio:** `Product + Compliance (notifications)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

