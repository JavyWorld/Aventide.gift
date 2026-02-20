# STATE_MACHINE · users

## Estados detectados/derivados
- Estados de cuenta + suspensión/restricción + borrado diferenciado.
- 4) Flujos end-to-end (happy path + edge cases)
- Estado PENDING_APPROVAL y revisión por Ops Lead (Kanban).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Usuarios
- RBAC changes, overrides, impersonation, cambios de estado de cuenta y borrado → append-only.

## Transiciones y eventos de entrada/salida
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Usuarios
- Entrega/Tridente: identidad del evento de entrega ligada a evidencia; confirmación robusta.
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
