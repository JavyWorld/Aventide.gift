# DATA_CONTRACTS · coverage

## Entidades y campos
- Proveer evidencia operacional: snapshot logístico por orden (distancia, geocode meta, resultado cobertura).
- Integración con Búsqueda (ST_DWithin) y Ordenes (snapshot logístico).
- SYSTEM/BOT: geocoding, cálculo distancia, check cobertura, snapshot, cache invalidation, jobs de re-geocoding.
- Snapshot de orden marca coverage_result=OVERRIDDEN con actor/razónSuposición: el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Campos mínimos:
- countries: address_schema, moneda, unidades (km/millas), reglas macro.
- 6.4 order_logistics_snapshot

## Constraints y claves de negocio
- Buyer confirma y guarda con POST /addresses.Regla dura: no se guarda sin lat/long validado.
- address_quality_score bajo: permitir guardar pero marcar needs_review=true (para antifraude/soporte), y exigir confirmación extra (Suposición: consistente con “score opcional para antifraude y soporte”).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- addresses/validate: idempotente por (buyer_id, raw_address_hash) si se cachea.
- coverage/check: idempotente por (seller_id, address_id, date_bucket, algo_version) para caching controlado.
- order_snapshot: idempotente por (order_id).
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
