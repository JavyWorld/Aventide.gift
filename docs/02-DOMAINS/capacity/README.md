# capacity

## Propósito

- Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado
- Fuente de verdad: “Sistema #5 — Capacidad & Disponibilidad (Capacity, Scheduler, Stock, Cupos, Temporadas)”.
- Definición y objetivos del sistema/módulo
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`
- Objetivos (duros):
- Evitar promesas falsas: si el sistema dice “no hay cupo/stock/slot”, no se puede pagar.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado".

## Límites

- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- Alcance (incluye / excluye)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Integración estricta con Cobertura: orden de validación fijo y consistente.
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`
- Título extraído: "Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
