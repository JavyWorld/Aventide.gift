# DATA_CONTRACTS · support

## Entidades y campos
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- Calcular fees/impuestos desde cero: usa snapshot financiero locked de la orden.
- El agente elige outcome (scenario_id + severity_band + affected_items[]). El sistema calcula montos desde snapshot + policies.
- Cálculo determinístico desde snapshot financiero locked.
- Cada outcome produce buckets auditables + acciones automáticas (ledger/refund/release/credit/trust).
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- inputs_schema (allowed severity, allowed affected_items)

## Constraints y claves de negocio
- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- AuditGuard (razón obligatoria + WORM append-only)
- Contacto seller / confirmar ETA / documentar en timeline.
- saga_state, idempotency_keys[]
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- Saga: idempotency_keys[] por step; reintentos no duplican refunds/releases/credits.
- Métricas operativas clave

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
