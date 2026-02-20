# STATE_MACHINE · support

## Estados detectados/derivados
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- Casos de disputa (state machine formal),
- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- Disputas: apertura, hold de fondos, recopilación de evidencia, veredicto por outcomes, ejecución financiera por saga, chargebacks.
- Determinar la “verdad de entrega” fuera del sistema de Órdenes: Support OS consume la máquina de estados y evidencia, no la reemplaza.

## Transiciones y eventos de entrada/salida
- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- Disputas: apertura, hold de fondos, recopilación de evidencia, veredicto por outcomes, ejecución financiera por saga, chargebacks.
- support.dispute.execute_saga (system; L2 dispara “request execution”)
- “Reembolsos grandes o sensibles” requieren Finance Reviewer antes de ejecutar la saga. El umbral y criterios son policy-driven por país.
- saga_state, idempotency_keys[]
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos principales
- support.dispute_saga_started/step_succeeded/step_failed/completed

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
