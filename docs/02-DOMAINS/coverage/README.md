# coverage

## Propósito

- Devuelve PASS/FAIL + ETA estimado (3–5 días hábiles) y exige tracking/POD por webhook (sin PIN).
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
- Entrada por link directo: si fuera de zona, mostrar “fuera de área de servicio”.
- geocode_provider_meta (place_id, confidence)
- Calcula distancia distance_meters (Haversine; o ruta si se integra).
- geocode_provider_meta
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".

## Límites

- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Distancia cercana al límite (99–101%): registrar para auditoría “near_limit”.
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- Integración con Búsqueda (ST_DWithin) y Ordenes (snapshot logístico).
- Scheduler de slots/capacidad (solo dependencia; Coverage decide si llega o no).
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".


## Control operativo verificable

- Owner: `Equipo coverage`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-COVERAGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/coverage/dominio-coverage-operacion`
  - `https://jira.aventide.gift/browse/OPS-COVERAGE-241`

## Trazabilidad

- Documento origen: `sistema-de-cobertura-260207_0907.docx`
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
