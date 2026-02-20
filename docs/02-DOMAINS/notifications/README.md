# notifications

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (prioridades, canales, límites, validaciones)
- Corrección de incoherencia: los límites se aplican en el Orchestrator (no en cada servicio de dominio) para que el enforcement sea único.

## Dependencias
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Un servicio de dominio (Órdenes/Pagos/Disputas) ejecuta su transacción.
- Corrección de incoherencia: los límites se aplican en el Orchestrator (no en cada servicio de dominio) para que el enforcement sea único.
- 6.1 outbox_events (por servicio de dominio)
- provider

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
- Título extraído: "Sistema de Notificaciones v2.0 (Notification Center + Inbox) — corregido y unificado".
