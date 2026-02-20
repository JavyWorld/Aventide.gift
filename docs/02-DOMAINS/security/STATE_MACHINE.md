# STATE_MACHINE · security

## Estados

- Estado e idempotencia: solo ejecuta si la orden está en estado correcto; evita dobles confirmaciones.
- Estado de cuenta para borrado/archivo

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Flujos end-to-end (happy path + edge cases)
- Entrega segura — Tridente (flujo core)

## Triggers

- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- Eventos y triggers + idempotencia
- Eventos mínimos de seguridad
- Webhooks: dedupe por provider_event_id + firma + ventana temporal.

## Trazabilidad

- Documento origen: `sistema-de-seguridad-260207_0756.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
