# INVARIANTS · geo-intelligence-map

Reglas no negociables del dominio:
- Extensión: población/densidad poblacional oficial + usuarios GPS-verificados agregados (penetración), siempre anti-PII.
- Heatmaps y capas deben ser performantes y anti-PII: nunca pintar usuarios individuales; Operación definida y validada agregado por grid H3/tiles.
- Operación de zona: cambiar estado de zona (kill switch / paused / saturated) desde el mapa, con motivo y auditoría.
- Click zona → drawer/panel contextual → puede cambiar estado operativo (ACTIVE/PAUSED/SATURATED/CREATED_INACTIVE) si tiene permiso zone.update_status, registrando motivo y auditoría append-only.
- No se borra histórico: se desactiva (disabled_at), auditado.
- 7) Eventos y triggers (pipelines) + idempotencia
- Idempotencia: (country_code, dataset_version, cell_id)
- license/terms_ref (para auditoría/legal)
- Fallback/rollback: si falla ingesta, mantener dataset_version_current y alertar; permitir rollback explícito auditado.
- 10) Seguridad y auditoría


## Control operativo verificable

- Owner: `Equipo geo-intelligence-map`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GEOINTELLIGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/geo-intelligence-map/dominio-geo-intelligence-map-operacion`
  - `https://jira.aventide.gift/browse/OPS-GEOINTELLIGE-241`

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
