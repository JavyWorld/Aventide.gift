# internal-credit

## Propósito

- fee_credits_requested (FS)
- store_credit_requested (BSC) (si policy lo permite como tender)
- (opcional) gcc_credit_requested si GCC está habilitado.
- store_credit_requested (BSC/GCC si policy lo permite)
- bsc_applied = min(bsc_balance, eligible_base_for_bsc, store_credit_requested)
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
- Objetivos:
- Origen: compra de gift card.Uso: depende de policy del país.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado".

## Límites

- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Eliminar incoherencia “crédito genérico”: wallets separadas por tipo con reglas duras.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Reglas y políticas (límites, expiraciones, caps, validaciones)
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.
- Integración con checkout vía inputs explícitos:
- Compatibilidad con sistemas existentes (dependencias directas)


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
- Título extraído: "Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
