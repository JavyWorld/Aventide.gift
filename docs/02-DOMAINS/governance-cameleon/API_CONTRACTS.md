# API_CONTRACTS · governance-cameleon

## Versión de contrato

- **Versión actual:** `v1.1.0`
- **Compatibilidad:** `v1.0.0` se mantiene de forma transitoria mediante endpoint legacy de comandos genéricos.
- **Ruta de migración:** clientes en `v1.0.0` deben migrar de `POST /sistema-gobernanza-multi-pais-app-camaleon/commands` a endpoints explícitos `/governance/*`.

## Endpoints v1.1 (explícitos)

1. `POST /governance/resolve`
   - Resuelve contexto de gobernanza para host + tenant + país.
2. `GET /governance/countries/{country_code}/ui-profile`
   - Retorna perfil de UI vigente por país.
3. `POST /governance/countries/{country_code}/rulesets/publish`
   - Publica ruleset con idempotencia obligatoria.
4. `POST /governance/simulate-routing`
   - Simula decisión de enrutamiento/políticas para un escenario.

## Campos mínimos obligatorios

Los flujos de resolución, consulta, publicación y simulación deben transportar/retornar al menos:

- `host`
- `country_code`
- `tenant_id`
- `locale`
- `currency`
- `config_version`
- `signature_status`

Estos campos conforman el contexto base de gobernanza y son requeridos para validar configuración, compliance y fallback operativo.

## Errores de negocio normalizados

Se formalizan los siguientes códigos:

- `COUNTRY_NOT_ENABLED` → país no habilitado.
- `HOST_NOT_MAPPED` → host no mapeado al contexto de tenant/país.
- `INVALID_SIGNATURE` → firma inválida del artefacto de configuración/UI.
- `INCOMPATIBLE_CONFIG_VERSION` → versión de configuración incompatible con el contrato cliente.

Todos los errores deben incluir `correlation_id` para trazabilidad E2E.

## Idempotencia y auditoría

### Idempotencia

- `POST /governance/countries/{country_code}/rulesets/publish` requiere header `Idempotency-Key`.
- La clave debe ser estable por intento lógico de publicación para soportar reintentos seguros.

### Auditoría

- Operaciones mutables y simulaciones deben registrar metadatos de actor:
  - `actor_id`
  - `actor_role`
- Se requiere `correlation_id` (header `X-Correlation-Id` o generado por plataforma) para trazabilidad distribuida.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- GeoIntegrityGuard (address con lat/lng obligatorio)

## Códigos de error

- Firma de UI config obligatoria; app rechaza configs no firmadas o schema incompatible y entra en fallback.

## Control operativo verificable

- Owner: `Equipo governance-cameleon`
- Fecha de última validación: `2026-02-23 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GOVERNANCECA-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/governance-cameleon/dominio-governance-cameleon-operacion`
  - `https://jira.aventide.gift/browse/OPS-GOVERNANCECA-241`

## Trazabilidad

- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
