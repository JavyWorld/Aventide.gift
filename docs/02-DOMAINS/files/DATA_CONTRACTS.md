# DATA_CONTRACTS · files

## Entidades y campos
- Cumplir compliance: no borrar fiscal/ledger antes del mínimo; permitir pseudonimización/crypto-shredding donde corresponda.
- Cifrado fuerte: DEK por entidad + KEK en KMS; crypto-shredding para ciertos tipos.
- Versionado/snapshotting de fotos de listings (“lo que el buyer vio”) y documentos fiscales congelados.
- 4.3 Snapshotting de listings (“lo que el buyer vio”)
- se guarda PDF + JSON snapshot (o hash+ref),
- DEK por entidad protegida por KEK en KMS.
- Crypto-shredding permitido solo donde la ley lo permite; no para KYC/AML ni fiscal/ledger antes del mínimo legal.
- Campos oficiales:

## Constraints y claves de negocio
- Impedir filtración de PoD y adjuntos privados (solo URLs firmadas con TTL corto + no-cache).
- Permitir auditoría completa: cada acceso sensible genera file_access_log append-only.
- SensitivityGuard: data_class determina si se permite URL firmada y TTL.
- Emite URL firmada con TTL y headers:
- PRIVATE_ATTACHMENTS y PoD: TTL recomendado 60s–10min, siempre firmado, nunca CDN público.
- Moderación remueve foto v2 por policy: la orden conserva v1 como evidencia (siempre privada/firmada si corresponde).
- se guarda PDF + JSON snapshot (o hash+ref),
- referencia a foto PoD (privada + firmada),


## Control operativo verificable

- Owner: `Equipo files`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-FILES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/files/dominio-files-operacion`
  - `https://jira.aventide.gift/browse/OPS-FILES-241`

## Trazabilidad
- Documento origen: `sistema-de-archivos-260207_0840.docx`
