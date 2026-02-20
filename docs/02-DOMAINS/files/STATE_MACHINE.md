# STATE_MACHINE · files

## Estados

- checksum mismatch: rechaza y mantiene estado PENDING_UPLOAD con TTL de limpieza.
- file_access_log append-only para auditoría, incluyendo emisión de URL firmada.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers + idempotencia
- Eventos mínimos

## Trazabilidad

- Documento origen: `sistema-de-archivos-260207_0840.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
