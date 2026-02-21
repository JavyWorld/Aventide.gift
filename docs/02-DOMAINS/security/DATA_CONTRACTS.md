# DATA_CONTRACTS · security

## Entidades y campos
- Definición: Sistema transversal que protege CIA + Privacidad (Confidencialidad, Integridad, Disponibilidad) y blinda los flujos críticos de Aventide Gift contra fraude/abuso:Identidad → Checkout → Pago/Escrow → Entrega (Tridente) → Settlement/Payout → Disputas/Auditoría mediante “Defensa en Profundidad” (capas obligatorias A–H).
- Privacidad defendible: crypto-shredding bien aplicado + retención correcta (no borra ledger/AML).
- Identidad/autenticación (Firebase/Auth0) + sesión/JWT propio con claims + RBAC.
- Auditoría inmutable (Black Box/WORM): roles, money trail, snapshots, entrega/legal.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- audit_logs con campos estándar (mínimo):
- Regla: ni SuperAdmin puede DELETE/UPDATE; solo INSERT/SELECT (almacenamiento/tablas separadas).
- 6.3 Crypto-shredding (claves por usuario)

## Constraints y claves de negocio
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Seguridad de archivos/evidencias (URLs firmadas, acceso por rol).
- Implementación específica de proveedores (p.ej. reglas exactas de Rapyd/otros) más allá de los invariantes (idempotencia, dedupe, firma, etc.).
- 4.2.2 Confirmación forense (PoD)
- Estado e idempotencia: solo ejecuta si la orden está en estado correcto; evita dobles confirmaciones.
- PIN one-time 6–8 dígitos, guardado hasheado (Argon2/bcrypt).
- Foto: evidencia obligatoria; URL firmada privada; acceso limitado por rol (Soporte/Legal).
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.


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
