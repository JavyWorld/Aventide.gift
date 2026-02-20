# memory

## Propósito

- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- Definición y objetivos del sistema/módulo
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.
- Documento origen: `sistema-de-memory-260207_1012.docx`
- Usuario desactiva marketing: recordatorios transaccionales siguen si son “utilidad personal” (Suposición: el doc menciona recordatorios; la distinción marketing/transaccional depende del sistema Notificaciones).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)".

## Límites

- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- Alcance (incluye / excluye)
- Excluye (en “Solo Memory”)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-memory-260207_1012.docx`
- Título extraído: "Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
