# STATE_MACHINE · content

## Estados

- Rechazo: estado REJECTED con razón específica (“foto borrosa”, “descripción engañosa”).
- Workflow de publicación y estados (DRAFT→PENDING→ACTIVE, etc.) con gates por capacidad/logística/moderación.
- Moderación/Trust & Safety completa (Contenido integra gates/estados y dispara/recibe decisiones).
- QualityGateGuard (capacidad + logística + assets + atributos requeridos + estado de seller)

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)
- event_id único por transición.

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos del dominio Contenido
- event_id único por transición.
- Suspensión seller lenta → corregido: regla de desindex < 1 minuto con evento y métricas.

## Trazabilidad

- Documento origen: `sistema-de-contenido-260206_2344.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
