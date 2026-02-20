# ADR-0001: Contexto y decisiones clave (billing-docs)

- **Estado**: Aprobado
- **Contexto**: errores de WORM/Object Lock (alto riesgo compliance)

## Decisiones
- errores de WORM/Object Lock (alto riesgo compliance)
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Objetivos:

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `facturacion--documentos-260207_0805.docx`
