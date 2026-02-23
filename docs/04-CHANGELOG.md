# 04 - CHANGELOG

Este changelog se mantiene por entrada y **debe** actualizarse en cada cambio de dominio.

## Regla operativa obligatoria

> **Ningún cambio de dominio se acepta sin actualizar este changelog y `docs/05-DEPLOY-GATES.md`.**

## Formato requerido por entrada

Cada entrada debe incluir:

1. **Fecha** (`YYYY-MM-DD`)
2. **Dominio** (ej.: Órdenes, Pagos, Auditoría)
3. **Tipo de cambio** (`breaking` o `non-breaking`)
4. **ADR relacionada** (ID o link)
5. **Migraciones requeridas** (sí/no + detalle)
6. **Release ID** (`YYYY-MM-DD-release-id`)
7. **Estado de aprobación del release** (`aprobado|pendiente|rechazado`)

## Plantilla de registro

```md
### [YYYY-MM-DD] - <Dominio> - <breaking|non-breaking>
- **Resumen:** <qué cambió y por qué>
- **ADR relacionada:** <ADR-XXX o URL>
- **Migraciones requeridas:** <Sí/No>
- **Detalle de migraciones:** <pasos, scripts, orden de ejecución, ventana>
- **Impacto esperado:** <servicios, países, equipos>
- **Release ID:** <YYYY-MM-DD-release-id>
- **Estado de aprobación del release:** <aprobado|pendiente|rechazado>
- **Registro de gate:** <ruta o URL al archivo en docs/releases/>
- **Rollback:** <estrategia y condiciones de reversa>
```

## Entradas

### [2026-02-20] - Gobernanza de documentación de release - non-breaking
- **Resumen:** Se formaliza el estándar de changelog y gates de despliegue con regla operativa de cumplimiento obligatorio.
- **ADR relacionada:** Pendiente (`ADR-TO-BE-ASSIGNED`)
- **Migraciones requeridas:** No
- **Detalle de migraciones:** No aplica.
- **Impacto esperado:** Estandarización de releases en todos los dominios y países.
- **Release ID:** 2026-02-20-doc-governance-baseline
- **Estado de aprobación del release:** aprobado
- **Registro de gate:** `docs/releases/2026-02-20-doc-governance-baseline.md`
- **Rollback:** Revertir cambios documentales si se reemplaza por un estándar superior aprobado por arquitectura.


### [2026-02-23] - Documentación transcrita 38/38 de sistemas históricos - non-breaking
- **Resumen:** Se crea `docs/07-SISTEMAS-TRANSCRITOS/` con 38 archivos `.md` (uno por sistema histórico en `Sistemas/*.docx`) y un índice de cobertura integral para lectura IA/humana sin depender del formato `.docx`.
- **ADR relacionada:** [ADR-STR-001](./01-ADR/ADR-STR-001-criterio-retiro-sistemas.md)
- **Migraciones requeridas:** No
- **Detalle de migraciones:** No aplica (cambio documental).
- **Impacto esperado:** Mejora de trazabilidad y accesibilidad documental cross-domain; se mantiene compatibilidad con fuentes históricas.
- **Release ID:** 2026-02-23-sistemas-transcritos-38x38
- **Estado de aprobación del release:** pendiente
- **Registro de gate:** `docs/releases/2026-02-23-sistemas-transcritos-38x38.md`
- **Rollback:** Eliminar `docs/07-SISTEMAS-TRANSCRITOS/` y revertir referencias en `docs/00-INDEX.md` y `docs/06-MASTER-BLUEPRINT.md`.
