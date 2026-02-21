# RUNBOOKS · memory

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.

## Incidentes, rollback y backfill
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.
- Objetivos (duros):
- Reuso: reducir fricción en compras repetidas (cumples, aniversarios, Navidad).


## Control operativo verificable

- Owner: `Equipo memory`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MEMORY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/memory/dominio-memory-operacion`
  - `https://jira.aventide.gift/browse/OPS-MEMORY-241`

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo memory`
- **Owner negocio/regulatorio:** `Product + Compliance (memory)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

