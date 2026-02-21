# RUNBOOKS · security

## Operación
- Integración con Observabilidad como “capa de detección” (SIEM + alertas).
- Operación de zonas:
- Anti-abuso: 3 fallos de PIN en 10 min → bloqueo temporal + alerta a Ops Lead.
- A) Edge: CDN/WAF/DDoS + rate limiting en borde.B) App: validación estricta + JWT/RBAC + reglas duras en endpoints críticos.C) Data: cifrado + acceso mínimo + aislamiento (RLS/tenant).D) User: 2FA/passkeys/biometría cuando aplique + controles anti-abuso.E) Trust: KYC sellers + trust score buyer/seller para fricción adaptativa.F) Payments: tokenización + PCI vía PSP.G) SDLC: NIST SSDF + SAST/DAST + secret scanning.H) Observabilidad/SIEM: alertas por anomalías de auth, drift de permisos, fraude.
- SIEM/alertas + hardening continuo
- Alertas por anomalías de autenticación, drift de permisos, fraude, lockouts de PIN, invalid signature webhooks.

## Incidentes, rollback y backfill
- Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado
- Fuente de verdad: “Sistema de Seguridad (Aventide Gift)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Objetivos:
- Reducir fraude (compras falsas, no-entregado, colusión buyer/seller, abuso de refunds).
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Gobernanza fuerte: RBAC + scopes geográficos + kill switches + auditoría WORM.


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

## Ownership & Escalation

- **Owner técnico:** `Equipo security`
- **Owner negocio/regulatorio:** `Product + Compliance (security)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

