# 05 - DEPLOY GATES

Checklist mínimo obligatorio para aprobar despliegues en producción.

## Regla operativa obligatoria

> **Ningún cambio de dominio se acepta sin actualizar `docs/04-CHANGELOG.md` y registrar un gate por release en `docs/releases/`.**

## Gates mínimos

1. **Invariantes no violados.**
   - Evidencia: pruebas, métricas o validaciones automáticas/manuales.
2. **Contratos API/Event/Data versionados.**
   - Evidencia: versionado explícito, compatibilidad y consumidores identificados.
3. **Runbooks actualizados (incluye `Ownership & Escalation`).**
   - Evidencia: owner técnico, owner negocio/regulatorio, rotación on-call y matriz SEV0/SEV1/SEV2 con tiempos de respuesta alineados a `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.
4. **Country policies validadas.**
   - Evidencia: validación legal/fiscal/regulatoria por país afectado.
5. **Riesgo y rollback definidos.**
   - Evidencia: nivel de riesgo, blast radius, estrategia de reversa y RTO/RPO objetivo.
6. **Auditoría/eventos críticos verificados.**
   - Evidencia: trazabilidad, logs, alertas y eventos críticos emitidos correctamente.

## Plantilla de aprobación por release

Cada release debe tener su propio archivo en `docs/releases/` con formato `YYYY-MM-DD-release-id.md`.

Además, cada gate de release debe incluir **enlaces concretos** (URL) a evidencia de:

- dashboard/observabilidad del cambio,
- incident drill o simulacro ejecutado,
- pruebas E2E relevantes,
- aprobaciones legales/regulatorias por país.

```md
### Release: <id>
- [ ] Gate 1: Invariantes no violados.
- [ ] Gate 2: Contratos API/Event/Data versionados.
- [ ] Gate 3: Runbooks actualizados.
- [ ] Gate 4: Country policies validadas.
- [ ] Gate 5: Riesgo y rollback definidos.
- [ ] Gate 6: Auditoría/eventos críticos verificados.
- **Dashboard:** [enlace](https://...)
- **Incident Drill:** [enlace](https://...)
- **Pruebas E2E:** [enlace](https://...)
- **Aprobación legal/regulatoria:** [enlace](https://...)
- **Aprobador técnico:** <nombre>
- **Aprobador de negocio/regulatorio:** <nombre>
- **Estado de aprobación:** <aprobado|pendiente|rechazado>
- **Fecha/hora:** <UTC>
- **Notas:** <observaciones>
```
