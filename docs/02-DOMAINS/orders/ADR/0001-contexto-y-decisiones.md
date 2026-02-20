# ADR-0001: Contexto y decisiones clave (orders)

- **Estado**: Aprobado
- **Contexto**: Motor de reembolsos/decisión: Soporte/Disputas decide outcomes; Órdenes ejecuta transiciones y bloqueos.

## Decisiones
- Motor de reembolsos/decisión: Soporte/Disputas decide outcomes; Órdenes ejecuta transiciones y bloqueos.
- escalar a soporte/ops para decisión (cancelar o reasignar por policy).
- Si vence accept_by: evento + notificación + escalamiento a ops/soporte.Suposición: la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.
- 1) Definición y objetivos del sistema/módulo

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
