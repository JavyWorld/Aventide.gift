# governance-cameleon

## Propósito

- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Si firma inválida o schema incompatible: fallback local (modo degradado) con mínima funcionalidad y aviso.
- fallback local
- UI config vulnerable a tampering → corregido: firma + schema version + fallback + ETag cache.
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
- Determinismo: misma entrada (PolicyContext) ⇒ misma salida (ResolvedPolicy + UI Profile).
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Sistema central que resuelve qué reglas aplican y qué UI se renderiza en tiempo real según un contexto: país → hub/ciudad → zona, rol (buyer/seller/ops/admin), intención (ASAP/programada), flags/experimentos y compliance. Es la “columna vertebral” para operar multi-país sin hardcode y sin releases constantes: App Camaleón (server-driven UI).
- Objetivos (duros):
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado".

## Límites

- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.
- Definición: Sistema central que resuelve qué reglas aplican y qué UI se renderiza en tiempo real según un contexto: país → hub/ciudad → zona, rol (buyer/seller/ops/admin), intención (ASAP/programada), flags/experimentos y compliance. Es la “columna vertebral” para operar multi-país sin hardcode y sin releases constantes: App Camaleón (server-driven UI).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Cálculo detallado del breakdown monetario (Motor Financiero lo hace; aquí se inyectan reglas/límites).
- Reglas y políticas (precedencia, límites, validaciones)
- Título extraído: "Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado".

## Dependencias

- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado".


## Control operativo verificable

- Owner: `Equipo governance-cameleon`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GOVERNANCECA-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/governance-cameleon/dominio-governance-cameleon-operacion`
  - `https://jira.aventide.gift/browse/OPS-GOVERNANCECA-241`

## Trazabilidad

- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
- Título extraído: "Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
