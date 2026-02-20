# EVENT_CONTRACTS · users

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Usuarios
- Entrega/Tridente: identidad del evento de entrega ligada a evidencia; confirmación robusta.
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- Autorización estricta por claims y middleware (no por UI).
- Contexto geo-operativo consistente: Seller estático por “sorting hat” y Buyer dinámico por “Entregar en…”.

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
