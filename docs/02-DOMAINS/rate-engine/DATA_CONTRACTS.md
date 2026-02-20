# DATA_CONTRACTS · rate-engine

## Entidades y campos
- Este motor sustituye la lógica dispersa del “Take-Rate Engine OS” y del “Revenue Rate Engine” por un solo cerebro que produce un RateVector y lo “compila” a un breakdown financiero y a un blueprint de ledger/settlement, todo con snapshot por orden.
- Reproducibilidad contable: cada orden debe poder recalcularse 1:1 desde su snapshot (locked_fee_structure + decision_id + policy_version).
- Compilación a breakdown final (FeePolicyResolver) y snapshot en checkout.
- Ledger split determinístico:
- Ejecución de reembolsos/disputas (lo hace el pipeline de money/disputas; este motor solo fija reglas y splits snapshotteados).
- Checkout Financial Engine (FeePolicyResolver): compila RateVector a breakdown y snapshot.
- 4.2 Checkout: resolver breakdown + snapshot (no retroactividad)
- Orden creada queda congelada: todo settlement/refund/dispute usará ese snapshot.

## Constraints y claves de negocio
- Definición: Motor único que gobierna, de forma dinámica, determinista y auditable, todos los porcentajes (rates) que impactan el dinero de una orden, separando estrictamente:
- SYSTEM (Rate Decision Service): calcula RateVector, emite decisiones, firma y versiona.
- AuditGuard (append-only: decisiones y cambios)
- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)
- Fuente de verdad: “Motor Unificado de Rates para Aventide Gift”.

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
