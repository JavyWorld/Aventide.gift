# ADR-0001: Contexto y decisiones clave (payments)

- **Estado**: Aprobado
- **Contexto**: “Dinero retenido”: no sale de escrow sin entrega confirmada o decisión de disputa.

## Decisiones
- “Dinero retenido”: no sale de escrow sin entrega confirmada o decisión de disputa.
- Multi-país server-driven: allowlist métodos + torre de precios + riesgo/payout policies.
- payout/riesgo (min/max, KYC threshold, reserve),
- Payouts sin riesgo por país → corregido: cashout_min/max, KYC threshold, rolling reserve policy-driven.
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Fuente de verdad: “Sistema de Pagos — Aventide Gift”.

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
