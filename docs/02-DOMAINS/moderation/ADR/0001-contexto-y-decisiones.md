# ADR-0001: Contexto y decisiones clave (moderation)

- **Estado**: Aprobado
- **Contexto**: EvidenceGuard (no permite decisión humana sin evidence_ref)

## Decisiones
- EvidenceGuard (no permite decisión humana sin evidence_ref)
- FLAG (requiere riesgo/humano)
- Salida Capa 2 (decisión operativa):
- final_action (capa 4, decisión efectiva).Así el sistema es auditable y evita “doble fuente de verdad”.
- Toda decisión humana o auto-reject debe mapear a reason_code fijo (educativo + auditable).
- Crecimiento de queue_depth (riesgo operativo)

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
