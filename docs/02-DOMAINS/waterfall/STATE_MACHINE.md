# STATE_MACHINE · waterfall

## Estados detectados/derivados
- estado de recuperación
- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- Recibe eventos de pérdida:
- Salida:
- loss_case creado en estado OPEN.
- Estados del caso:OPEN -> APPLIED -> RECOVERY_ACTIVE -> RECOVERY_CLOSEDo OPEN -> EMERGENCY_ESCALATION si Global no alcanza.

## Transiciones y eventos de entrada/salida
- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- Recibe eventos de pérdida:
- Salida:
- Eventos de default
- eventos Kafka/Webhook (loss.created, waterfall.applied, recovery.settled, etc.),
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️
- Waterfall Engine v1.0
- Objetivo: cubrir pérdidas de forma determinística, proteger caja global y forzar recuperación automática al nivel correcto de responsabilidad (COL).

## Trazabilidad
- Documento origen: `waterfall-engine-v10-260207_0941.docx`
