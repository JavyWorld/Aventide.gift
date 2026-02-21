# INVARIANTS · waterfall

Reglas no negociables del dominio:
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️
- Objetivo: cubrir pérdidas de forma determinística, proteger caja global y forzar recuperación automática al nivel correcto de responsabilidad (COL).
- 1) Principios no negociables
- No retroactividad: cada orden usa su snapshot financiero inmutable.
- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- E. Governance & Audit
- logs inmutables
- nunca dejar ops_lead_earn_pct por debajo de floor
- idempotency-key
- audit-trail


## Control operativo verificable

- Owner: `Equipo waterfall`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-WATERFALL-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/waterfall/dominio-waterfall-operacion`
  - `https://jira.aventide.gift/browse/OPS-WATERFALL-241`

## Trazabilidad
- Documento origen: `waterfall-engine-v10-260207_0941.docx`
