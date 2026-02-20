# ADR-0001: Contexto y decisiones clave (audit)

- **Estado**: Aprobado
- **Contexto**: Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado

## Decisiones
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- Objetivos (no negociables):
- WORM/append-only: un registro de auditoría nunca se edita ni se borra.

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
