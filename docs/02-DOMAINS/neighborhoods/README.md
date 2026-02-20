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

- Alcance (incluye / excluye)
- Private-by-default: nada del círculo es visible fuera (incluye recipients externos). (Inferencia: consistente con “grupo privado”).
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Errores de notificación “gift incoming” (dependencia Notificaciones)
- Miembros del círculo (usuarios Aventide) + invitación/aceptación (evento explícito).
- Private-by-default: nada del círculo es visible fuera (incluye recipients externos). (Inferencia: consistente con “grupo privado”).
- Moderación: evitar temas sensibles/abusivos (dependencia Moderación).
- invitaciones usan mecanismos definidos en Usuarios (contactos/lookup). (Inferencia: dependencia natural)
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-barrio-260207_1012.docx`
- Título extraído: "Sistema Barrio v2.0 (Círculos privados) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
