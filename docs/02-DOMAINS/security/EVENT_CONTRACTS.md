# EVENT_CONTRACTS · security

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- 7) Eventos y triggers + idempotencia
- 7.1 Eventos mínimos de seguridad
- Webhooks: dedupe por provider_event_id + firma + ventana temporal.
- Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado
- Fuente de verdad: “Sistema de Seguridad (Aventide Gift)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Objetivos:
- Reducir fraude (compras falsas, no-entregado, colusión buyer/seller, abuso de refunds).


## Control operativo verificable

- Owner: `Equipo security`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SECURITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/security/dominio-security-operacion`
  - `https://jira.aventide.gift/browse/OPS-SECURITY-241`

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
