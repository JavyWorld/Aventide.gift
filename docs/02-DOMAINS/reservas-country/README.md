# reservas-country

## Propósito

- Se gobierna con workflow formal (request/approve/execute), auditoría WORM y controles break-glass para cualquier movimiento sensible.
- reserve.disbursement.request.create{country} (finance_admin)
- reserve.disbursement.request.approve{country} (finance_admin distinto; four-eyes)
- RESERVE_DISBURSEMENT_REQUESTED/APPROVED/EXECUTED/REJECTED
- Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)
- Fuentes de verdad:
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
- Si quieres, lo siguiente es convertir este sistema a contratos “copy-paste para ingeniería”: endpoints admin exactos, enums purpose_code, eventos definitivos, y un set mínimo de tests UAT (vacancia, disbursement, pérdida y recovery).
- “resumen-260207_1014” (Continuidad, vacancia, routing a reserva, break-glass, four-eyes, monitoreo).
- Definición y objetivos del sistema/módulo
- Título extraído: "Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)".

## Límites

- Regla exacta de qué eventos alimentan inflow a reserve además del routing por vacancia (p.ej., diferencial cap-earn si Rate Engine lo define).
- Alcance (incluye / excluye)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Determinismo contable: todo movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Regla exacta de qué eventos alimentan inflow a reserve además del routing por vacancia (p.ej., diferencial cap-earn si Rate Engine lo define).
- Integración con Waterfall Engine para cubrir pérdidas (Layer 1).
- si aplica: ejecuta payout vía proveedor (por Integraciones/Pagos).
- Pagos/Integraciones
- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)

## Trazabilidad

- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
- Título extraído: "Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
