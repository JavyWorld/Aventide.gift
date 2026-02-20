# RUNBOOKS · internal-credit

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas mínimas
- Spike en wallet_mint_total{source_type=SUPPORT_OUTCOME} (posible problema de calidad/operación)
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Definición y objetivos del sistema/módulo

## Incidentes, rollback y backfill
- Reintentos/redoble click: no duplica spend (idempotencia por checkout_id).
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Definición y objetivos del sistema/módulo
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Objetivos:
- Eliminar incoherencia “crédito genérico”: wallets separadas por tipo con reglas duras.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
