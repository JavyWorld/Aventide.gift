# neighborhoods

## Qué resuelve
- Basado en: definición “Social layer: Barrio (o Círculos)” + sus componentes (recipients compartidos, fechas opt-in, wishlists temáticas, notificación de regalo entrante).

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- Private-by-default: nada del círculo es visible fuera (incluye recipients externos). (Inferencia: consistente con “grupo privado”).
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias
- Moderación: evitar temas sensibles/abusivos (dependencia Moderación).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- invitaciones usan mecanismos definidos en Usuarios (contactos/lookup). (Inferencia: dependencia natural)
- Errores de notificación “gift incoming” (dependencia Notificaciones)
- 11) Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`
- Título extraído: "Sistema Barrio v2.0 (Círculos privados) — corregido y unificado".
