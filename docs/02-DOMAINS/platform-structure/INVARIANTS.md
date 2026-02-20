# INVARIANTS · platform-structure

Reglas no negociables del dominio:
- contratos transversales (territorio como first-class, policy engine, RBAC+scopes, server-driven UI, auditoría WORM, pipeline de dinero),
- Multi-país/territorio como “primera clase” en requests, UI, reglas, búsqueda, pagos, auditoría y analítica.
- Trazabilidad y evidencia (logs anti-PII + auditoría append-only + WORM) como base transversal.
- Controles transversales: RBAC+scopes, PolicyGuard, idempotencia, anti-PII, break-glass.
- Separación de poderes + kill switch regional auditado.
- Service actors: workers/webhooks corren con service_id para trazabilidad/auditoría.
- Regional OS incluye Studio para operar config/UI/merchandising bajo guardrails y auditoría.
- El frontend nunca mueve dinero ni habla directo con Rapyd para mover fondos; todo pasa por backend + ledger/pipeline auditable.
- Rutas de Studio + flujo draft→preview→publish + time machine + rollback con auditoría completa.
- 6.1 Idempotencia + dedupe

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`
