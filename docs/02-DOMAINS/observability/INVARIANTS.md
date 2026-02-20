# INVARIANTS · observability

Reglas no negociables del dominio:
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Sustituir Auditoría WORM: Observabilidad correlaciona y referencia, pero la evidencia legal/forense vive en Auditoría/Black Box. (Compatibilidad obligatoria, no reemplazo).
- SUPER_ADMIN: configura políticas críticas, ejecuta acciones controladas, ve global (auditado).
- obs.dlq.replay (SRE con auditoría)
- AuditGuard: toda acción activa (banner, breaker, replay DLQ, overrides) requiere reason_code y queda registrada.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- 4.2 Flujo “Money Pipeline” (monitor de invariantes)
- Invariante dura:No puede existir DELIVERED_VERIFIED sin SETTLED pasado X minutos sin causa visible (RETRY, DLQ, HOLD, DISPUTE).
- 5.1 Principios no negociables

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`
