# STATE_MACHINE · reservas-global

## Estados detectados/derivados
- 4) Flujos end-to-end (happy path + edge cases)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Esto ya capitaliza Global automáticamente (retorno de fondos) y debe ser tratado como flujo “inflow-recovery”, no como revenue.
- 8) Eventos y triggers
- EMERGENCY_ESCALATION_TRIGGERED(loss_case_id) (ya existe como flujo)

## Transiciones y eventos de entrada/salida
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- 8) Eventos y triggers
- Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)
- Fuentes de verdad:
- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Continuidad / Country Governance (VACANT/LOCKDOWN, break-glass, four-eyes, WORM).
- Reserva Nacional v2.0 (Layer 1, workflow, prohibiciones, observabilidad).

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
