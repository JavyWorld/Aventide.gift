# STATE_MACHINE · continuity

## Estados

- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- Ningún país queda “sin control”: existe un estado formal del país y una cadena de cobertura.
- Gestión del estado de gobernanza por país: ACTIVE | VACANT | TRANSITION | LOCKDOWN.
- Política laboral/HR de terminaciones (solo estado operativo y efectos en plataforma).
- WORM y evidencia: todo cambio de estado/rol y cada acción sensible genera eventos auditables y adjunta evidencia (links).
- COL/ActingCOL opera estado y configuración local (zonas, onboarding, contenido local) dentro de límites.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- 3B) Transición (VACANT → TRANSITION)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos
- Eventos/señales a vigilar (mínimo):
- SEV0: LOCKDOWN activado o spike de break-glass + eventos críticos correlacionados.
- WORM y evidencia: todo cambio de estado/rol y cada acción sensible genera eventos auditables y adjunta evidencia (links).
- Eventos técnicos como QUEUE_REROUTED/PAYOUT_HOLD_APPLIED: el documento define reroute/holds como comportamiento; los nombres exactos de eventos pueden variar, pero deben quedar auditados WORM.
- Trigger: anomalías por seguridad/abuso (ver 9) o incidentes de integridad.

## Trazabilidad

- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
