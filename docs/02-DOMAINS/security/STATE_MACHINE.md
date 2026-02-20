# STATE_MACHINE · security

## Estados detectados/derivados
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- 4) Flujos end-to-end (happy path + edge cases)
- 4.2 Entrega segura — Tridente (flujo core)
- Estado e idempotencia: solo ejecuta si la orden está en estado correcto; evita dobles confirmaciones.
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- 6.4 Estado de cuenta para borrado/archivo

## Transiciones y eventos de entrada/salida
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- SYSTEM/BOT (workers, webhook handlers).
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- PIN deshabilitado; se valida por tracking del courier y PoD externo por webhook.
- 7) Eventos y triggers + idempotencia
- 7.1 Eventos mínimos de seguridad
- payments.webhook_received/deduped/invalid_signature
- Webhooks: dedupe por provider_event_id + firma + ventana temporal.

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
