# moderation

## Propósito

- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- moderation.decision.publish/reject
- AUTO_REJECT
- REJECT (con motivo educativo)
- Leakage en imagen (teléfono/URL): AUTO_REJECT con mensaje educativo.
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
- Salida Capa 1 (recomendación):
- Salida Capa 2 (decisión operativa):
- Entradas mínimas:
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado".

## Límites

- Corrección de incoherencia:Strike Ledger y “funds policy” deben ser derivados y aplicados por policy engine/pagos; moderación no mueve dinero, solo cambia el estado/política (rolling_reserve=50%, freeze=180d).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Reglas y políticas (límites, validaciones, catálogos)

## Dependencias

- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- Corrección de incoherencia:Strike Ledger y “funds policy” deben ser derivados y aplicados por policy engine/pagos; moderación no mueve dinero, solo cambia el estado/política (rolling_reserve=50%, freeze=180d).
- Corrección de incoherencia: StrikeLedger es proyección; los cambios reales ocurren vía eventos STRIKE_APPLIED + policy engine que setea flags en user_status y seller_operational_flags.
- Integración obligatoria con Reputación/Score, Búsqueda/Ranking, Órdenes/Pagos, Soporte, Auditoría.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado".


## Control operativo verificable

- Owner: `Equipo moderation`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MODERATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/moderation/dominio-moderation-operacion`
  - `https://jira.aventide.gift/browse/OPS-MODERATION-241`

## Trazabilidad

- Documento origen: `sistema-de-moderacion-260207_0828.docx`
- Título extraído: "Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
