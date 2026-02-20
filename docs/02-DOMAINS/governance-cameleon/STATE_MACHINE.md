# STATE_MACHINE · governance-cameleon

## Estados detectados/derivados
- Determinismo: misma entrada (PolicyContext) ⇒ misma salida (ResolvedPolicy + UI Profile).
- 4) Flujos end-to-end (happy path + edge cases)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.

## Transiciones y eventos de entrada/salida
- Determinismo: misma entrada (PolicyContext) ⇒ misma salida (ResolvedPolicy + UI Profile).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema central que resuelve qué reglas aplican y qué UI se renderiza en tiempo real según un contexto: país → hub/ciudad → zona, rol (buyer/seller/ops/admin), intención (ASAP/programada), flags/experimentos y compliance. Es la “columna vertebral” para operar multi-país sin hardcode y sin releases constantes: App Camaleón (server-driven UI).
- Objetivos (duros):

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
