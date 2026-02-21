# INVARIANTS · moderation

Reglas no negociables del dominio:
- Convertir moderación en un sistema auditable (evidencia + reason codes + quién decidió).
- Integración obligatoria con Reputación/Score, Búsqueda/Ranking, Órdenes/Pagos, Soporte, Auditoría.
- Sistema de reportes (user flagging) con evidencia automática (chat + order context desde audit log).
- moderation.audit.read (audit/finance/admin)
- AuditGuard (append-only)
- Seller trusted (score > 90) ⇒ post-moderation (AUTO_PUBLISH) con auditorías aleatorias.
- final_action (capa 4, decisión efectiva).Así el sistema es auditable y evita “doble fuente de verdad”.
- Seller trusted: puede AUTO_PUBLISH pero queda sujeto a post-moderation y auditorías aleatorias.
- Si chat: últimos 10 mensajes + order_id desde Audit Log inmutable (no screenshots).
- Toda decisión humana o auto-reject debe mapear a reason_code fijo (educativo + auditable).


## Control operativo verificable

- Owner: `Equipo moderation`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MODERATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/moderation/dominio-moderation-operacion`
  - `https://jira.aventide.gift/browse/OPS-MODERATION-241`

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
