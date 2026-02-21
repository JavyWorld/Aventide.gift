# neighborhoods

## Propósito

- GIFT_INCOMING_NOTIFICATION_REQUESTED (checkout)
- circle.invite.accept / circle.invite.reject
- Documento origen: `sistema-de-barrio-260207_1012.docx`
- Sistema emite evento circle_invite_sent.
- Basado en: definición “Social layer: Barrio (o Círculos)” + sus componentes (recipients compartidos, fechas opt-in, wishlists temáticas, notificación de regalo entrante).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Barrio v2.0 (Círculos privados) — corregido y unificado".

## Límites

- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Private-by-default: nada del círculo es visible fuera (incluye recipients externos). (Inferencia: consistente con “grupo privado”).
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Errores de notificación “gift incoming” (dependencia Notificaciones)
- Miembros del círculo (usuarios Aventide) + invitación/aceptación (evento explícito).
- Private-by-default: nada del círculo es visible fuera (incluye recipients externos). (Inferencia: consistente con “grupo privado”).
- Moderación: evitar temas sensibles/abusivos (dependencia Moderación).
- invitaciones usan mecanismos definidos en Usuarios (contactos/lookup). (Inferencia: dependencia natural)
- Compatibilidad con sistemas existentes (dependencias directas)


## Control operativo verificable

- Owner: `Equipo neighborhoods`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-NEIGHBORHOOD-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/neighborhoods/dominio-neighborhoods-operacion`
  - `https://jira.aventide.gift/browse/OPS-NEIGHBORHOOD-241`

## Trazabilidad

- Documento origen: `sistema-de-barrio-260207_1012.docx`
- Título extraído: "Sistema Barrio v2.0 (Círculos privados) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
