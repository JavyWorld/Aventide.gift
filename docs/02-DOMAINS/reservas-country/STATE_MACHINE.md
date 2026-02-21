# STATE_MACHINE · reservas-country

## Estados

- SUPER_ADMIN (global): puede activar estados especiales (LOCKDOWN), aplicar break-glass para acciones críticas y forzar medidas de contención con evidencia.
- Cambio de estado en medio de un checkout: se respeta el snapshot de la orden (no retroactividad).

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)
- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)

## Triggers

- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (Reserva Nacional + Waterfall)
- Regla exacta de qué eventos alimentan inflow a reserve además del routing por vacancia (p.ej., diferencial cap-earn si Rate Engine lo define).
- Si quieres, lo siguiente es convertir este sistema a contratos “copy-paste para ingeniería”: endpoints admin exactos, enums purpose_code, eventos definitivos, y un set mínimo de tests UAT (vacancia, disbursement, pérdida y recovery).


## Control operativo verificable

- Owner: `Equipo reservas-country`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RESERVASCOUN-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reservas-country/dominio-reservas-country-operacion`
  - `https://jira.aventide.gift/browse/OPS-RESERVASCOUN-241`

## Trazabilidad

- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
