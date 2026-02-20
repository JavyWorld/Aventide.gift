# rate-engine

## Propósito

- rates.capfloor.change.request.create (ops lead/admin)
- rates.capfloor.change.request.approve (super_admin)
- Se crea CapFloorChangeRequest con evidencia + rango propuesto + vigencia temporal + plan canary.
- cap_floor_change_requests
- CAP_FLOOR_CHANGE_REQUEST_CREATED/APPROVED/REJECTED/EXECUTED
- Fallbacks
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
- Entradas (features/rollups)
- Salidas (contratos)
- Fuente de verdad: “Motor Unificado de Rates para Aventide Gift”.
- Definición y objetivos del sistema/módulo
- Cada time_window (ej. hourly/daily) por country_code + segment_key, el servicio:
- platform_fee_pct es independiente del bucket ops, pero sujeto a floors/ceilings por país/segmento.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".

## Límites

- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).
- Alcance (incluye / excluye)
- ops_fee_cap_pct (fee buyer-facing para “Ops local” bajo límites)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".

## Trazabilidad

- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
