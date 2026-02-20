# ADR-0001: Contexto y decisiones clave (referrals)

- **Estado**: Aprobado
- **Contexto**: Chargeback → REVOKED + señales de riesgo.

## Decisiones
- Chargeback → REVOKED + señales de riesgo.
- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X E).
- 1) Definición y objetivos del sistema/módulo
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.
- Objetivos (duros):

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-referido-260207_0826.docx`
