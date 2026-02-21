# EVENT_CONTRACTS · internal-credit

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Objetivos:
- Eliminar incoherencia “crédito genérico”: wallets separadas por tipo con reglas duras.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.
- Evitar bugs financieros: no mezclar FS/BSC/GCC; no permitir aplicar créditos a taxes/processing/ops_fee; FS solo contra platform_fee.


## Control operativo verificable

- Owner: `Equipo internal-credit`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-INTERNALCRED-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/internal-credit/dominio-internal-credit-operacion`
  - `https://jira.aventide.gift/browse/OPS-INTERNALCRED-241`

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
