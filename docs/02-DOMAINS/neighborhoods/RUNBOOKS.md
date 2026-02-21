# RUNBOOKS · neighborhoods

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema Barrio v2.0 (Círculos privados) — corregido y unificado
- Basado en: definición “Social layer: Barrio (o Círculos)” + sus componentes (recipients compartidos, fechas opt-in, wishlists temáticas, notificación de regalo entrante).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Barrio es una capa social privada encima de Usuarios + Memory (recipients/perfil/agenda) que permite organizar familiares/amigos en grupos (“barrios/círculos”) y habilitar:

## Incidentes, rollback y backfill
- Sistema Barrio v2.0 (Círculos privados) — corregido y unificado
- Basado en: definición “Social layer: Barrio (o Círculos)” + sus componentes (recipients compartidos, fechas opt-in, wishlists temáticas, notificación de regalo entrante).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Barrio es una capa social privada encima de Usuarios + Memory (recipients/perfil/agenda) que permite organizar familiares/amigos en grupos (“barrios/círculos”) y habilitar:
- lista de recipients dentro del grupo (usuarios Aventide o externos),
- fechas importantes compartidas (opt-in),
- wishlists temáticas (preferencias, no productos específicos),
- y “apps hablándose”: opción de notificar al recipient que le llegará un regalo (sin revelar qué) respetando sorpresa y “Admirador Secreto”.


## Control operativo verificable

- Owner: `Equipo neighborhoods`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-NEIGHBORHOOD-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/neighborhoods/dominio-neighborhoods-operacion`
  - `https://jira.aventide.gift/browse/OPS-NEIGHBORHOOD-241`

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo neighborhoods`
- **Owner negocio/regulatorio:** `Product + Compliance (neighborhoods)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

