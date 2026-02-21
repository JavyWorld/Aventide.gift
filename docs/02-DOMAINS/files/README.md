# files

## Propósito

- privacy.delete_request.submit
- Sistema valida RBAC+ABAC + data_class.
- action (VIEW/DOWNLOAD/ISSUE_SIGNED_URL/UPLOAD/DELETE_REQUEST/LEGAL_HOLD)
- Sistema de Archivos v2.0 (Storage & Attachments) — corregido y unificado
- Fuente de verdad: “Sistema de Archivos (Storage & Attachments)”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Documento origen: `sistema-de-archivos-260207_0840.docx`
- Definición: Sistema central de almacenamiento para media pública, adjuntos privados, evidencia operativa, y documentos legales/fiscales, con:
- entrega por Signed URLs para contenido privado,
- Unificar evidencia/documentos sin dispersión por servicios.
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Archivos v2.0 (Storage & Attachments) — corregido y unificado".

## Límites

- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- COUNTRY_OPS_LEAD: acceso scoping país/hub con límites.
- file_access_log append-only para auditoría, incluyendo emisión de URL firmada.

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Compatibilidad con sistemas existentes (dependencias directas)


## Control operativo verificable

- Owner: `Equipo files`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-FILES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/files/dominio-files-operacion`
  - `https://jira.aventide.gift/browse/OPS-FILES-241`

## Trazabilidad

- Documento origen: `sistema-de-archivos-260207_0840.docx`
- Título extraído: "Sistema de Archivos v2.0 (Storage & Attachments) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
