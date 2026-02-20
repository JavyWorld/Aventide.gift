# loyalty

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Aplicación de FS en checkout como Fee Credit con límite: max_applied = platform_fee_amount (nunca más).
- Excluye
- Se calcula EOV (Eligible Order Value):EOV = (items_subtotal - seller_coupon_discount) + delivery_fee_if_applicableExcluye: taxes, platform_fee, ops_fee, processing_fee.

## Dependencias
- Integración obligatoria con Disputas/Refunds (reversión)
- Cupones seller-funded (es Promos del seller; aquí solo se integra para calcular EOV/earn).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- 11) Compatibilidad con sistemas existentes (dependencias directas)
- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado

## Trazabilidad
- Documento origen: `sistema-de-lealtad-260207_0817.docx`
- Título extraído: "Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado".
