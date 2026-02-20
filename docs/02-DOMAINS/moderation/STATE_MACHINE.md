# STATE_MACHINE · moderation

## Estados detectados/derivados
- 4) Flujos end-to-end (happy path + edge cases)
- Salida Capa 1 (recomendación):
- Salida Capa 2 (decisión operativa):
- Estado obligatorio de producto:DRAFT → PENDING_REVIEW → (FLAGGED → revisión humana) → ACTIVE
- Entradas mínimas:
- Corrección de incoherencia:Strike Ledger y “funds policy” deben ser derivados y aplicados por policy engine/pagos; moderación no mueve dinero, solo cambia el estado/política (rolling_reserve=50%, freeze=180d).

## Transiciones y eventos de entrada/salida
- Salida Capa 1 (recomendación):
- Salida Capa 2 (decisión operativa):
- Entradas mínimas:
- Corrección de incoherencia: StrikeLedger es proyección; los cambios reales ocurren vía eventos STRIKE_APPLIED + policy engine que setea flags en user_status y seller_operational_flags.
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
