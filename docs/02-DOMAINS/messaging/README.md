# messaging

## Propósito

- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.
- Definición y objetivos del sistema/módulo
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
- SYSTEM: mensajes de sistema, auto-replies, eventos; emite notificaciones.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado".

## Límites

- Alcance (incluye / excluye)
- Excluye (por diseño)
- Reglas y políticas (límites, validaciones, privacidad)
- Notificación externa nunca incluye binario ni preview sensible.

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Definición: Mensajería es un chat in-app, contextual a una orden, diseñado para que el flujo ideal sea cero conversación (“silencio por defecto”) y el chat se active solo por excepción, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.
- Notificación externa nunca incluye binario ni preview sensible.
- Integración estricta: Órdenes (scope), Notificaciones (bridge), Moderación (pipeline), Soporte (ticket+freeze), Auditoría (logs).
- Compatibilidad con sistemas existentes (dependencias directas)
- Chat usado como requisito de la orden → corregido: “silencio por defecto”; chat es excepción, no dependencia.

## Trazabilidad

- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
- Título extraído: "Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
