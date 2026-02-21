# RUNBOOKS · integrations

## Operación
- Proveedor caído: circuit breaker → job a retry con backoff; si excede, DLQ + alerta.
- DLQ + alertas.
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado
- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).

## Incidentes, rollback y backfill
- Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado
- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Capa central que conecta el Core Aventide con proveedores externos (Pagos, Mensajería, Maps/Geocoding, Storage, Tax, etc.) bajo un patrón Hub & Spoke:
- El Core decide (lógica, estados, políticas).
- El Ledger/Audit registra intención y evidencia.
- Un pool de Workers asíncronos ejecuta llamadas externas y procesa confirmaciones vía Webhooks.
- Objetivos (duros):


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
