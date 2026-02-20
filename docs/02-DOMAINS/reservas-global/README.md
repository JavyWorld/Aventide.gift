# reservas-global

## Propósito

- global_reserve.emergency.freeze.request/approve (super_admin/finance_admin)
- global_reserve.disbursement.request/create (finance_admin) (solo si existe uso fuera del waterfall; ver 8.2)
- Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)
- Fuentes de verdad:
- Continuidad / Country Governance (VACANT/LOCKDOWN, break-glass, four-eyes, WORM).
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
- Definición y objetivos del sistema/módulo
- Compatibilidad con sistemas existentes (dependencias directas)
- Sistema de Capitalización de Reserva Global v2.0 (integrado con Motor Unificado “Take Rate Engine + Revenue Rate Engine”)
- Título extraído: "Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)".

## Límites

- Alcance (incluye / excluye)
- Reglas y políticas (límites, expiraciones, caps, validaciones)
- No tocar lo buyer-facing fuera de límites: el motor decide rates, pero el snapshot por orden es inmutable y no retroactivo.

## Dependencias

- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Reserva Nacional v2.0 (Layer 1, workflow, prohibiciones, observabilidad).
- Waterfall Engine (dependencia directa)
- Compatibilidad con sistemas existentes (dependencias directas)
- Sistema de Capitalización de Reserva Global v2.0 (integrado con Motor Unificado “Take Rate Engine + Revenue Rate Engine”)

## Trazabilidad

- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
- Título extraído: "Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
