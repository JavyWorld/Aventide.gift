# INVARIANTS · files

Reglas no negociables del dominio:
- WORM/Object Lock para documentos legales inmutables,
- Permitir auditoría completa: cada acceso sensible genera file_access_log append-only.
- SUPPORT: acceso temporal y auditado por ticket/orden.
- SUPER_ADMIN: acceso total pero Operación definida y validada auditado.
- files.audit.read (audit/finance)
- SensitivityGuard: data_class determina si se permite URL firmada y TTL.
- AuditGuard: log obligatorio en toda lectura/descarga/URL issuance.
- registro de auditoría.
- PRIVATE_ATTACHMENTS y PoD: TTL recomendado 60s–10min, siempre firmado, nunca CDN público.
- Moderación remueve foto v2 por policy: la orden conserva v1 como evidencia (siempre privada/firmada si corresponde).


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
