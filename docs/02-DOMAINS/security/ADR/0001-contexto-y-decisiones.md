# ADR-0001: Contexto y decisiones clave (security)

- **Estado**: Aprobado
- **Contexto**: El nivel de verificación sube/baja según señales de riesgo/actividad (ej. “seller grande”).

## Decisiones
- El nivel de verificación sube/baja según señales de riesgo/actividad (ej. “seller grande”).
- Jerarquía: roles/scopes y kill switch por zona como control de riesgo.
- Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado
- Fuente de verdad: “Sistema de Seguridad (Aventide Gift)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
