# RUNBOOKS · orders

## Operación
- SLA: aceptación rápida, producción, pickup, entrega, con alertas/acciones.
- En orden se persiste promises y items_snapshot con add-ons (operación).
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.

## Incidentes, rollback y backfill
- Reintentos: idempotencia por payment_attempt_id.
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que convierte un checkout en una entrega real con:
- Snapshot inmutable de precios/fees/items/dirección/promesa.
- Máquina de estados estricta (no saltos).
- Reglas cerradas de cancelación por estado (y ventanas).


## Control operativo verificable

- Owner: `Equipo orders`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ORDERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/orders/dominio-orders-operacion`
  - `https://jira.aventide.gift/browse/OPS-ORDERS-241`

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo orders`
- **Owner negocio/regulatorio:** `Product + Compliance (orders)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

