# ADR-0001: Contexto y decisiones clave (rate-engine)

- **Estado**: Aprobado
- **Contexto**: lo que se distribuye internamente (platform fee, payout al Country Ops Lead y Reserva Nacional por país) dentro de guardrails.

## Decisiones
- lo que se distribuye internamente (platform fee, payout al Country Ops Lead y Reserva Nacional por país) dentro de guardrails.
- Maximizar margen neto esperado, no revenue bruto, incorporando costos externos, earned schedule, créditos/loyalty y riesgo.
- Guardrails: floors/ceilings, max delta, min samples, safe-mode, last-known-good.
- GuardrailGuard (floors/ceilings, max delta, min samples, safe-mode)
- 4.1 Decisión de rates por ventana (Rate Decision Service)
- obtiene features/rollups de riesgo y margen,

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
