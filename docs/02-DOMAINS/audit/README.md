# audit

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- GET /audit/certificate/order/:order_id genera PDF/CSV con timeline:Creación → Pago → Chats → Intentos de entrega → PIN → Liberación de fondosIncluye hash de integridad del documento y referencias a evidencias.

## Dependencias
- audit.write (solo servicios; no humanos)
- Servicio de dominio ejecuta acción (ej. update de price, payout, role change).
- GET /audit/certificate/order/:order_id genera PDF/CSV con timeline:Creación → Pago → Chats → Intentos de entrega → PIN → Liberación de fondosIncluye hash de integridad del documento y referencias a evidencias.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- 11) Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
- Título extraído: "Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado".
