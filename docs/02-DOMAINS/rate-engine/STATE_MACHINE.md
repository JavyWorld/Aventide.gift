# STATE_MACHINE · rate-engine

## Estados

- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).

## Transiciones

- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- request_id
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).

## Trazabilidad

- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
