# RUNBOOKS · audit

## Operación
- Alerta por escalada inusual (ej. finanzas a soporte).
- Índices mínimos (operación real):
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.

## Incidentes, rollback y backfill
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Objetivos (no negociables):
- WORM/append-only: un registro de auditoría nunca se edita ni se borra.
- Snapshotting: demostrar cómo era algo antes de cambios (precio/fotos/listing).
- Atribución estricta: no existen acciones “anónimas” del sistema: siempre User_ID o Service_ID.

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
