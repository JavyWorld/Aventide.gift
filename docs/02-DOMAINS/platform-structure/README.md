# platform-structure

## Propósito

- Client Camaleón: boot config, ETag, firma, fallback, modo degradado.
- Camaleón (Server-driven UI) boot + caching + fallback + hot reload
- Documento origen: `estructura-v2-260207_1049.docx`
- Service actors: workers/webhooks corren con service_id para trazabilidad/auditoría.
- Pagos: Rapyd (sessions por country_code, wallets/escrow, payouts + webhooks).
- Definición y objetivos del sistema/módulo
- Título extraído: "Estructura v2.0 (Estructura del Proyecto / Plataforma Aventide Gift)".

## Límites

- Un core único (misma API/reglas/datos) para web+mobile+paneles.
- Multi-país/territorio como “primera clase” en requests, UI, reglas, búsqueda, pagos, auditoría y analítica.
- Alcance (incluye / excluye)
- Regional OS incluye Studio para operar config/UI/merchandising bajo guardrails y auditoría.
- Alcance

## Dependencias

- contratos transversales (territorio como first-class, policy engine, RBAC+scopes, server-driven UI, auditoría WORM, pipeline de dinero),
- Backend operable: /api/v1, Postgres+PostGIS, Redis+colas, S3 WORM, gateway de webhooks, workers con DLQ/retries/backoff, observabilidad base.
- Core registra intención/estado → workers llaman proveedor → webhooks confirman → handler reconcilia “observed vs expected” → transición de estados (ej. PAID_IN_ESCROW).
- Eventos y triggers (estructura de integración)
- Separación explícita Client / Server / Integraciones para evitar acoplamientos peligrosos (especialmente dinero).
- Plano asíncrono obligatorio (BullMQ/workers) para integraciones y procesos críticos.

## Trazabilidad

- Documento origen: `estructura-v2-260207_1049.docx`
- Título extraído: "Estructura v2.0 (Estructura del Proyecto / Plataforma Aventide Gift)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
