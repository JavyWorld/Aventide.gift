# coverage

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- Distancia cercana al límite (99–101%): registrar para auditoría “near_limit”.
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias
- Integración con Búsqueda (ST_DWithin) y Ordenes (snapshot logístico).
- Scheduler de slots/capacidad (solo dependencia; Coverage decide si llega o no).
- geocode_provider_meta (place_id, confidence)
- Calcula distancia distance_meters (Haversine; o ruta si se integra).
- geocode_provider_meta

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
- Título extraído: "Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado".
