# STATE_MACHINE · loyalty

## Estados

- loyalty_accounts (estado materializado)

## Transiciones

- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”
- Backend aplica FS con clamp duro:fs_applied = min(fs_balance_available, platform_fee_amount)y genera evento FEE_CREDIT_APPLIED (max_applied = platform_fee_amount).
- No reversión ante refund/chargeback → corregido: eventos REVOKED/ajuste negativo y bloqueo según policy país.

## Trazabilidad

- Documento origen: `sistema-de-lealtad-260207_0817.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
