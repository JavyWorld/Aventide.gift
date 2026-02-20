# STATE_MACHINE · reservas-country

## Estados detectados/derivados
- SUPER_ADMIN (global): puede activar estados especiales (LOCKDOWN), aplicar break-glass para acciones críticas y forzar medidas de contención con evidencia.
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- 4) Flujos end-to-end (happy path + edge cases)
- Cambio de estado en medio de un checkout: se respeta el snapshot de la orden (no retroactividad).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (Reserva Nacional + Waterfall)

## Transiciones y eventos de entrada/salida
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (Reserva Nacional + Waterfall)
- Regla exacta de qué eventos alimentan inflow a reserve además del routing por vacancia (p.ej., diferencial cap-earn si Rate Engine lo define).
- Si quieres, lo siguiente es convertir este sistema a contratos “copy-paste para ingeniería”: endpoints admin exactos, enums purpose_code, eventos definitivos, y un set mínimo de tests UAT (vacancia, disbursement, pérdida y recovery).
- Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)
- Fuentes de verdad:
- “resumen-260207_1014” (Continuidad, vacancia, routing a reserva, break-glass, four-eyes, monitoreo).

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
