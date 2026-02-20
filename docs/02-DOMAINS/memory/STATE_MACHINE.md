# STATE_MACHINE · memory

## Estados detectados/derivados
- Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).
- 4) Flujos end-to-end (happy path + edge cases)
- Se escribe evento MEMORY_PROFILE_UPDATED con diff.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Memory

## Transiciones y eventos de entrada/salida
- Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).
- Se escribe evento MEMORY_PROFILE_UPDATED con diff.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Memory
- Auditoría: eventos y lecturas sensibles trazables.
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`
