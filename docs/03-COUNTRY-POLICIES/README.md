# 03 - Country Policies

Este directorio define políticas locales por país activo.

## Países activos
- `DO` (República Dominicana)
- `CO` (Colombia)

Cada país contiene:
- `README.md`: alcance regulatorio y operativo local.
- `POLICY_OVERRIDES.md`: diferencias frente al baseline global.
- `COMPLIANCE_CHECKLIST.md`: controles de cumplimiento por dominio.
- `RISK_NOTES.md`: riesgos locales y mitigaciones.

## Country + Domain Onboarding

Para estandarizar el alta de nuevos países y dominios locales, utilizar la plantilla reusable:

- [`_templates/COUNTRY_DOMAIN_ONBOARDING.md`](_templates/COUNTRY_DOMAIN_ONBOARDING.md)

La plantilla cubre:
- Dominio y DNS (alta de `aventide.xx`, SSL, CDN/WAF, cache y edge headers).
- Routing y experiencia (mapeo host a `country_code/tenant_id`, comportamiento en `aventide.com` y selector manual).
- Configuración de negocio (moneda, idioma, pagos, envíos e impuestos).
- Cumplimiento (checklist legal/fiscal/privacidad, ADR local y `POLICY_OVERRIDES.md`).
- Observabilidad y operación (dashboards, métricas mínimas y runbook de incidentes multi-país).
