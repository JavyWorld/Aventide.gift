# ADR-0001: Contexto y decisiones clave (notifications)

- **Estado**: Aprobado
- **Contexto**: Guardrails editor de plantillas por Ops Lead (localización sin tocar código, con whitelist de variables + versioning + rollback).

## Decisiones
- Guardrails editor de plantillas por Ops Lead (localización sin tocar código, con whitelist de variables + versioning + rollback).
- 5.7 Guardrails de plantillas (no permitir “inventar”)
- Sistema de Notificaciones v2.0 (Notification Center + Inbox) — corregido y unificado
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
