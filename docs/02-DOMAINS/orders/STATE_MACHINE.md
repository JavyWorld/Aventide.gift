# STATE_MACHINE · orders

## Estados detectados/derivados
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.
- Máquina de estados estricta (no saltos).
- Reglas cerradas de cancelación por estado (y ventanas).
- “Estado manda”: ninguna acción fuera de transición válida.
- Pago y transición a escrow.
- Motor de reembolsos/decisión: Soporte/Disputas decide outcomes; Órdenes ejecuta transiciones y bloqueos.

## Transiciones y eventos de entrada/salida
- “Estado manda”: ninguna acción fuera de transición válida.
- Pago y transición a escrow.
- Motor de reembolsos/decisión: Soporte/Disputas decide outcomes; Órdenes ejecuta transiciones y bloqueos.
- Motor de logística/driver como sistema completo (Órdenes emite/consume eventos).
- StateGuard (validación de transición)
- evento “no atendida”,
- Si vence accept_by: evento + notificación + escalamiento a ops/soporte.Suposición: la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)
- from_status, to_status (nullable para eventos no estado)

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
