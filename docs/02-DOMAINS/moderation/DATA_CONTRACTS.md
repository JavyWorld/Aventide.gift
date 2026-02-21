# DATA_CONTRACTS · moderation

## Entidades y campos
- Corrección de incoherencia:Strike Ledger y “funds policy” deben ser derivados y aplicados por policy engine/pagos; moderación no mueve dinero, solo cambia el estado/política (rolling_reserve=50%, freeze=180d).
- Campos definidos:
- risk_score_at_time (snapshot)
- D) StrikeLedger
- Corrección de incoherencia: StrikeLedger es proyección; los cambios reales ocurren vía eventos STRIKE_APPLIED + policy engine que setea flags en user_status y seller_operational_flags.
- Strikes sin efectos coherentes → corregido: tabla de efectos cruzados (ranking, creación productos, reserve, freeze) y StrikeLedger auditable.
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.

## Constraints y claves de negocio
- AuditGuard (append-only)
- IP_HASH
- PAYMENT_METHOD_HASH
- IP compartida (cafés/redes): IP_HASH es señal débil (solo ayuda; no es suficiente para hard ban). (Inferencia: consistente con “cuidado por redes públicas”.)
- Chat: Capa 1 texto; si abuso/leakage confirmado ⇒ habilita reporte + señal a soporte/T&S.
- evidence_ref (audit-log links, imágenes, hashes)
- type (DEVICE_ID|IP_HASH|PAYMENT_METHOD_HASH|PHONE_NORMALIZED)
- value_hash


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
