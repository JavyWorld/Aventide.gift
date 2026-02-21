# STATE_MACHINE · platform-structure

## Estados

- /orders (máquina de estados)
- Core registra intención/estado → workers llaman proveedor → webhooks confirman → handler reconcilia “observed vs expected” → transición de estados (ej. PAID_IN_ESCROW).

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end estructurales (plumbing obligatorio)
- Rutas de Studio + flujo draft→preview→publish + time machine + rollback con auditoría completa.
- Core registra intención/estado → workers llaman proveedor → webhooks confirman → handler reconcilia “observed vs expected” → transición de estados (ej. PAID_IN_ESCROW).
- Emisión confiable de eventos por transiciones (Outbox Pattern) para notificaciones/analítica/workers y trazabilidad del “money journey”.

## Triggers

- Eventos y triggers (estructura de integración)
- Emisión confiable de eventos por transiciones (Outbox Pattern) para notificaciones/analítica/workers y trazabilidad del “money journey”.
- POST /api/v1/webhooks/:provider/... verifica firma, persiste payload raw, dedupe, responde 200 rápido, encola job con trace_id/dedupe_key.
- Tabla idempotency_keys para endpoints críticos; dedupe de webhooks por provider_event_id + firma + ventana.


## Control operativo verificable

- Owner: `Equipo platform-structure`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PLATFORMSTRU-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/platform-structure/dominio-platform-structure-operacion`
  - `https://jira.aventide.gift/browse/OPS-PLATFORMSTRU-241`

## Trazabilidad

- Documento origen: `estructura-v2-260207_1049.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
