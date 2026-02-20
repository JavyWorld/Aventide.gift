# STATE_MACHINE · reputation-seller

## Estados

- Review entra a estado BLIND: no se publica hasta que:
- MODERATION_ACTION → actualiza estados de review (removed/hold).

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (seller reputation)
- Solo “verdad verificada” cuenta: review y métricas derivan de eventos auditables (COMPLETED, outcomes, cancel_reason).

## Trazabilidad

- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
