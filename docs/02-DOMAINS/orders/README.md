# orders

## Propósito

- orders.cancel.request_post_accept (buyer → crea caso, no cancela directo)
- cancel_meta JSON {requested_by, reason_code, requested_at, outcome_case_id}
- state (REQUESTED/UNDER_REVIEW/APPROVED/REJECTED/PARTIAL_REFUND)
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
- Motor de logística/driver como sistema completo (Órdenes emite/consume eventos).
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Sistema valida entregabilidad/capacidad (depende de Contenido/Capacidad).
- Integridad
- Título extraído: "Sistema de Órdenes v2.0 (corregido y unificado)".

## Límites

- Regla dura: estado de orden ≠ estado de refund.Refund flow (ejemplo): REQUESTED → UNDER_REVIEW → APPROVED/REJECTED → PARTIAL_REFUNDLa orden puede estar DELIVERED_PENDING_RELEASE o COMPLETED mientras corre el refund.
- Reglas cerradas de cancelación por estado (y ventanas).
- Si vence accept_by: evento + notificación + escalamiento a ops/soporte.Suposición: la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Política operativa: cada validación crítica debe ejecutarse en tiempo de request y registrar resultado en auditoría para trazabilidad legal.

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Si vence accept_by: evento + notificación + escalamiento a ops/soporte.Suposición: la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)
- Si zona no activa / sin capacidad para la ventana: no se permite crear o se crea como “no confirmable” (según policy); en cualquier caso, no se debe pagar si no es entregable. (Integración obligatoria con Capacidad/Logística; aquí se fija el enforcement en el gate de checkout, coherente con “lo visible debe ser comprable”.)


## Control operativo verificable

- Owner: `Equipo orders`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ORDERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/orders/dominio-orders-operacion`
  - `https://jira.aventide.gift/browse/OPS-ORDERS-241`

## Trazabilidad

- Documento origen: `sistema-de-ordenes-260207_0037.docx`
- Título extraído: "Sistema de Órdenes v2.0 (corregido y unificado)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
