# 00 · Índice Maestro del Sistema

> **Ubicación de fuentes históricas:** los 38 archivos `.docx` están en `Sistemas/*.docx`.

## Enlaces de navegación

- [01-GLOSSARY](./01-GLOSSARY.md)
- [02-DOMAINS](./02-DOMAINS/)
- [03-COUNTRY-POLICIES](./03-COUNTRY-POLICIES/)
- [04-CHANGELOG](./04-CHANGELOG.md)
- [05-DEPLOY-GATES](./05-DEPLOY-GATES.md)

---

## 1) Inventario completo (38 fuentes)

## 1.1) Política de transición de fuentes

- **Fase A (vigente como respaldo histórico):** los `.docx` en `Sistemas/*.docx` se conservan como respaldo de origen.
- **Fase B (vigente como fuente operativa):** la documentación canónica en `docs/` y `docs/02-DOMAINS/*` es la fuente de trabajo para operación, cambios y revisiones.
- **Fase C (objetivo):** retiro de `/Sistemas` cuando todos los dominios cumplan criterios de paridad y exista validación integral registrada.

## 1.2) Criterios de paridad para retirar `/Sistemas`

Un sistema se considera en paridad cuando su dominio canónico demuestra, como mínimo:

1. **Cobertura funcional:** el `README.md` describe alcance, límites y casos principales del dominio.
2. **Contratos:** existen y están actualizados `API_CONTRACTS.md`, `DATA_CONTRACTS.md` y `EVENT_CONTRACTS.md`.
3. **Invariantes:** `INVARIANTS.md` define reglas no negociables de consistencia y seguridad.
4. **Runbooks:** `RUNBOOKS.md` documenta operación normal e incident response del dominio.
5. **Políticas país:** cuando aplica, la regulación/operación multi-país está reflejada en `docs/03-COUNTRY-POLICIES/` y enlazada desde el dominio.
6. **ADR:** las decisiones de arquitectura relevantes están registradas y referenciadas desde el dominio.

## 1.3) Estado de transición por sistema

Estados permitidos: `pendiente` · `parcial` · `validado` · `listo para retiro docx`.

| Sistema (.docx en `Sistemas/`) | Dominio canónico | Estado |
|---|---|---|
| `Sistema Gobernanza multi-país + App Camaleón.docx` | `governance-cameleon` | `validado` |
| `disputas-260207_0809.docx` | `disputes` | `validado` |
| `estructura-v2-260207_1049.docx` | `platform-structure` | `validado` |
| `facturacion--documentos-260207_0805.docx` | `billing-docs` | `validado` |
| `sistema-de-analitica-260206_2336.docx` | `analytics` | `validado` |
| `sistema-de-archivos-260207_0840.docx` | `files` | `validado` |
| `sistema-de-auditoria-260207_0947.docx` | `audit` | `validado` |
| `sistema-de-barrio-260207_1012.docx` | `neighborhoods` | `validado` |
| `sistema-de-busqueda-260207_0312.docx` | `search` | `validado` |
| `sistema-de-capacidad--disponibilidad-260207_0922.docx` | `capacity` | `validado` |
| `sistema-de-cobertura-260207_0907.docx` | `coverage` | `validado` |
| `sistema-de-contenido-260206_2344.docx` | `content` | `validado` |
| `sistema-de-continuidad-v2-260207_1030.docx` | `continuity` | `validado` |
| `sistema-de-copia-de-seguridad-260207_0955.docx` | `backup` | `validado` |
| `sistema-de-credito-interno-260207_0827.docx` | `internal-credit` | `validado` |
| `sistema-de-cupones-260207_0826.docx` | `coupons` | `validado` |
| `sistema-de-genie-260207_1012.docx` | `genie` | `validado` |
| `sistema-de-integraciones-260207_0951.docx` | `integrations` | `validado` |
| `sistema-de-jerarqua-260206_2015.docx` | `hierarchy` | `validado` |
| `sistema-de-lealtad-260207_0817.docx` | `loyalty` | `validado` |
| `sistema-de-memory-260207_1012.docx` | `memory` | `validado` |
| `sistema-de-mensajeria-260207_0925.docx` | `messaging` | `validado` |
| `sistema-de-moderacion-260207_0828.docx` | `moderation` | `validado` |
| `sistema-de-notificaciones-260207_0929.docx` | `notifications` | `validado` |
| `sistema-de-observalidad-260207_0755.docx` | `observability` | `validado` |
| `sistema-de-ordenes-260207_0037.docx` | `orders` | `validado` |
| `sistema-de-pagos-260207_0800.docx` | `payments` | `validado` |
| `sistema-de-referido-260207_0826.docx` | `referrals` | `validado` |
| `sistema-de-reputacion-buyer-260207_0839.docx` | `reputation-buyer` | `validado` |
| `sistema-de-reputacion-seller-260207_0839.docx` | `reputation-seller` | `validado` |
| `sistema-de-reserva-global-260207_1041.docx` | `reservas-global` | `validado` |
| `sistema-de-reserva-nacional-260207_1031.docx` | `reservas-country` | `validado` |
| `sistema-de-seguridad-260207_0756.docx` | `security` | `validado` |
| `sistema-de-soporte-260207_0731.docx` | `support` | `validado` |
| `sistema-de-usuarios-260206_2328.docx` | `users` | `validado` |
| `sistema-geo-intelligence-map-260207_1103.docx` | `geo-intelligence-map` | `validado` |
| `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx` | `rate-engine` | `validado` |
| `waterfall-engine-v10-260207_0941.docx` | `waterfall` | `validado` |

**Última validación integral:** 2026-02-20 · Responsable: Equipo de Arquitectura Documental.

| # | Nombre actual (.docx) | Slug canónico |
|---|---|---|
| 1 | `Sistema Gobernanza multi-país + App Camaleón.docx` | `governance-multi-country-camaleon-app` |
| 2 | `disputas-260207_0809.docx` | `disputas` |
| 3 | `estructura-v2-260207_1049.docx` | `estructura-v2` |
| 4 | `facturacion--documentos-260207_0805.docx` | `facturacion-documentos` |
| 5 | `sistema-de-analitica-260206_2336.docx` | `sistema-de-analitica` |
| 6 | `sistema-de-archivos-260207_0840.docx` | `sistema-de-archivos` |
| 7 | `sistema-de-auditoria-260207_0947.docx` | `sistema-de-auditoria` |
| 8 | `sistema-de-barrio-260207_1012.docx` | `sistema-de-barrio` |
| 9 | `sistema-de-busqueda-260207_0312.docx` | `sistema-de-busqueda` |
| 10 | `sistema-de-capacidad--disponibilidad-260207_0922.docx` | `sistema-de-capacidad-disponibilidad` |
| 11 | `sistema-de-cobertura-260207_0907.docx` | `sistema-de-cobertura` |
| 12 | `sistema-de-contenido-260206_2344.docx` | `sistema-de-contenido` |
| 13 | `sistema-de-continuidad-v2-260207_1030.docx` | `sistema-de-continuidad-v2` |
| 14 | `sistema-de-copia-de-seguridad-260207_0955.docx` | `sistema-de-copia-de-seguridad` |
| 15 | `sistema-de-credito-interno-260207_0827.docx` | `sistema-de-credito-interno` |
| 16 | `sistema-de-cupones-260207_0826.docx` | `sistema-de-cupones` |
| 17 | `sistema-de-genie-260207_1012.docx` | `sistema-de-genie` |
| 18 | `sistema-de-integraciones-260207_0951.docx` | `sistema-de-integraciones` |
| 19 | `sistema-de-jerarqua-260206_2015.docx` | `sistema-de-jerarquia` |
| 20 | `sistema-de-lealtad-260207_0817.docx` | `sistema-de-lealtad` |
| 21 | `sistema-de-memory-260207_1012.docx` | `sistema-de-memory` |
| 22 | `sistema-de-mensajeria-260207_0925.docx` | `sistema-de-mensajeria` |
| 23 | `sistema-de-moderacion-260207_0828.docx` | `sistema-de-moderacion` |
| 24 | `sistema-de-notificaciones-260207_0929.docx` | `sistema-de-notificaciones` |
| 25 | `sistema-de-observalidad-260207_0755.docx` | `sistema-de-observabilidad` |
| 26 | `sistema-de-ordenes-260207_0037.docx` | `sistema-de-ordenes` |
| 27 | `sistema-de-pagos-260207_0800.docx` | `sistema-de-pagos` |
| 28 | `sistema-de-referido-260207_0826.docx` | `sistema-de-referido` |
| 29 | `sistema-de-reputacion-buyer-260207_0839.docx` | `sistema-de-reputacion-buyer` |
| 30 | `sistema-de-reputacion-seller-260207_0839.docx` | `sistema-de-reputacion-seller` |
| 31 | `sistema-de-reserva-global-260207_1041.docx` | `sistema-de-reserva-global` |
| 32 | `sistema-de-reserva-nacional-260207_1031.docx` | `sistema-de-reserva-nacional` |
| 33 | `sistema-de-seguridad-260207_0756.docx` | `sistema-de-seguridad` |
| 34 | `sistema-de-soporte-260207_0731.docx` | `sistema-de-soporte` |
| 35 | `sistema-de-usuarios-260206_2328.docx` | `sistema-de-usuarios` |
| 36 | `sistema-geo-intelligence-map-260207_1103.docx` | `sistema-geo-intelligence-map` |
| 37 | `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx` | `take-rate-revenue-rate-engine-v20` |
| 38 | `waterfall-engine-v10-260207_0941.docx` | `waterfall-engine-v10` |

---

## 2) Clasificación por dominio

- **Identity & Access:** `sistema-de-usuarios`, `sistema-de-jerarquia`, `sistema-de-seguridad`.
- **Orders & Fulfillment:** `sistema-de-ordenes`, `sistema-de-barrio`, `sistema-de-cobertura`, `sistema-de-capacidad-disponibilidad`.
- **Payments & Revenue:** `sistema-de-pagos`, `take-rate-revenue-rate-engine-v20`, `waterfall-engine-v10`, `sistema-de-credito-interno`, `sistema-de-cupones`, `sistema-de-lealtad`, `sistema-de-referido`, `facturacion-documentos`.
- **Risk, Trust & Compliance:** `disputas`, `sistema-de-reserva-global`, `sistema-de-reserva-nacional`, `sistema-de-auditoria`, `sistema-de-reputacion-buyer`, `sistema-de-reputacion-seller`, `sistema-de-moderacion`.
- **Support & CX:** `sistema-de-soporte`, `sistema-de-mensajeria`, `sistema-de-notificaciones`.
- **Geo & Discovery:** `sistema-geo-intelligence-map`, `sistema-de-busqueda`.
- **Platform & Operations:** `estructura-v2`, `sistema-de-integraciones`, `sistema-de-observabilidad`, `sistema-de-continuidad-v2`, `sistema-de-copia-de-seguridad`, `sistema-de-archivos`.
- **Content & Knowledge:** `sistema-de-contenido`, `sistema-de-memory`, `sistema-de-genie`, `sistema-de-analitica`.
- **Governance:** `governance-multi-country-camaleon-app`.

---

## 3) Etiquetas de criticidad

- **`money-critical`:** `sistema-de-pagos`, `take-rate-revenue-rate-engine-v20`, `waterfall-engine-v10`, `facturacion-documentos`, `sistema-de-credito-interno`, `sistema-de-cupones`, `sistema-de-lealtad`, `sistema-de-referido`, `sistema-de-reserva-global`, `sistema-de-reserva-nacional`, `disputas`.
- **`policy-critical`:** `governance-multi-country-camaleon-app`, `sistema-de-soporte`, `sistema-de-moderacion`, `sistema-de-reputacion-buyer`, `sistema-de-reputacion-seller`, `sistema-geo-intelligence-map`, `sistema-de-cobertura`.
- **`security-critical`:** `sistema-de-seguridad`, `sistema-de-usuarios`, `sistema-de-jerarquia`, `sistema-de-auditoria`, `sistema-de-integraciones`, `sistema-de-archivos`, `sistema-de-copia-de-seguridad`.
- **`ops-critical`:** `estructura-v2`, `sistema-de-observabilidad`, `sistema-de-continuidad-v2`, `sistema-de-capacidad-disponibilidad`, `sistema-de-ordenes`, `sistema-de-notificaciones`, `sistema-de-mensajeria`.

---

## 4) Ruta de lectura recomendada (onboarding)

### Día 1 · Panorama y fundamentos
1. `estructura-v2`
2. `governance-multi-country-camaleon-app`
3. `sistema-de-usuarios`
4. `sistema-de-seguridad`
5. `sistema-de-ordenes`
6. `sistema-de-pagos`

### Día 2 · Dinero, riesgo y operación
1. `take-rate-revenue-rate-engine-v20`
2. `waterfall-engine-v10`
3. `disputas`
4. `sistema-de-reserva-nacional`
5. `sistema-de-reserva-global`
6. `sistema-de-auditoria`
7. `sistema-de-observabilidad`

### Día 3 · Escala, país y experiencia
1. `sistema-geo-intelligence-map`
2. `sistema-de-cobertura`
3. `sistema-de-capacidad-disponibilidad`
4. `sistema-de-soporte`
5. `sistema-de-notificaciones`
6. `sistema-de-integraciones`
7. `sistema-de-continuidad-v2`

---

## 5) Mapa de dependencias de alto nivel

```text
identity/seguridad
  -> órdenes
    -> pagos
      -> take-rate/revenue-rate
        -> waterfall
          -> facturación
            -> disputas
              -> reservas (nacional/global)
                -> auditoría/compliance
                  -> analítica/observabilidad

geo/cobertura/capacidad
  -> asignación de órdenes
    -> reputación/moderación
      -> soporte/mensajería/notificaciones

integraciones/archivos/backup/continuidad
  -> resiliencia operativa transversal
```

## 6) Convención de normalización aplicada

- Se removió sufijo de timestamp (`-YYMMDD_HHMM`) para definir slugs.
- Se unificaron separadores múltiples (`--` → `-`).
- Se normalizó ortografía de slug en casos obvios (`jerarqua` → `jerarquia`, `observalidad` → `observabilidad`).
- Los `.docx` permanecen intactos como **source-of-truth** inicial.

## 7) Regla de naming para nuevos dominios

- **No crear nuevos dominios bajo naming legacy** (por ejemplo: `sistema-de-*`, `facturacion--documentos`, `disputas`, `waterfall-engine-v10`).
- Al crear o mover documentación, usar exclusivamente el slug canónico publicado en `docs/02-DOMAINS/README.md`.
