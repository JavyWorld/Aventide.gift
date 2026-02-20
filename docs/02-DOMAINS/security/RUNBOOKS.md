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
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Objetivos:
- Reducir fraude (compras falsas, no-entregado, colusión buyer/seller, abuso de refunds).
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Gobernanza fuerte: RBAC + scopes geográficos + kill switches + auditoría WORM.

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
