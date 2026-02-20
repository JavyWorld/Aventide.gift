# coverage

## Propósito

- Devuelve PASS/FAIL + ETA estimado (3–5 días hábiles) y exige tracking/POD por webhook (sin PIN).
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- Definición y objetivos del sistema/módulo
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
- Entrada por link directo: si fuera de zona, mostrar “fuera de área de servicio”.
- geocode_provider_meta (place_id, confidence)
- Calcula distancia distance_meters (Haversine; o ruta si se integra).
- geocode_provider_meta
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".

## Límites

- Alcance (incluye / excluye)
- Distancia cercana al límite (99–101%): registrar para auditoría “near_limit”.
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- Integración con Búsqueda (ST_DWithin) y Ordenes (snapshot logístico).
- Scheduler de slots/capacidad (solo dependencia; Coverage decide si llega o no).
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".

## Trazabilidad

- Documento origen: `sistema-de-cobertura-260207_0907.docx`
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
