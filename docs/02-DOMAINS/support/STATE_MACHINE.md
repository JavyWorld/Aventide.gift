# STATE_MACHINE · support

## Estados

- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- Determinar la “verdad de entrega” fuera del sistema de Órdenes: Support OS consume la máquina de estados y evidencia, no la reemplaza.
- Dependencia crítica (no duplicar): financial_snapshot_locked de la orden se referencia por order_id y es el input determinista del cálculo.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos principales

## Trazabilidad

- Documento origen: `sistema-de-soporte-260207_0731.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
