# EVENT_CONTRACTS · waterfall

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- Recibe eventos de pérdida:
- Eventos de default
- eventos Kafka/Webhook (loss.created, waterfall.applied, recovery.settled, etc.),
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️
- Waterfall Engine v1.0
- Objetivo: cubrir pérdidas de forma determinística, proteger caja global y forzar recuperación automática al nivel correcto de responsabilidad (COL).
- 1) Principios no negociables
- Orden fijo de cobertura (no alterable por operación manual):Country Reserve -> COL Liability -> Global Reserve -> Recovery obligatorio al COL
- Toda pérdida tiene expediente único (loss_case_id) con trazabilidad completa de:

## Trazabilidad
- Documento origen: `waterfall-engine-v10-260207_0941.docx`
