# RUNBOOKS · platform-structure

## Operación
- Rutas de Studio + flujo draft→preview→publish + time machine + rollback con auditoría completa.
- ui_profiles versionadas (config_version), scheduling, rollback, auditoría; entrega por contrato (profile/flags/dictionary/modules/validation_rules/schema_version/signature/ETag).
- SLO prioridad money pipeline: SEV0 si checkout roto por país, payout detenido, duplicación de cobros.
- Camaleón/Config ↔ resiliencia (firma/ETag/fallback/rollback) ↔ observabilidad.
- UI hardcodeada por país → fijo: Server-Driven UI (Camaleón) con firma/ETag/fallback/rollback.
- Estructura de Deployment v2.0 (CI/CD + Entornos + Rollback) — alineada a “Estructura”

## Incidentes, rollback y backfill
- Rutas de Studio + flujo draft→preview→publish + time machine + rollback con auditoría completa.
- ui_profiles versionadas (config_version), scheduling, rollback, auditoría; entrega por contrato (profile/flags/dictionary/modules/validation_rules/schema_version/signature/ETag).
- Camaleón/Config ↔ resiliencia (firma/ETag/fallback/rollback) ↔ observabilidad.
- UI hardcodeada por país → fijo: Server-Driven UI (Camaleón) con firma/ETag/fallback/rollback.
- Estructura de Deployment v2.0 (CI/CD + Entornos + Rollback) — alineada a “Estructura”
- Definición: Estructura de deployment es el conjunto de entornos, pipelines, artefactos, estrategias de release y rollback que permiten desplegar el monolito modular (API), los workers (BullMQ), y las superficies (web/mobile/paneles), garantizando:
- idempotencia y continuidad ante reintentos,
- Camaleón (server-driven UI) con publish/rollback seguro,


## Control operativo verificable

- Owner: `Equipo platform-structure`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PLATFORMSTRU-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/platform-structure/dominio-platform-structure-operacion`
  - `https://jira.aventide.gift/browse/OPS-PLATFORMSTRU-241`

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo platform-structure`
- **Owner negocio/regulatorio:** `Product + Compliance (platform-structure)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

