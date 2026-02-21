# INVARIANTS · rate-engine

Reglas no negociables del dominio:
- Definición: Motor único que gobierna, de forma dinámica, determinista y auditable, todos los porcentajes (rates) que impactan el dinero de una orden, separando estrictamente:
- No retroactividad: cambios de rates solo afectan órdenes futuras.
- Ledger split determinístico:
- Auditoría WORM-style de decisiones, cambios, aprobaciones y órdenes afectadas por ventana temporal.
- FINANCE/AUDIT/LEGAL: lectura de auditoría, reconciliación, export.
- rates.decision.read (finance/audit)
- DeterminismGuard (misma entrada → mismo RateVector)
- AuditGuard (append-only: decisiones y cambios)
- 4.2 Checkout: resolver breakdown + snapshot (no retroactividad)
- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).


## Control operativo verificable

- Owner: `Equipo rate-engine`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RATEENGINE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/rate-engine/dominio-rate-engine-operacion`
  - `https://jira.aventide.gift/browse/OPS-RATEENGINE-241`

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
