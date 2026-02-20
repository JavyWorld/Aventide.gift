# RUNBOOKS · memory

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- 1) Definición y objetivos del sistema/módulo
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.

## Incidentes, rollback y backfill
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- 1) Definición y objetivos del sistema/módulo
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.
- Objetivos (duros):
- Reuso: reducir fricción en compras repetidas (cumples, aniversarios, Navidad).

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`
