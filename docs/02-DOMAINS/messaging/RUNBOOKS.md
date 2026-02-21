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
