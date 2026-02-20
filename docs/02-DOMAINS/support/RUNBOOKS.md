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
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
