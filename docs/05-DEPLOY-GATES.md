# 05 - DEPLOY GATES

Checklist mínimo obligatorio para aprobar despliegues en producción.

## Regla operativa obligatoria

> **Ningún cambio de dominio se acepta sin actualizar `docs/04-CHANGELOG.md` y este documento de gates.**

## Gates mínimos

1. **Invariantes no violados.**
   - Evidencia: pruebas, métricas o validaciones automáticas/manuales.
2. **Contratos API/Event/Data versionados.**
   - Evidencia: versionado explícito, compatibilidad y consumidores identificados.
3. **Runbooks actualizados.**
   - Evidencia: operación, troubleshooting, on-call y escalamiento.
4. **Country policies validadas.**
   - Evidencia: validación legal/fiscal/regulatoria por país afectado.
5. **Riesgo y rollback definidos.**
   - Evidencia: nivel de riesgo, blast radius, estrategia de reversa y RTO/RPO objetivo.
6. **Auditoría/eventos críticos verificados.**
   - Evidencia: trazabilidad, logs, alertas y eventos críticos emitidos correctamente.

## Plantilla de aprobación por release

```md
### Release: <id>
- [ ] Gate 1: Invariantes no violados.
- [ ] Gate 2: Contratos API/Event/Data versionados.
- [ ] Gate 3: Runbooks actualizados.
- [ ] Gate 4: Country policies validadas.
- [ ] Gate 5: Riesgo y rollback definidos.
- [ ] Gate 6: Auditoría/eventos críticos verificados.
- **Aprobador técnico:** <nombre>
- **Aprobador de negocio/regulatorio:** <nombre>
- **Fecha/hora:** <UTC>
- **Notas:** <observaciones>
```
