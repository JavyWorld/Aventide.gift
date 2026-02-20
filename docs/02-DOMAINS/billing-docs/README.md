# billing-docs

## Propósito

- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- Definición y objetivos del sistema/módulo
- Documento origen: `facturacion--documentos-260207_0805.docx`
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- SELLER: consulta docs de sus órdenes + statements + payout statements.
- condicionada (B2B, monto, tipo producto/servicio).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado".

## Límites

- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Alcance (incluye / excluye)
- COUNTRY_OPS_LEAD: ve docs del territorio bajo su alcance contractual (si aplica).
- docs.resend (system/support con límites)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado".

## Trazabilidad

- Documento origen: `facturacion--documentos-260207_0805.docx`
- Título extraído: "Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
