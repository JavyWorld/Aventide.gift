# INVARIANTS · coverage

Reglas no negociables del dominio:
- SUPPORT: ve evidencia de geocode, distancia, historial de cambios de dirección; audita overrides (si existen).
- coverage.audit.read (support/ops)
- AuditGuard: registra coverage_check_run con versión algoritmo y resultado.
- determina ring_id por distancia
- Distancia cercana al límite (99–101%): registrar para auditoría “near_limit”.
- El documento menciona “si existiera” override: debe ser excepcional y auditado.Regla dura (corrección):
- Snapshot de orden marca coverage_result=OVERRIDDEN con actor/razónSuposición: el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- COVERAGE_CHECK_RUN (audit)
- 7.2 Idempotencia

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
