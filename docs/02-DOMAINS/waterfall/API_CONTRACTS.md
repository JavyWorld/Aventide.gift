# API_CONTRACTS · waterfall

## Endpoints y auth
- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- plan de recapitalización por prioridad de impacto
- 11) API mínima (lista para backend)
- idempotency-key
- request-signature
- eventos Kafka/Webhook (loss.created, waterfall.applied, recovery.settled, etc.),
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️
- Waterfall Engine v1.0

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️
- Waterfall Engine v1.0
- Objetivo: cubrir pérdidas de forma determinística, proteger caja global y forzar recuperación automática al nivel correcto de responsabilidad (COL).
- 1) Principios no negociables
- Orden fijo de cobertura (no alterable por operación manual):Country Reserve -> COL Liability -> Global Reserve -> Recovery obligatorio al COL

## Trazabilidad
- Documento origen: `waterfall-engine-v10-260207_0941.docx`
