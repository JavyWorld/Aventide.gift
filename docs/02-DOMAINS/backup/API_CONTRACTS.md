# API_CONTRACTS · backup

## Endpoints y auth
- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- Reconciliación contra Rapyd/webhooks:
- Regla extra: restore idempotente (sin duplicar cobros/payouts).
- 7) Eventos y triggers (colas/jobs) + idempotencia
- Idempotencia
- Cada job escribe run_id y es idempotente por (resource_type, schedule_window, country_code).

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado
- Fuente de verdad: “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
