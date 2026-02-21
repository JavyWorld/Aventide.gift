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
