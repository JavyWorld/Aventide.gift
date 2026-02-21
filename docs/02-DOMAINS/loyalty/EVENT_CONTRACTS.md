# EVENT_CONTRACTS · loyalty

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”
- Backend aplica FS con clamp duro:fs_applied = min(fs_balance_available, platform_fee_amount)y genera evento FEE_CREDIT_APPLIED (max_applied = platform_fee_amount).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- No reversión ante refund/chargeback → corregido: eventos REVOKED/ajuste negativo y bloqueo según policy país.
- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos”
- Integración obligatoria con Disputas/Refunds (reversión)
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Lealtad es un sistema de incentivos para buyers basado en dos monedas:


## Control operativo verificable

- Owner: `Equipo loyalty`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-LOYALTY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/loyalty/dominio-loyalty-operacion`
  - `https://jira.aventide.gift/browse/OPS-LOYALTY-241`

## Trazabilidad
- Documento origen: `sistema-de-lealtad-260207_0817.docx`
