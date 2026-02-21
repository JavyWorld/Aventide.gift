# reputation-buyer

## Propósito

- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Sistema que calcula un Buyer Trust Score (0–100) y lo expone al seller como Trust Level + Trust Badge (semi-visible) para equilibrar privacidad (incl. “Admirador Secreto”) con seguridad operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
- Buyer Reviews (reviews_buyer) como insumo de integridad (no “rating público” del buyer).
- Integridad de reviews (buyer)
- violaciones moderación⇒ baja review_integrity_score, puede poner review_hold temporal y envía CHAT_FLAGGED/MODERATION_ACTION como señales.
- Título extraído: "Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado".

## Límites

- SYSTEM/BOT: calcula score, aplica fricción y límites, genera eventos, mantiene historial.
- Integración consistente con Órdenes, Disputas, Moderación y Búsqueda: el score define fricción inteligente y límites (no mueve dinero directamente).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Acciones por nivel: límites de cancelación tardía, fricción adicional en alto valor, hold de reviews si riesgo, verificación adicional, suspensión por chargebacks.

## Dependencias

- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Integración consistente con Órdenes, Disputas, Moderación y Búsqueda: el score define fricción inteligente y límites (no mueve dinero directamente).
- Motor completo de Moderación (solo integración).


## Control operativo verificable

- Owner: `Equipo reputation-buyer`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REPUTATIONBU-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reputation-buyer/dominio-reputation-buyer-operacion`
  - `https://jira.aventide.gift/browse/OPS-REPUTATIONBU-241`

## Trazabilidad

- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
- Título extraído: "Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
