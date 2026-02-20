# STATE_MACHINE · backup

## Estados

- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Lifecycle por clase (evidencia disputas > adjuntos chat).
- sanity de estados críticos (no dejar PAID sin ledger)
- Tras restore Tier 0, reconciliar contra webhooks/estado proveedor antes de reabrir dinero.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (colas/jobs) + idempotencia
- Eventos mínimos

## Trazabilidad

- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
