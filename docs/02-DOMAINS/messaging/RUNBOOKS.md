# RUNBOOKS · messaging

## Operación
- ADMIN/OPS LEAD: auditoría/operación (scoped por país).
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Spike de freezes (operación/disputas) anormal
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.

## Incidentes, rollback y backfill
- Send message: idempotencia por client_message_id por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Mensajería es un chat in-app, contextual a una orden, diseñado para que el flujo ideal sea cero conversación (“silencio por defecto”) y el chat se active solo por excepción, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.
- Objetivos (duros):
- Mantener el marketplace seguro: impedir bypass off-platform (teléfonos, pagos externos), acoso, spam y fraude.
- Ser evidencia operativa/legal: inmutable, auditable y exportable para Soporte/Disputas.


## Control operativo verificable

- Owner: `Equipo messaging`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MESSAGING-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/messaging/dominio-messaging-operacion`
  - `https://jira.aventide.gift/browse/OPS-MESSAGING-241`

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo messaging`
- **Owner negocio/regulatorio:** `Product + Compliance (messaging)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

