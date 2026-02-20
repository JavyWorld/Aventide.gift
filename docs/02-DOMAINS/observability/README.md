# observability

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (límites, validaciones, caps, resiliencia)
- Sistema de Observabilidad v2.0 (SRE / “Sistema Nervioso Central”) — corregido y unificado

## Dependencias
- Telemetría de: backend API, workers, webhooks, DB, cache, colas, integraciones (Rapyd, WhatsApp/SMS, Email, Storage, Maps), Policy Engine + App Camaleón.
- Request entra al API → se genera/propaga trace_id + request_id.
- Cada llamada a DB/provider genera span hijo con latencia y resultado.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Integraciones

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`
- Título extraído: "Sistema de Observabilidad v2.0 (SRE / “Sistema Nervioso Central”) — corregido y unificado".
