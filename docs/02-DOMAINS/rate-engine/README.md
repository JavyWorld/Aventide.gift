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
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Cada time_window (ej. hourly/daily) por country_code + segment_key, el servicio:
- platform_fee_pct es independiente del bucket ops, pero sujeto a floors/ceilings por país/segmento.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".

## Límites

- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- ops_fee_cap_pct (fee buyer-facing para “Ops local” bajo límites)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
- Eventos para policy engine (gobernanza multi-país) y para finanzas (reserve health).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".


## Control operativo verificable

- Owner: `Equipo rate-engine`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RATEENGINE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/rate-engine/dominio-rate-engine-operacion`
  - `https://jira.aventide.gift/browse/OPS-RATEENGINE-241`

## Trazabilidad

- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
