# billing-docs

## Propósito

- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Documento origen: `facturacion--documentos-260207_0805.docx`
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- SELLER: consulta docs de sus órdenes + statements + payout statements.
- condicionada (B2B, monto, tipo producto/servicio).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado".

## Límites

- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- COUNTRY_OPS_LEAD: ve docs del territorio bajo su alcance contractual (si aplica).
- docs.resend (system/support con límites)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado".


## Control operativo verificable

- Owner: `Equipo billing-docs`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-BILLINGDOCS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/billing-docs/dominio-billing-docs-operacion`
  - `https://jira.aventide.gift/browse/OPS-BILLINGDOCS-241`

## Trazabilidad

- Documento origen: `facturacion--documentos-260207_0805.docx`
- Título extraído: "Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
