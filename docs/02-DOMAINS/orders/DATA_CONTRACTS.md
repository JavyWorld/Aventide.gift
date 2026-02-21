# DATA_CONTRACTS · orders

## Entidades y campos
- Snapshot inmutable de precios/fees/items/dirección/promesa.
- Checkout → creación de orden con snapshot.
- Cálculo profundo de fees/impuestos (solo se snapshottea su resultado).
- 4.1 Checkout → Creación de orden (snapshot)
- Se crea order en estado CREATED con snapshot:
- 5.5 Lead time, cut-off y promesa (persistido en snapshot)
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- address_snapshot JSON (inmutable)

## Constraints y claves de negocio
- “Dinero retenido”: seller no toca fondos antes de entrega confirmada.
- BUYER: crea orden, cancela en pre-aceptación, trackea, confirma/abre disputa.
- Si zona no activa / sin capacidad para la ventana: no se permite crear o se crea como “no confirmable” (según policy); en cualquier caso, no se debe pagar si no es entregable. (Integración obligatoria con Capacidad/Logística; aquí se fija el enforcement en el gate de checkout, coherente con “lo visible debe ser comprable”.)
- Reintentos: idempotencia por payment_attempt_id.
- PIN ingresado (hash)
- Se crea delivery_proof ligado a order_id con:photo_url, gps_lat, gps_lng, gps_accuracy, pin_hash, captured_at, captured_by_user_id, device_fingerprint, ...
- 6.2 Timeline / Action Stream (append-only)
- pin_hash


## Control operativo verificable

- Owner: `Equipo orders`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ORDERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/orders/dominio-orders-operacion`
  - `https://jira.aventide.gift/browse/OPS-ORDERS-241`

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
