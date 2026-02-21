# RUNBOOKS · referrals

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X E).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.

## Incidentes, rollback y backfill
- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X E).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.
- Objetivos (duros):
- Adquirir nuevos buyers y aumentar recurrencia sin afectar Seller Net ni items_subtotal.
- Mantener filosofía: FS solo contra Platform Fee y si referidos otorgan FS, cuenta dentro de caps mensuales de FS del buyer.
- Ser determinista: estados + ventana de atribución + hold windows + catálogo de reglas por país (server-driven).


## Control operativo verificable

- Owner: `Equipo referrals`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REFERRALS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/referrals/dominio-referrals-operacion`
  - `https://jira.aventide.gift/browse/OPS-REFERRALS-241`

## Trazabilidad
- Documento origen: `sistema-de-referido-260207_0826.docx`
