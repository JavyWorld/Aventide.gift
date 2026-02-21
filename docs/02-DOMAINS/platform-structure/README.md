# platform-structure

## Propósito

- Client Camaleón: boot config, ETag, firma, fallback, modo degradado.
- Camaleón (Server-driven UI) boot + caching + fallback + hot reload
- Documento origen: `estructura-v2-260207_1049.docx`
- Service actors: workers/webhooks corren con service_id para trazabilidad/auditoría.
- Pagos: Rapyd (sessions por country_code, wallets/escrow, payouts + webhooks).
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Título extraído: "Estructura v2.0 (Estructura del Proyecto / Plataforma Aventide Gift)".

## Límites

- Un core único (misma API/reglas/datos) para web+mobile+paneles.
- Multi-país/territorio como “primera clase” en requests, UI, reglas, búsqueda, pagos, auditoría y analítica.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Regional OS incluye Studio para operar config/UI/merchandising bajo guardrails y auditoría.
- Alcance

## Dependencias

- contratos transversales (territorio como first-class, policy engine, RBAC+scopes, server-driven UI, auditoría WORM, pipeline de dinero),
- Backend operable: /api/v1, Postgres+PostGIS, Redis+colas, S3 WORM, gateway de webhooks, workers con DLQ/retries/backoff, observabilidad base.
- Core registra intención/estado → workers llaman proveedor → webhooks confirman → handler reconcilia “observed vs expected” → transición de estados (ej. PAID_IN_ESCROW).
- Eventos y triggers (estructura de integración)
- Separación explícita Client / Server / Integraciones para evitar acoplamientos peligrosos (especialmente dinero).
- Plano asíncrono obligatorio (BullMQ/workers) para integraciones y procesos críticos.


## Control operativo verificable

- Owner: `Equipo platform-structure`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PLATFORMSTRU-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/platform-structure/dominio-platform-structure-operacion`
  - `https://jira.aventide.gift/browse/OPS-PLATFORMSTRU-241`

## Trazabilidad

- Documento origen: `estructura-v2-260207_1049.docx`
- Título extraído: "Estructura v2.0 (Estructura del Proyecto / Plataforma Aventide Gift)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
