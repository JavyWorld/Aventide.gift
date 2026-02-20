# STATE_MACHINE · audit

## Estados detectados/derivados
- SYSTEM/WORKER (Service_ID): produce eventos obligatorios por write-path.
- SensitiveReadGuard (VIEW_SENSITIVE siempre genera evento)
- 4) Flujos end-to-end (happy path + edge cases)
- Fallo en escritura de auditoría: la acción crítica debe fallar (enforcement) o entrar en modo safe (bloqueo) según severidad. (Inferencia: consistente con “toda acción crítica write debe producir evento”.)
- Todo evento debe tener actor_id y actor_type (USER|SERVICE).
- packet_json (gps, time, device, photo_file_id, pin_state, etc.)

## Transiciones y eventos de entrada/salida
- SYSTEM/WORKER (Service_ID): produce eventos obligatorios por write-path.
- SensitiveReadGuard (VIEW_SENSITIVE siempre genera evento)
- Fallo en escritura de auditoría: la acción crítica debe fallar (enforcement) o entrar en modo safe (bloqueo) según severidad. (Inferencia: consistente con “toda acción crítica write debe producir evento”.)
- Todo evento debe tener actor_id y actor_type (USER|SERVICE).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (audit-aware)
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
