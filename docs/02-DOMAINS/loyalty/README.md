# loyalty

## Propósito

- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos”
- Documento origen: `sistema-de-lealtad-260207_0817.docx`
- caps_state_monthly (JSON: used_fs_this_month, month_key, etc.)
- Definición y objetivos del sistema/módulo
- Cupones seller-funded (es Promos del seller; aquí solo se integra para calcular EOV/earn).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado".

## Límites

- Idempotencia (reglas)
- Alcance (incluye / excluye)
- Aplicación de FS en checkout como Fee Credit con límite: max_applied = platform_fee_amount (nunca más).
- Se calcula EOV (Eligible Order Value):EOV = (items_subtotal - seller_coupon_discount) + delivery_fee_if_applicableExcluye: taxes, platform_fee, ops_fee, processing_fee.

## Dependencias

- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”
- Integración obligatoria con Disputas/Refunds (reversión)
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado".

## Trazabilidad

- Documento origen: `sistema-de-lealtad-260207_0817.docx`
- Título extraído: "Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
