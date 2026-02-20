# ADR-0001: Contexto y decisiones clave (memory)

- **Estado**: Aprobado
- **Contexto**: Recipients globales (riesgo de privacidad) → corregido: recipients son scoped al buyer.

## Decisiones
- Recipients globales (riesgo de privacidad) → corregido: recipients son scoped al buyer.
- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- 1) Definición y objetivos del sistema/módulo
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.
- Objetivos (duros):

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`
