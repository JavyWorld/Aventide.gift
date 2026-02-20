# 06 · MASTER BLUEPRINT

> **Puerta de entrada oficial para onboarding técnico y operativo (IA/humano).**
> Este documento es la vista integral del sistema completo y debe ser la primera lectura para cualquier persona o agente que opere la plataforma.

## 1) Visión integral del producto/plataforma

Aventide opera como una plataforma transaccional multi-dominio y multi-país que integra:

- ciclo completo de demanda-oferta (`search` → `orders`),
- manejo de dinero (`payments` → `rate-engine` → `waterfall` → `billing-docs`),
- confianza y control (`disputes`, `audit`, `security`, `moderation`, reputación),
- operación y resiliencia (`observability`, `continuity`, `backup`, `integrations`, `files`),
- capa normativa por país (`docs/03-COUNTRY-POLICIES`).

La arquitectura documental está organizada por **38 dominios canónicos** y conserva los `.docx` en `Sistemas/` como respaldo histórico controlado.

## 2) Mapa de sistemas (38)

### 2.1 Dominios canónicos

`analytics`, `audit`, `backup`, `billing-docs`, `capacity`, `content`, `continuity`, `coupons`, `coverage`, `disputes`, `files`, `genie`, `geo-intelligence-map`, `governance-cameleon`, `hierarchy`, `integrations`, `internal-credit`, `loyalty`, `memory`, `messaging`, `moderation`, `neighborhoods`, `notifications`, `observability`, `orders`, `payments`, `platform-structure`, `rate-engine`, `referrals`, `reputation-buyer`, `reputation-seller`, `reservas-country`, `reservas-global`, `search`, `security`, `support`, `users`, `waterfall`.

### 2.2 Núcleos funcionales

- **Core transaccional:** `search`, `coverage`, `capacity`, `orders`, `payments`.
- **Core de monetización:** `rate-engine`, `waterfall`, `billing-docs`, `coupons`, `loyalty`, `referrals`, `internal-credit`.
- **Core de riesgo/confianza:** `disputes`, `audit`, `security`, `moderation`, `reputation-buyer`, `reputation-seller`, `reservas-*`.
- **Core de plataforma/operación:** `platform-structure`, `integrations`, `files`, `backup`, `continuity`, `observability`.
- **Core de experiencia y crecimiento:** `users`, `hierarchy`, `messaging`, `notifications`, `support`, `content`, `genie`, `memory`, `analytics`, `geo-intelligence-map`, `governance-cameleon`, `neighborhoods`.

## 3) Flujos E2E críticos

### 3.1 Flujo money-critical principal

1. **Order** (`orders`): creación, reserva lógica de capacidad y reglas de elegibilidad.
2. **Payment** (`payments`): autorización/captura y emisión de eventos de pago.
3. **Escrow/Reservas** (`reservas-country`/`reservas-global`): retención temporal y garantías operativas/regulatorias.
4. **Dispute** (`disputes`): gestión de reclamos, evidencias y decisiones de resolución.
5. **Settlement** (`rate-engine` + `waterfall` + `billing-docs`): cálculo de distribución, liquidación y documentación fiscal.

### 3.2 Controles transversales obligatorios

- Auditoría y trazabilidad (`audit`, `observability`).
- Políticas país (`docs/03-COUNTRY-POLICIES/*`).
- Seguridad, fraude y permisos (`security`, `governance-cameleon`).

## 4) Límites de bounded contexts

- **BC-Identity & Access:** `users`, `hierarchy`, `security`.
- **BC-Marketplace Execution:** `search`, `coverage`, `capacity`, `orders`, `neighborhoods`.
- **BC-Money Movement:** `payments`, `internal-credit`, `coupons`, `loyalty`, `referrals`.
- **BC-Revenue & Settlement:** `rate-engine`, `waterfall`, `billing-docs`.
- **BC-Risk & Trust:** `disputes`, `reservas-country`, `reservas-global`, reputación, moderación, auditoría.
- **BC-Engagement & Support:** `messaging`, `notifications`, `support`, `content`, `genie`, `memory`.
- **BC-Platform Reliability:** `platform-structure`, `integrations`, `files`, `backup`, `continuity`, `observability`, `analytics`.
- **BC-Governance & Geo:** `governance-cameleon`, `geo-intelligence-map`.

Regla de diseño: interacción entre BCs solo por contratos (`API_CONTRACTS.md`, `EVENT_CONTRACTS.md`, `DATA_CONTRACTS.md`) y decisiones ADR.

## 5) Gobernanza multi-país

- Marco base: `docs/03-COUNTRY-POLICIES/README.md`.
- Implementación actual: Colombia (`CO`) y República Dominicana (`DO`) con `README`, `POLICY_OVERRIDES`, `COMPLIANCE_CHECKLIST` y `RISK_NOTES` por país.
- En producción, cualquier cambio de contrato o runbook que impacte operación/regulación debe reflejarse en la política país correspondiente antes de release.

## 6) Riesgos de producción (top)

1. **Desalineación contratos vs policy país.**
2. **Errores en cadena de settlement (`payments`/`rate-engine`/`waterfall`).**
3. **Cobertura/capacidad inconsistente con asignación de órdenes.**
4. **Incidentes de seguridad o permisos en identidades/integraciones.**
5. **Brechas de observabilidad que impidan auditoría forense.**

Mitigación mínima: gates de despliegue (`docs/05-DEPLOY-GATES.md`), runbooks por dominio, ADR vigente y checklist país al día.

## 7) Checklist go-live global

- [ ] Contratos API/DATA/EVENT actualizados en todos los dominios impactados.
- [ ] Runbooks validados con simulación de incidente para flujos críticos.
- [ ] ADR de cambios de arquitectura aprobado.
- [ ] Country policy (`CO`/`DO` y países objetivo) revisada y firmada.
- [ ] Pruebas E2E de `order → payment → escrow → dispute → settlement` completas.
- [ ] Trazabilidad audit-ready y métricas de observabilidad habilitadas.
- [ ] Plan de continuidad/backup probado para RTO/RPO objetivo.

## 8) Matriz de trazabilidad total

> Formato: **cada sistema `.docx` → dominio canónico → contratos → runbook → policy país → ADR**.

| Sistema `.docx` | Dominio canónico | Contratos | Runbook | Policy país | ADR |
|---|---|---|---|---|---|

| `Sistema Gobernanza multi-país + App Camaleón.docx` | `governance-cameleon` | `docs/02-DOMAINS/governance-cameleon/API_CONTRACTS.md`<br>`docs/02-DOMAINS/governance-cameleon/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/governance-cameleon/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/governance-cameleon/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/governance-cameleon/ADR/0001-contexto-y-decisiones.md` |
| `disputas-260207_0809.docx` | `disputes` | `docs/02-DOMAINS/disputes/API_CONTRACTS.md`<br>`docs/02-DOMAINS/disputes/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/disputes/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/disputes/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/disputes/ADR/0001-contexto-y-decisiones.md` |
| `estructura-v2-260207_1049.docx` | `platform-structure` | `docs/02-DOMAINS/platform-structure/API_CONTRACTS.md`<br>`docs/02-DOMAINS/platform-structure/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/platform-structure/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/platform-structure/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/platform-structure/ADR/0001-contexto-y-decisiones.md` |
| `facturacion--documentos-260207_0805.docx` | `billing-docs` | `docs/02-DOMAINS/billing-docs/API_CONTRACTS.md`<br>`docs/02-DOMAINS/billing-docs/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/billing-docs/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/billing-docs/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/billing-docs/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-analitica-260206_2336.docx` | `analytics` | `docs/02-DOMAINS/analytics/API_CONTRACTS.md`<br>`docs/02-DOMAINS/analytics/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/analytics/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/analytics/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/analytics/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-archivos-260207_0840.docx` | `files` | `docs/02-DOMAINS/files/API_CONTRACTS.md`<br>`docs/02-DOMAINS/files/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/files/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/files/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/files/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-auditoria-260207_0947.docx` | `audit` | `docs/02-DOMAINS/audit/API_CONTRACTS.md`<br>`docs/02-DOMAINS/audit/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/audit/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/audit/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/audit/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-barrio-260207_1012.docx` | `neighborhoods` | `docs/02-DOMAINS/neighborhoods/API_CONTRACTS.md`<br>`docs/02-DOMAINS/neighborhoods/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/neighborhoods/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/neighborhoods/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/neighborhoods/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-busqueda-260207_0312.docx` | `search` | `docs/02-DOMAINS/search/API_CONTRACTS.md`<br>`docs/02-DOMAINS/search/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/search/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/search/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/search/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-capacidad--disponibilidad-260207_0922.docx` | `capacity` | `docs/02-DOMAINS/capacity/API_CONTRACTS.md`<br>`docs/02-DOMAINS/capacity/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/capacity/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/capacity/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/capacity/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-cobertura-260207_0907.docx` | `coverage` | `docs/02-DOMAINS/coverage/API_CONTRACTS.md`<br>`docs/02-DOMAINS/coverage/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/coverage/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/coverage/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/coverage/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-contenido-260206_2344.docx` | `content` | `docs/02-DOMAINS/content/API_CONTRACTS.md`<br>`docs/02-DOMAINS/content/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/content/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/content/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/content/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-continuidad-v2-260207_1030.docx` | `continuity` | `docs/02-DOMAINS/continuity/API_CONTRACTS.md`<br>`docs/02-DOMAINS/continuity/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/continuity/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/continuity/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/continuity/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-copia-de-seguridad-260207_0955.docx` | `backup` | `docs/02-DOMAINS/backup/API_CONTRACTS.md`<br>`docs/02-DOMAINS/backup/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/backup/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/backup/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/backup/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-credito-interno-260207_0827.docx` | `internal-credit` | `docs/02-DOMAINS/internal-credit/API_CONTRACTS.md`<br>`docs/02-DOMAINS/internal-credit/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/internal-credit/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/internal-credit/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/internal-credit/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-cupones-260207_0826.docx` | `coupons` | `docs/02-DOMAINS/coupons/API_CONTRACTS.md`<br>`docs/02-DOMAINS/coupons/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/coupons/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/coupons/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/coupons/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-genie-260207_1012.docx` | `genie` | `docs/02-DOMAINS/genie/API_CONTRACTS.md`<br>`docs/02-DOMAINS/genie/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/genie/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/genie/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/genie/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-integraciones-260207_0951.docx` | `integrations` | `docs/02-DOMAINS/integrations/API_CONTRACTS.md`<br>`docs/02-DOMAINS/integrations/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/integrations/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/integrations/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/integrations/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-jerarqua-260206_2015.docx` | `hierarchy` | `docs/02-DOMAINS/hierarchy/API_CONTRACTS.md`<br>`docs/02-DOMAINS/hierarchy/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/hierarchy/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/hierarchy/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/hierarchy/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-lealtad-260207_0817.docx` | `loyalty` | `docs/02-DOMAINS/loyalty/API_CONTRACTS.md`<br>`docs/02-DOMAINS/loyalty/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/loyalty/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/loyalty/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/loyalty/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-memory-260207_1012.docx` | `memory` | `docs/02-DOMAINS/memory/API_CONTRACTS.md`<br>`docs/02-DOMAINS/memory/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/memory/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/memory/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/memory/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-mensajeria-260207_0925.docx` | `messaging` | `docs/02-DOMAINS/messaging/API_CONTRACTS.md`<br>`docs/02-DOMAINS/messaging/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/messaging/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/messaging/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/messaging/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-moderacion-260207_0828.docx` | `moderation` | `docs/02-DOMAINS/moderation/API_CONTRACTS.md`<br>`docs/02-DOMAINS/moderation/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/moderation/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/moderation/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/moderation/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-notificaciones-260207_0929.docx` | `notifications` | `docs/02-DOMAINS/notifications/API_CONTRACTS.md`<br>`docs/02-DOMAINS/notifications/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/notifications/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/notifications/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/notifications/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-observalidad-260207_0755.docx` | `observability` | `docs/02-DOMAINS/observability/API_CONTRACTS.md`<br>`docs/02-DOMAINS/observability/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/observability/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/observability/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/observability/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-ordenes-260207_0037.docx` | `orders` | `docs/02-DOMAINS/orders/API_CONTRACTS.md`<br>`docs/02-DOMAINS/orders/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/orders/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/orders/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/orders/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-pagos-260207_0800.docx` | `payments` | `docs/02-DOMAINS/payments/API_CONTRACTS.md`<br>`docs/02-DOMAINS/payments/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/payments/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/payments/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/payments/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-referido-260207_0826.docx` | `referrals` | `docs/02-DOMAINS/referrals/API_CONTRACTS.md`<br>`docs/02-DOMAINS/referrals/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/referrals/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/referrals/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/referrals/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-reputacion-buyer-260207_0839.docx` | `reputation-buyer` | `docs/02-DOMAINS/reputation-buyer/API_CONTRACTS.md`<br>`docs/02-DOMAINS/reputation-buyer/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/reputation-buyer/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/reputation-buyer/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/reputation-buyer/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-reputacion-seller-260207_0839.docx` | `reputation-seller` | `docs/02-DOMAINS/reputation-seller/API_CONTRACTS.md`<br>`docs/02-DOMAINS/reputation-seller/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/reputation-seller/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/reputation-seller/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/reputation-seller/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-reserva-global-260207_1041.docx` | `reservas-global` | `docs/02-DOMAINS/reservas-global/API_CONTRACTS.md`<br>`docs/02-DOMAINS/reservas-global/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/reservas-global/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/reservas-global/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/reservas-global/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-reserva-nacional-260207_1031.docx` | `reservas-country` | `docs/02-DOMAINS/reservas-country/API_CONTRACTS.md`<br>`docs/02-DOMAINS/reservas-country/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/reservas-country/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/reservas-country/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/reservas-country/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-seguridad-260207_0756.docx` | `security` | `docs/02-DOMAINS/security/API_CONTRACTS.md`<br>`docs/02-DOMAINS/security/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/security/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/security/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/security/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-soporte-260207_0731.docx` | `support` | `docs/02-DOMAINS/support/API_CONTRACTS.md`<br>`docs/02-DOMAINS/support/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/support/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/support/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/support/ADR/0001-contexto-y-decisiones.md` |
| `sistema-de-usuarios-260206_2328.docx` | `users` | `docs/02-DOMAINS/users/API_CONTRACTS.md`<br>`docs/02-DOMAINS/users/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/users/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/users/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/users/ADR/0001-contexto-y-decisiones.md` |
| `sistema-geo-intelligence-map-260207_1103.docx` | `geo-intelligence-map` | `docs/02-DOMAINS/geo-intelligence-map/API_CONTRACTS.md`<br>`docs/02-DOMAINS/geo-intelligence-map/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/geo-intelligence-map/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/geo-intelligence-map/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/geo-intelligence-map/ADR/0001-contexto-y-decisiones.md` |
| `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx` | `rate-engine` | `docs/02-DOMAINS/rate-engine/API_CONTRACTS.md`<br>`docs/02-DOMAINS/rate-engine/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/rate-engine/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/rate-engine/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/rate-engine/ADR/0001-contexto-y-decisiones.md` |
| `waterfall-engine-v10-260207_0941.docx` | `waterfall` | `docs/02-DOMAINS/waterfall/API_CONTRACTS.md`<br>`docs/02-DOMAINS/waterfall/DATA_CONTRACTS.md`<br>`docs/02-DOMAINS/waterfall/EVENT_CONTRACTS.md` | `docs/02-DOMAINS/waterfall/RUNBOOKS.md` | `docs/03-COUNTRY-POLICIES/README.md`<br>`docs/03-COUNTRY-POLICIES/CO/README.md`<br>`docs/03-COUNTRY-POLICIES/DO/README.md` | `docs/02-DOMAINS/waterfall/ADR/0001-contexto-y-decisiones.md` |


## 9) Supuestos, incoherencias resueltas y decisiones pendientes

### 9.1 Supuestos explícitos

- El set de 38 dominios canónicos publicado en `docs/02-DOMAINS/README.md` es la referencia oficial.
- Todo dominio canónico mantiene contrato triple (API/DATA/EVENT), `RUNBOOKS.md` y ADR base.
- Las políticas país vigentes iniciales son `CO` y `DO`; nuevos países heredan el mismo patrón de artefactos.

### 9.2 Incoherencias resueltas

- Se resolvió la coexistencia legacy vs canónico mediante mapeo 1:1 y aliases de compatibilidad.
- Se normalizaron nombres con errores históricos (`jerarqua`, `observalidad`) manteniendo redirecciones legacy.
- Se estableció una sola cadena E2E para money flow con checkpoints de riesgo/operación.

### 9.3 Decisiones pendientes

- Definir criterio formal de “listo para retiro de `/Sistemas`” con evidencia automatizable por dominio.
- Versionado semántico de contratos cross-domain para cambios incompatibles.
- Política de expansión multi-país (orden de países, controles mínimos, ownership legal-operativo).
- Estándar de pruebas de caos y DR para dominios money-critical.

## 10) Uso operacional de este blueprint

- **Onboarding técnico (humano):** primera lectura + navegación a dominios y runbooks.
- **Onboarding operativo (humano):** primera lectura + políticas país + checklist go-live.
- **Onboarding IA/agentes:** este archivo define el mapa maestro, prioridades de flujo y puntos de control normativo.

> Cualquier iniciativa nueva debe comenzar aquí y luego descender a contratos, runbooks, policy país y ADR del dominio impactado.
