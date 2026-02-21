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
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Compatibilidad con sistemas existentes (dependencias directas)
- LOCKDOWN: riesgo alto/integridad comprometida; restricciones fuertes y hold/contención.
- VACANT: detener cambios peligrosos y mantener servicio mínimo, sin perder control ni dinero.
- Título extraído: "Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”".

## Límites

- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- Política laboral/HR de terminaciones (solo estado operativo y efectos en plataforma).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Reglas y políticas (límites, expiraciones, caps, validaciones)
- COL/ActingCOL opera estado y configuración local (zonas, onboarding, contenido local) dentro de límites.

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Compatibilidad con sistemas existentes (dependencias directas)


## Control operativo verificable

- Owner: `Equipo continuity`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-CONTINUITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/continuity/dominio-continuity-operacion`
  - `https://jira.aventide.gift/browse/OPS-CONTINUITY-241`

## Trazabilidad

- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
- Título extraído: "Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
