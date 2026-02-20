# ADR-0001: Contexto y decisiones clave (backup)

- **Estado**: Aprobado
- **Contexto**: Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado

## Decisiones
- Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado
- Fuente de verdad: “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Objetivos (duros):
- Backups verificables (no “backups que nunca se prueban”).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
