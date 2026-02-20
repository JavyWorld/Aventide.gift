# DATA_CONTRACTS · memory

## Entidades y campos
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- campos marcados como privados,
- ADMIN/OPS: configura taxonomía/validadores por país (categorías, tallas, campos permitidos).
- DataClassGuard: campos sensibles (alergias, notas privadas) requieren scopes estrictos.
- PrivacyGuard: por defecto no compartir nada con sellers; solo campos explícitamente marcados “shareable”.
- Si el buyer marca un campo como “shareable”, solo se comparte en contextos definidos (p. ej. “mensaje en tarjeta”); nunca alergias o notas privadas.
- Todo campo es private_by_default.
- “Shareable” debe ser explícito por campo (whitelist).

## Constraints y claves de negocio
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- GIFT_HISTORY_ADDED idempotente por (buyer_id, order_id) (si 1 recipient por orden).
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- REMINDER_DUE idempotente por (reminder_id, fire_at).
- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`
