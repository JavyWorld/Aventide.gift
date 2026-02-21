# integrations

## Propósito

- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
- SYSTEM/WORKERS: ejecutan jobs y procesan webhooks.
- integrations.webhooks.raw.read (support/finance; auditado)
- Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado
- Título extraído: "Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado".

## Límites

- El Core decide (lógica, estados, políticas).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).
- Un pool de Workers asíncronos ejecuta llamadas externas y procesa confirmaciones vía Webhooks.
- No bloquear UX: llamadas externas críticas nunca se ejecutan en request síncrono (salvo validate liviano).
- Adapters por proveedor: PaymentsProvider, MessagingProvider, MapsProvider, StorageProvider + WebhookVerifier.
- Integration Registry por país y tipo: qué proveedor está activo, timeouts, rate limits, retry policy y secrets refs.
- Proveedor caído: circuit breaker → job a retry con backoff; si excede, DLQ + alerta.
- Duplicados por retry del proveedor: dedupe responde OK sin repetir efectos.
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
- Worker de webhook normaliza payload a evento interno y actualiza “observed vs expected” del ledger.
- Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado
- Evitar “conectar Operación definida y validada con Operación definida y validada”: integraciones pasan por registry + adapters + workers.
- Título extraído: "Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado".


## Control operativo verificable

- Owner: `Equipo integrations`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-INTEGRATIONS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/integrations/dominio-integrations-operacion`
  - `https://jira.aventide.gift/browse/OPS-INTEGRATIONS-241`

## Trazabilidad

- Documento origen: `sistema-de-integraciones-260207_0951.docx`
- Título extraído: "Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
