# EVENT_CONTRACTS · security

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- 7) Eventos y triggers + idempotencia
- 7.1 Eventos mínimos de seguridad
- Webhooks: dedupe por provider_event_id + firma + ventana temporal.
- Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado
- Fuente de verdad: “Sistema de Seguridad (Aventide Gift)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Objetivos:
- Reducir fraude (compras falsas, no-entregado, colusión buyer/seller, abuso de refunds).

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
