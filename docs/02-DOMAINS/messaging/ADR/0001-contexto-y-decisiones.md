# ADR-0001: Contexto y decisiones clave (messaging)

- **Estado**: Aprobado
- **Contexto**: Chat global sin contexto (riesgo fraude/acoso) → eliminado: solo order-scoped.

## Decisiones
- Chat global sin contexto (riesgo fraude/acoso) → eliminado: solo order-scoped.
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Mensajería es un chat in-app, contextual a una orden, diseñado para que el flujo ideal sea cero conversación (“silencio por defecto”) y el chat se active solo por excepción, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.
- Objetivos (duros):

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
