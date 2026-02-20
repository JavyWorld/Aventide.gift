# ADR-0001: Contexto y decisiones clave (reputation-buyer)

- **Estado**: Aprobado
- **Contexto**: Definición: Sistema que calcula un Buyer Trust Score (0–100) y lo expone al seller como Trust Level + Trust Badge (semi-visible) para equilibrar privacidad (incl. “Admirador Secreto”) con seguridad operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.

## Decisiones
- Definición: Sistema que calcula un Buyer Trust Score (0–100) y lo expone al seller como Trust Level + Trust Badge (semi-visible) para equilibrar privacidad (incl. “Admirador Secreto”) con seguridad operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.
- Acciones por nivel: límites de cancelación tardía, fricción adicional en alto valor, hold de reviews si riesgo, verificación adicional, suspensión por chargebacks.
- Retener PIN sistemáticamente ⇒ penalización alta (riesgo extorsión/fraude).
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
