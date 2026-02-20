# support

## Propósito

- support.dispute.execute_saga (system; L2 dispara “request execution”)
- requester_type (BUYER/SELLER/INTERNAL), requester_id
- sla_first_response_at, sla_resolution_at
- Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- Definición y objetivos del sistema/módulo
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- Documento origen: `sistema-de-soporte-260207_0731.docx`
- Casos de disputa (state machine formal),
- Disputas: apertura, hold de fondos, recopilación de evidencia, veredicto por outcomes, ejecución financiera por saga, chargebacks.
- Determinar la “verdad de entrega” fuera del sistema de Órdenes: Support OS consume la máquina de estados y evidencia, no la reemplaza.
- “Reembolsos grandes o sensibles” requieren Finance Reviewer antes de ejecutar la saga. El umbral y criterios son policy-driven por país.
- support.dispute_saga_started/step_succeeded/step_failed/completed
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado".

## Límites

- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- Alcance (incluye / excluye)
- support.ticket.assign/escalate (L1+ con límites)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- Integración con Trust & Safety: colusión/abuso/extorsión, moderación de reseñas conflictivas.
- Dependencia crítica (no duplicar): financial_snapshot_locked de la orden se referencia por order_id y es el input determinista del cálculo.
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-soporte-260207_0731.docx`
- Título extraído: "Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
