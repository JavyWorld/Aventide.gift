# RUNBOOKS · support

## Operación
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- L3 (Country Ops Lead): intervención fuerte en incidentes críticos + Force Complete controlado.
- ScopeGuard (country_code obligatorio para operación)
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Soporte como “call center infinito” → corregido: 2 dominios (incidente vivo vs disputa) + L0 fuerte.

## Incidentes, rollback y backfill
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- L3 (Country Ops Lead): intervención fuerte en incidentes críticos + Force Complete controlado.
- Autorizar reintento, reemplazo urgente o cancelación operativa (si hay dinero ya: se abre disputa/outcome).
- Saga: idempotency_keys[] por step; reintentos no duplican refunds/releases/credits.
- Soporte como “call center infinito” → corregido: 2 dominios (incidente vivo vs disputa) + L0 fuerte.
- Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


## Control operativo verificable

- Owner: `Equipo support`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SUPPORT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/support/dominio-support-operacion`
  - `https://jira.aventide.gift/browse/OPS-SUPPORT-241`

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo support`
- **Owner negocio/regulatorio:** `Product + Compliance (support)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

