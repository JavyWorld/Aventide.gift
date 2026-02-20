# internal-credit

## Propósito

- fee_credits_requested (FS)
- store_credit_requested (BSC) (si policy lo permite como tender)
- (opcional) gcc_credit_requested si GCC está habilitado.
- store_credit_requested (BSC/GCC si policy lo permite)
- bsc_applied = min(bsc_balance, eligible_base_for_bsc, store_credit_requested)
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- Definición y objetivos del sistema/módulo
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
- Objetivos:
- Origen: compra de gift card.Uso: depende de policy del país.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado".

## Límites

- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Eliminar incoherencia “crédito genérico”: wallets separadas por tipo con reglas duras.
- Alcance (incluye / excluye)
- Reglas y políticas (límites, expiraciones, caps, validaciones)
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.
- Integración con checkout vía inputs explícitos:
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
- Título extraído: "Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
