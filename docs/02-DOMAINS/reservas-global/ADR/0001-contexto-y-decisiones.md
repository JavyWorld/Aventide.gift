# ADR-0001: Contexto y decisiones clave (reservas-global)

- **Estado**: Aprobado
- **Contexto**: Definición: La Reserva Global es la “caja de último recurso” del ecosistema multi-país, implementada como una cuenta central de ledger (GLOBAL_RESERVE) que actúa como Layer 3 del Waterfall de pérdidas. Solo entra cuando Country Reserve y COL Liability no alcanzan, y cuando entra, crea automáticamente una obligación de recuperación contra el COL vía GLOBAL_RECOVERY_RECEIVABLE_{country} + recovery_account (set-off sobre earnings futuros), con guardrails.

## Decisiones
- Definición: La Reserva Global es la “caja de último recurso” del ecosistema multi-país, implementada como una cuenta central de ledger (GLOBAL_RESERVE) que actúa como Layer 3 del Waterfall de pérdidas. Solo entra cuando Country Reserve y COL Liability no alcanzan, y cuando entra, crea automáticamente una obligación de recuperación contra el COL vía GLOBAL_RECOVERY_RECEIVABLE_{country} + recovery_account (set-off sobre earnings futuros), con guardrails.
- Controles de crisis: detección de insuficiencia, EMERGENCY_ESCALATION, freeze parcial, restricción de métodos de pago riesgosos, comité.
- aplica guardrails: floor de ops_lead_earn_pct, cap de recorte diario (max_daily_delta_bps), horizonte máximo.
- restringir métodos de pago de alto riesgo,
- 5.4 Guardrails de recovery
- SAFE_RECOVERY mode y “risk freeze” si sube riesgo.

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
