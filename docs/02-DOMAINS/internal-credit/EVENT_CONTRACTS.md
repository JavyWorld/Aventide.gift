# EVENT_CONTRACTS · internal-credit

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Definición y objetivos del sistema/módulo
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Objetivos:
- Eliminar incoherencia “crédito genérico”: wallets separadas por tipo con reglas duras.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.
- Evitar bugs financieros: no mezclar FS/BSC/GCC; no permitir aplicar créditos a taxes/processing/ops_fee; FS solo contra platform_fee.

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
