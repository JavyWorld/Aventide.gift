# support

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- support.ticket.assign/escalate (L1+ con límites)
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias
- Integración con Trust & Safety: colusión/abuso/extorsión, moderación de reseñas conflictivas.
- EvidenceGuard (para acciones que dependan de PoD)
- Dependencia crítica (no duplicar): financial_snapshot_locked de la orden se referencia por order_id y es el input determinista del cálculo.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- 11) Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
- Título extraído: "Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado".
