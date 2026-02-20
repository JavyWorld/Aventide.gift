# disputes

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (límites, validaciones, caps, invariantes)
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado

## Dependencias
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- SYSTEM/BOT: ejecuta saga, integra con provider, ledger, docs, trust, loyalty.
- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- 8.2 Pagos/Escrow/Provider

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
- Título extraído: "Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado".
