# messaging

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye (por diseño)
- 5) Reglas y políticas (límites, validaciones, privacidad)
- Notificación externa nunca incluye binario ni preview sensible.

## Dependencias
- Integración estricta: Órdenes (scope), Notificaciones (bridge), Moderación (pipeline), Soporte (ticket+freeze), Auditoría (logs).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Plantillas dependen del estado de orden (IN_TRANSIT, DELIVERED, etc.).
- 11) Compatibilidad con sistemas existentes (dependencias directas)
- Chat usado como requisito de la orden → corregido: “silencio por defecto”; chat es excepción, no dependencia.

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
- Título extraído: "Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado".
