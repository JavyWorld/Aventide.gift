# STATE_MACHINE · continuity

## Estados detectados/derivados
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- Ningún país queda “sin control”: existe un estado formal del país y una cadena de cobertura.
- Gestión del estado de gobernanza por país: ACTIVE | VACANT | TRANSITION | LOCKDOWN.
- se enruta a beneficiario (COL o COUNTRY_RESERVE) según governance_state.
- Política laboral/HR de terminaciones (solo estado operativo y efectos en plataforma).
- country.governance.state.update (super_admin; ops lead no)

## Transiciones y eventos de entrada/salida
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos/señales a vigilar (mínimo):
- SEV0: LOCKDOWN activado o spike de break-glass + eventos críticos correlacionados.
- WORM y evidencia: todo cambio de estado/rol y cada acción sensible genera eventos auditables y adjunta evidencia (links).
- 3B) Transición (VACANT → TRANSITION)
- Eventos técnicos como QUEUE_REROUTED/PAYOUT_HOLD_APPLIED: el documento define reroute/holds como comportamiento; los nombres exactos de eventos pueden variar, pero deben quedar auditados WORM.
- Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
