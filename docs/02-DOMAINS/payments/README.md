# payments

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Payouts/cashout con límites por país + KYC thresholds + rolling reserve.
- Excluye
- Seller solicita retiro → validar límites por país:

## Dependencias
- Motor legal específico por país fuera de configuración (solo integración por policy/retención).
- Webhook duplicado: dedupe por provider_event_id / rapyd_transaction_id.
- Processing Fee (pct+flat) integrado consistentemente (incluye gross-up cuando aplica)
- 6.1 Payment Transaction (provider)
- provider = RAPYD

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".
