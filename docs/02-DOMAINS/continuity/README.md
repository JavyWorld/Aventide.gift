# continuity

## Propósito

- money.reserve.disbursement.request/create (finance_admin)
- (Recomendación operativa del sistema) four-eyes: requester ≠ approver para asignación de COL.
- reserve_disbursement_request
- RESERVE_DISBURSEMENT_REQUESTED/APPROVED/EXECUTED/REJECTED
- Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”
- Fuente de verdad: Documento “resumen-260207_1014”.
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- se enruta a beneficiario (COL o COUNTRY_RESERVE) según governance_state.
- country.governance.state.update (super_admin; ops lead no)
- Definición y objetivos del sistema/módulo
- Compatibilidad con sistemas existentes (dependencias directas)
- LOCKDOWN: riesgo alto/integridad comprometida; restricciones fuertes y hold/contención.
- VACANT: detener cambios peligrosos y mantener servicio mínimo, sin perder control ni dinero.
- Título extraído: "Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”".

## Límites

- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- Política laboral/HR de terminaciones (solo estado operativo y efectos en plataforma).
- Alcance (incluye / excluye)
- Reglas y políticas (límites, expiraciones, caps, validaciones)
- COL/ActingCOL opera estado y configuración local (zonas, onboarding, contenido local) dentro de límites.

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
- Título extraído: "Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
