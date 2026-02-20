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

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
