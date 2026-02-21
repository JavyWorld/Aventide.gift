# INVARIANTS · security

Reglas no negociables del dominio:
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Gobernanza fuerte: RBAC + scopes geográficos + kill switches + auditoría WORM.
- Auditoría inmutable (Black Box/WORM): roles, money trail, snapshots, entrega/legal.
- Implementación específica de proveedores (p.ej. reglas exactas de Rapyd/otros) más allá de los invariantes (idempotencia, dedupe, firma, etc.).
- AuditGuard (razón obligatoria en acciones sensibles)
- Estado e idempotencia: solo ejecuta si la orden está en estado correcto; evita dobles confirmaciones.
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- Ops Lead puede forzar finalización solo por error técnico, exigiendo motivo+evidencia y auditándolo.
- 5.2 Prioridad de implementación (no negociable)


## Control operativo verificable

- Owner: `Equipo security`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SECURITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/security/dominio-security-operacion`
  - `https://jira.aventide.gift/browse/OPS-SECURITY-241`

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
