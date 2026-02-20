# ADR-0001: Contexto y decisiones clave (content)

- **Estado**: Aprobado
- **Contexto**: Moderación pre y post: IA + revisión humana según riesgo/reputación.

## Decisiones
- Moderación pre y post: IA + revisión humana según riesgo/reputación.
- Trusted pero la IA detecta riesgo (nudity/text/dup robado): se anula fast-track y vuelve a PENDING humana.
- Toda decisión humana: approve/reject/pause requiere reason_code + comentario opcional.
- Sistema de Contenido v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- 1) Definición y objetivos del sistema/módulo

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-contenido-260206_2344.docx`
