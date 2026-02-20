# EVENT_CONTRACTS · governance-cameleon

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema central que resuelve qué reglas aplican y qué UI se renderiza en tiempo real según un contexto: país → hub/ciudad → zona, rol (buyer/seller/ops/admin), intención (ASAP/programada), flags/experimentos y compliance. Es la “columna vertebral” para operar multi-país sin hardcode y sin releases constantes: App Camaleón (server-driven UI).
- Objetivos (duros):
- Determinismo: misma entrada (PolicyContext) ⇒ misma salida (ResolvedPolicy + UI Profile).
- Precedencia única para evitar contradicciones (cascada oficial).
- Snapshot inmutable de todo lo que afecte dinero/validaciones en la orden (pasado no cambia).

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
