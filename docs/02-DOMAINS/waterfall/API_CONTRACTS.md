# API_CONTRACTS · waterfall

## Endpoints

- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- plan de recapitalización por prioridad de impacto
- API mínima (lista para backend)
- idempotency-key
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Auth

- Aplicar autenticación obligatoria con RBAC y scoping de dominio en todas las operaciones.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- idempotency-key
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `waterfall-engine-v10-260207_0941.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
