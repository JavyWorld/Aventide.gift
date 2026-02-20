# EVENT_CONTRACTS · backup

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Analítica: warehouse/event store (si existe) con RPO/RTO distinto.
- 7) Eventos y triggers (colas/jobs) + idempotencia
- Eventos mínimos
- Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado
- Fuente de verdad: “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.
- 1) Definición y objetivos del sistema/módulo
- Objetivos (duros):
- Backups verificables (no “backups que nunca se prueban”).
- RPO/RTO por criticidad (tiers) y por país (policy engine).

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
