# STATE_MACHINE · backup

## Estados detectados/derivados
- 4) Flujos end-to-end (happy path + edge cases)
- Lifecycle por clase (evidencia disputas > adjuntos chat).
- sanity de estados críticos (no dejar PAID sin ledger)
- 7) Eventos y triggers (colas/jobs) + idempotencia
- Eventos mínimos
- Tras restore Tier 0, reconciliar contra webhooks/estado proveedor antes de reabrir dinero.

## Transiciones y eventos de entrada/salida
- Reconciliación contra Rapyd/webhooks:
- 7) Eventos y triggers (colas/jobs) + idempotencia
- Eventos mínimos
- Tras restore Tier 0, reconciliar contra webhooks/estado proveedor antes de reabrir dinero.
- Integraciones/Pagos: reconciliación post-restore contra Rapyd/webhooks antes de reactivar dinero.
- Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado
- Fuente de verdad: “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
