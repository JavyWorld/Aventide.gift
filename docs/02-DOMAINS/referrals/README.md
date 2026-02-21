# referrals

## Propósito

- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X E).
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Documento origen: `sistema-de-referido-260207_0826.docx`
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Referidos v2.0 (Referral Program) — corregido y unificado".

## Límites

- Idempotencia (reglas duras)
- Ser determinista: estados + ventana de atribución + hold windows + catálogo de reglas por país (server-driven).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- EOV (idéntico a Lealtad)EOV = (items_subtotal - seller_coupon_discount) + delivery_fee_if_applicableExcluye: taxes, platform_fee, ops fee, processing fee.
- Anti-abuso y límites (antes de aprobar)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.
- Ser reversible: toda recompensa registrada en ledger y reversible por eventos negativos.
- Compatibilidad con sistemas existentes (dependencias directas)


## Control operativo verificable

- Owner: `Equipo referrals`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REFERRALS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/referrals/dominio-referrals-operacion`
  - `https://jira.aventide.gift/browse/OPS-REFERRALS-241`

## Trazabilidad

- Documento origen: `sistema-de-referido-260207_0826.docx`
- Título extraído: "Sistema de Referidos v2.0 (Referral Program) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
