# ADR-0001: Contexto y decisiones clave (internal-credit)

- **Estado**: Aprobado
- **Contexto**: flags de riesgo ⇒ bloquear FS X días (policy país)

## Decisiones
- flags de riesgo ⇒ bloquear FS X días (policy país)
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Definición y objetivos del sistema/módulo
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Objetivos:

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
