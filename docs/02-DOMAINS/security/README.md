# security

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)
- Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado

## Dependencias
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Perímetro (WAF/DDoS/CDN + rate limiting) y seguridad de API (gateway).
- Integración con Observabilidad como “capa de detección” (SIEM + alertas).
- Webhooks: dedupe por provider_event_id + firma + ventana temporal.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
- Título extraído: "Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado".
