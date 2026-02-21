# RUNBOOKS · rate-engine

## Operación
- Multi-país real: floors/ceilings, smoothing, segmentación segura y canary/rollback por país/hub/segmento.
- Canary/rollback por versión de policy.
- rates.policy.rollback (super_admin/ops lead scoped)
- Si falla: rollback automático a last_known_good.
- 5.7 Canary/rollback (operación de producción)
- Rollback automático si se rompen SLOs (conversión/riesgo/margen).

## Incidentes, rollback y backfill
- Multi-país real: floors/ceilings, smoothing, segmentación segura y canary/rollback por país/hub/segmento.
- Canary/rollback por versión de policy.
- rates.policy.rollback (super_admin/ops lead scoped)
- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Si falla: rollback automático a last_known_good.
- 5.7 Canary/rollback (operación de producción)
- Rollback automático si se rompen SLOs (conversión/riesgo/margen).
- Rollback: (country_code, target_version_id)


## Control operativo verificable

- Owner: `Equipo rate-engine`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RATEENGINE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/rate-engine/dominio-rate-engine-operacion`
  - `https://jira.aventide.gift/browse/OPS-RATEENGINE-241`

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
