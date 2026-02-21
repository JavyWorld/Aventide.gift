# Estándar transversal · Severidades, SLAs operativos y handoff

Documento normativo único para todos los dominios canónicos en `docs/02-DOMAINS/*`.

## 1) Objetivo y alcance

- Definir un lenguaje único de incidentes (`SEV0`, `SEV1`, `SEV2`).
- Establecer SLAs operativos mínimos de respuesta y comunicación.
- Estandarizar el handoff entre equipos técnicos, negocio y regulación/compliance.

## 2) Matriz única de severidades

| Severidad | Criterio de impacto | Ack inicial | Mitigación/contención objetivo | Cadencia de actualización | Escalamiento mínimo |
| --- | --- | --- | --- | --- | --- |
| **SEV0** | Interrupción total de flujo crítico, riesgo regulatorio grave, pérdida financiera activa o brecha de seguridad crítica. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min | IC + owner técnico + owner negocio/regulatorio + liderazgo ejecutivo |
| **SEV1** | Degradación severa con impacto alto en usuarios/transacciones, sin caída total. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min | IC + owner técnico + owner negocio/regulatorio |
| **SEV2** | Impacto parcial o degradación moderada con workaround. | ≤ 30 min (guardia/horario operativo) | ≤ 4 h | Cada 2 h | IC + owner técnico del dominio |

> Si un incidente cumple más de un criterio, prevalece la severidad más alta.

## 3) Roles obligatorios por dominio

Cada `RUNBOOKS.md` debe declarar explícitamente:

1. **Owner técnico** (responsable de diagnóstico, mitigación y postmortem técnico).
2. **Owner negocio/regulatorio** (responsable de decisiones de impacto comercial, clientes y cumplimiento).
3. **Rotación on-call** (primaria, secundaria y cobertura horaria).

## 4) SLA operativo mínimo

- **Tiempo de ack:** desde la generación del incidente hasta confirmación humana.
- **Tiempo de mitigación/contención:** restablecer servicio o reducir blast radius de forma verificable.
- **Cadencia de comunicación:** updates a stakeholders internos hasta cierre/estabilización.
- **Postmortem:**
  - SEV0/SEV1: borrador en ≤ 24 h, versión final en ≤ 5 días hábiles.
  - SEV2: post-incident review en ≤ 5 días hábiles.

## 5) Protocolo de handoff entre equipos

### 5.1 Handoff durante incidente (Follow-the-sun / cambio de turno)

Checklist obligatorio de transferencia:

- Contexto actual y severidad vigente.
- Hipótesis activas y evidencia recolectada.
- Acciones ejecutadas y resultados.
- Riesgos abiertos y decisiones pendientes.
- Próxima actualización comprometida (hora UTC).

### 5.2 Handoff técnico → negocio/regulatorio

Se debe comunicar explícitamente:

- Impacto en clientes/órdenes/pagos.
- Exposición legal/regulatoria por país.
- Medidas temporales aplicadas y duración esperada.
- Plan de comunicación externa (si aplica).

### 5.3 Handoff de cierre

Condiciones mínimas para cerrar incidente:

- Métricas de servicio estabilizadas.
- Riesgo residual documentado y aceptado.
- Ticket de seguimiento (acciones preventivas) creado.
- Dueños y fechas comprometidas registradas.

## 6) Integración con Deploy Gates y Master Blueprint

- Los dominios deben referenciar este estándar desde su sección `Ownership & Escalation`.
- `docs/05-DEPLOY-GATES.md` debe exigir evidencia de ownership, severidad y SLA.
- `docs/06-MASTER-BLUEPRINT.md` debe incluir este estándar como control transversal operativo.

## 7) Cumplimiento y auditoría

- Incumplimientos de SLA o handoff incompleto se registran en `docs/04-CHANGELOG.md` y en el artefacto de release correspondiente (`docs/releases/*`).
- Este estándar aplica por defecto a todos los dominios; excepciones requieren ADR aprobada.
