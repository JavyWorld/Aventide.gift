# DATA_CONTRACTS · backup

## Entidades y campos
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Ledger/Finanzas: movimientos, fees, payouts, refunds, disputas, snapshots financieros (inmutables).
- Documentos legales/fiscales: facturas, recibos, notas crédito, PoD y JSON/hash de snapshot en WORM/Object Lock.
- 4.1 Backups OLTP (PITR + snapshots + export lógico)
- Snapshot físico diario.
- 4.2 Ledger/Finanzas (append-only + snapshots + reconciliación)
- Ledger tratado como append-only.
- Snapshots financieros inmutables con hash + metadatos (idealmente WORM).

## Constraints y claves de negocio
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- Documentos legales/fiscales: facturas, recibos, notas crédito, PoD y JSON/hash de snapshot en WORM/Object Lock.
- 4.2 Ledger/Finanzas (append-only + snapshots + reconciliación)
- Ledger tratado como append-only.
- Snapshots financieros inmutables con hash + metadatos (idealmente WORM).
- guardar PDF final + JSON snapshot (o hash+ref) en bucket WORM/Object Lock,
- inventario/manifest con hashes para detectar corrupción.

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
