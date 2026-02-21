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
