# disputes

## Propósito

- disputes.evidence.request/read/write
- disputes.finance.approval.request / disputes.finance.approval.grant
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Documento origen: `disputas-260207_0809.docx`
- disputes.saga.execute (system)
- Pagos/Escrow/Provider
- Título extraído: "Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado".

## Límites

- Reglas fiscales específicas de cada país (se delegan a Facturación & Documentos, invocadas por evento).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Reglas y políticas (límites, validaciones, caps, invariantes)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Orquestación Saga: refund, release/clawback, ledger adjustments, docs adjustments, trust/loyalty updates.
- SYSTEM/BOT: ejecuta saga, integra con provider, ledger, docs, trust, loyalty.


## Control operativo verificable

- Owner: `Equipo disputes`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-DISPUTES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/disputes/dominio-disputes-operacion`
  - `https://jira.aventide.gift/browse/OPS-DISPUTES-241`

## Trazabilidad

- Documento origen: `disputas-260207_0809.docx`
- Título extraído: "Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
