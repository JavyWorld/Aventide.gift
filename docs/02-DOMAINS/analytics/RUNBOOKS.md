# RUNBOOKS · analytics

## Operación
- Definición: Sistema de Analítica es el “HUB central” que captura, consolida y expone métricas de negocio y operación del marketplace, derivadas de:
- Modelos analíticos (facts/dims) y rollups para BI y operación near-real-time.
- Real-time operativo / eventual para BI profundo: operación “hoy/última hora” near-real-time; cohortes/finanzas pesadas con jobs.
- COUNTRY_OPS_LEAD (Regional OS): operación + crecimiento de su país/hub/zone.
- 4.3 Rollups para operación y BI
- 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Analítica

## Incidentes, rollback y backfill
- Reintento de evento: dedupe por event_id (idempotencia).
- Sistema de Analítica v2.0 (corregido y unificado)
- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema de Analítica es el “HUB central” que captura, consolida y expone métricas de negocio y operación del marketplace, derivadas de:
- Eventos críticos server-side (inmutables, append-only).
- Estados finales de órdenes y snapshots financieros (para evitar descuadres ante cambios futuros de fees/reglas).
- Modelos analíticos (facts/dims) y rollups para BI y operación near-real-time.

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`
