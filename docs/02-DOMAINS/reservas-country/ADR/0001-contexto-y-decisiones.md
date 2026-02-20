# ADR-0001: Contexto y decisiones clave (reservas-country)

- **Estado**: Aprobado
- **Contexto**: “waterfall-engine-v10-260207_0941” (Waterfall de pérdidas, layers, loss_case, recovery al COL, guardrails, ledger doble-entry).

## Decisiones
- “waterfall-engine-v10-260207_0941” (Waterfall de pérdidas, layers, loss_case, recovery al COL, guardrails, ledger doble-entry).
- Recibe automáticamente el diferencial / bucket destinado a operación país cuando aplica (p.ej., vacancia de COL o decisiones de riesgo/policy).
- Riesgo: absorber pérdidas locales (chargebacks, fraude, refunds irreversibles, penalidades atribuibles a operación país si policy lo admite) con orden fijo y trazabilidad.
- Si Global cubre parte: se crea recovery_account y se activa Recovery Engine (recuperación obligatoria al COL vía recorte de earnings, con guardrails).
- Cobertura de riesgo (chargebacks/fraude/refunds irreversibles) a través de Waterfall.
- 5.4 Guardrails de recovery (protección del país y anti-colapso)

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
