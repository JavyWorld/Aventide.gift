# EVENT_CONTRACTS · continuity

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos/señales a vigilar (mínimo):
- SEV0: LOCKDOWN activado o spike de break-glass + eventos críticos correlacionados.
- WORM y evidencia: todo cambio de estado/rol y cada acción sensible genera eventos auditables y adjunta evidencia (links).
- Si había payout schedule activo al COL saliente: poner hold preventivo si policy lo exige (especialmente si vacancia por riesgo).
- timeline_refs[] (audit event IDs)
- Umbral crítico → sugerir LOCKDOWN (si policy lo permite) y aplicar holds preventivos.
- Eventos técnicos como QUEUE_REROUTED/PAYOUT_HOLD_APPLIED: el documento define reroute/holds como comportamiento; los nombres exactos de eventos pueden variar, pero deben quedar auditados WORM.

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
