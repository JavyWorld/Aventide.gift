### Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”

**Fuente de verdad:** Documento “resumen-260207_1014”.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Continuidad es el sistema que garantiza que el negocio **no se detenga** cuando falta (temporal o permanentemente) un rol crítico por país —especialmente **COUNTRY_OPS_LEAD (COL)**— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo **gobernanza, auditoría fuerte y políticas multi-país**, sin introducir retroactividad en dinero (snapshot).

**Objetivos (duros):**

1. Ningún país queda “sin control”: existe un estado formal del país y una cadena de cobertura.

2. No romper el core económico: fees snapshotteados, split automático (seller / Aventide / COL), ledger inmutable.

3. Control de riesgo/abuso: acciones críticas requieren **break-glass + 2FA + motivo + TTL + auditoría**; y cuando sube el riesgo existe **LOCKDOWN**.

4. En vacancia, el bucket “ops” no desaparece: se enruta a **COUNTRY_RESERVE** con custodia corporativa, no “backpay” al nuevo COL.

5. Observabilidad y respuesta automática: monitoreo de anomalías por país/rol y disparo de medidas (hold, bloqueo, reroute).

---

## 2) Alcance (incluye / excluye)

### Incluye

- Gestión del estado de gobernanza por país: `ACTIVE | VACANT | TRANSITION | LOCKDOWN`.

- Reglas de **delegación temporal** (Acting Ops Lead) con TTL + subset de permisos + auditoría.

- Re-enrutamiento de colas operativas cuando falta COL (incidentes, aprobaciones, tickets/disputas).

- Continuidad financiera del bucket OpsFee:

    - se sigue cobrando,

    - se snapshottea en orden,

    - se enruta a beneficiario (COL o COUNTRY_RESERVE) según governance_state.

- Workflow de desembolso desde COUNTRY_RESERVE con **four-eyes** + ejecución idempotente por worker + auditoría WORM.

- Detección/alerta de abuso de rol (break-glass bursts, exportaciones, cambios de zona, spikes de aprobaciones).

### Excluye

- Copias de seguridad/DR (eso es “Copia de seguridad”).

- Política laboral/HR de terminaciones (solo estado operativo y efectos en plataforma).

- Cálculo del fee: Continuidad **no calcula** fees; solo define routing y permisos (cálculo vive en motores financieros/rates).

---

## 3) Actores y permisos (RBAC) + guards

### Actores

- **COUNTRY_OPS_LEAD (COL):** operación local (control plane).

- **ACTING_COUNTRY_OPS_LEAD:** delegado temporal con permisos limitados.

- **SUPER_ADMIN (global):** control máximo y cobertura ante vacancia; puede activar LOCKDOWN.

- **FINANCE_ADMIN (global):** controla movimientos desde COUNTRY_RESERVE y acciones de money-plane vía workflow.

- **SUPPORT_AGENT / SRE_ADMIN:** cobertura operacional limitada (p.ej. pausar/kill switch) según policy de emergencia.

- **SYSTEM/WORKERS:** ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).

- **AUDIT/LEGAL:** lectura y export de evidencia, con registros de acceso sensible.

### Permisos mínimos (núcleo)

- `country.governance.read`

- `country.governance.state.update` (super_admin; ops lead no)

- `role.assignment.create/terminate` (super_admin; four-eyes recomendado)

- `role.delegation.grant/revoke` (super_admin; con TTL obligatorio)

- `queue.reroute.execute` (system)

- `money.reserve.disbursement.request/create` (finance_admin)

- `money.reserve.disbursement.approve` (finance_admin distinto; four-eyes)

- `money.reserve.disbursement.execute` (system/worker)

- `break_glass.start/stop` (roles permitidos; con 2FA/motivo/TTL)

- `audit.read` / `audit.view_sensitive` (scoped; con reason)

### Guards (cadena canónica + extensión de continuidad)

Cadena base: `AuthGuard → RoleGuard → ScopeGuard → PermissionGuard → PolicyGuard`.

**ContinuityPolicyGuard (nuevo dentro de PolicyGuard):**

- bloquea/permite acciones según `country_governance_state` y si hay `ops_lead_assignment` activo.

- exige **break-glass** para overrides críticos (dinero/outcomes/escrow).

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Caso A — Vacancia (renuncia/despido/inhabilitación del COL)

**Trigger:** revocación del rol/scope o offboarding del usuario (auditado).

**Happy path**

1. `RBAC_ROLE_REVOKED` + `RBAC_SCOPE_REVOKED` al COL saliente + invalidación de sesiones/claims.

2. `country_governance_state = VACANT`.

3. Policy Engine activa “modo continuidad” para ese país:

    - bloquea publish local y acciones masivas,

    - permite solo acciones de seguridad operacional por SUPER_ADMIN (y/o SRE limitado).

4. Reroute colas: items que antes iban al COL (incidentes L3, aprobaciones, etc.) pasan a `GLOBAL_ONCALL_QUEUE`/`SUPER_ADMIN_QUEUE`.

5. Money-plane: las nuevas órdenes siguen cobrando `ops_fee_pct` snapshotteado, pero su beneficiario pasa a `COUNTRY_RESERVE`.

**Edge cases**

- Si en vacancia ocurre una acción crítica de dinero (hold/unhold, refund manual, payout exception): se exige break-glass y el actor debe ser global (SUPER_ADMIN/FINANCE_ADMIN).

### 4.2 Caso B — Handover controlado (cambio de COL)

**Happy path**

1. Crear `ops_lead_assignment` nuevo con `effective_from`.

2. (Recomendación operativa del sistema) **four-eyes**: requester ≠ approver para asignación de COL.

3. Grant de `COUNTRY_OPS_LEAD` con scope del país.

4. Reroute de colas al nuevo COL.

5. `country_governance_state = ACTIVE`.

**Regla dura anti-backpay**

- El nuevo COL **solo** recibe OpsFee desde `effective_from`.

- El `COUNTRY_RESERVE` acumulado **no** se transfiere automáticamente al nuevo COL.

### 4.3 Caso C — Ausencia temporal (vacaciones/incapacidad/abandono)

**Happy path**

1. `ops_lead_assignment.status = TEMP_UNAVAILABLE` con `until`.

2. Conceder `role_delegation` a un ActingOpsLead con TTL y subset de permisos.

3. Si no hay delegado, se eleva a `SUPER_ADMIN_QUEUE` (cobertura global).

**Edge case**

- Expira el TTL del delegado: `ROLE_DELEGATION_EXPIRED` y el país entra a `VACANT` o vuelve a ACTIVE si el COL regresa.

### 4.4 Caso D — Riesgo alto (LOCKDOWN)

**Trigger:** anomalías por seguridad/abuso (ver 9) o incidentes de integridad.

**Happy path**

1. Policy Engine coloca `country_governance_state = LOCKDOWN`.

2. Efectos:

- bloquear onboarding approvals / cambios masivos,

- requerir SUPER_ADMIN para acciones críticas,

- aplicar holds a payouts del COL (si existe), usando políticas de payout/riesgo por país.

1. Alertas internas P0/P1 a Global Management.

---

## 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

### 5.1 Principio clave: separación Control Plane vs Money Plane

- **COL/ActingCOL** opera estado y configuración local (zonas, onboarding, contenido local) dentro de límites.

- **Money Plane** (payouts/refunds/releases/reserve movements) se ejecuta por workers/policies y roles globales; overrides requieren break-glass.

### 5.2 Regla financiera innegociable

- `ops_lead_fee_pct` es config por país y **se snapshottea en la orden**; no cambia retrospectivamente.

### 5.3 Routing del bucket OpsFee (beneficiario)

En snapshot financiero por orden (extensión mínima):

- `ops_fee_pct`, `ops_fee_amount`

- `ops_fee_beneficiary_type: USER | COUNTRY_RESERVE`

- `ops_fee_beneficiary_id: user_id | reserve_account_id`

**Regla:**

- Si país `ACTIVE` y hay `ops_lead_assignment=ACTIVE` ⇒ beneficiario = COL (USER).

- Si `VACANT` o no hay assignment activo ⇒ beneficiario = COUNTRY_RESERVE.

### 5.4 Country_Reserve (custodia corporativa) y usos permitidos

**Country_Reserve = custodia corporativa por país**, no “backpay” del Ops Lead.

Usos permitidos (solo workflow global):

- gastos operativos del país,

- cobertura de riesgo (chargebacks/costos externos),

- presupuesto operativo aprobado,

- consolidación contable a plataforma (si se define).

---

## 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

### 6.1 country_governance_state

- `country_code`

- `state: ACTIVE | VACANT | TRANSITION | LOCKDOWN`

- `acting_user_id` (nullable)

- `updated_by`, `updated_at`

- `reason_code`, `reason_text`

Índices: unique(`country_code`)

### 6.2 ops_lead_assignments

- `id`

- `country_code`

- `user_id` (nullable si VACANT-seat)

- `status: ACTIVE | TEMP_UNAVAILABLE | TERMINATED | SUSPENDED`

- `effective_from`, `effective_to`

- `termination_reason_code` (optional)

- `created_by`, `approved_by` (four-eyes)

Índices: (`country_code`,`status`), (`country_code`,`effective_from desc`)

### 6.3 role_delegations (Acting)

- `id`, `country_code`

- `delegate_user_id`

- `delegated_role: ACTING_COUNTRY_OPS_LEAD`

- `permissions_subset[]`

- `starts_at`, `expires_at` (TTL obligatorio)

- `created_by`, `approved_by`, `reason`

Constraint: TTL máximo por policy.

### 6.4 ledger_accounts (extensión)

- `account_type = COUNTRY_RESERVE`

- `country_code`

- `account_id`

### 6.5 reserve_disbursement_request

- `id`

- `country_code`

- `amount`, `currency`

- `purpose_code`

- `evidence_refs[]`

- `status: REQUESTED | APPROVED | EXECUTED | REJECTED`

- `requested_by`, `approved_by`, `executed_at`

- `idempotency_key`

---

## 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

### Eventos mínimos

- `COUNTRY_GOVERNANCE_STATE_CHANGED`

- `OPS_LEAD_ASSIGNMENT_CREATED/UPDATED/ENDED`

- `ROLE_DELEGATION_GRANTED/REVOKED/EXPIRED`

- `OPS_FEE_ROUTED_TO_RESERVE` (para analítica/alerting)

- `RESERVE_DISBURSEMENT_REQUESTED/APPROVED/EXECUTED/REJECTED`

- `COUNTRY_LOCKDOWN_ENABLED/DISABLED`

### Idempotencia (mínima)

- Delegación: `delegation:{country}:{delegate}:{starts_at}`

- Cambio de governance_state: CAS/lock por `country_code` (evita carreras).

- Disbursement: `idempotency_key` por request (worker ejecuta una vez).

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Policy Engine (Gobernanza multi-país)

- Entrega `ResolvedPolicy` con:

    - `country_governance_state`

    - capabilities habilitadas por rol en VACANT/LOCKDOWN.

### Pagos / Ledger / Rates

- Split automático sigue igual; Continuidad solo define **beneficiario** del bucket ops (COL vs reserve).

- Payout/riesgo por país: `cashout_min/max`, `rolling_reserve_pct`, thresholds KYC (se reutiliza para holds y lockdown).

### Auditoría

- Toda asignación/revocación/delegación/lockdown/disbursement y break-glass queda en WORM.

### Notificaciones internas

- Al entrar a VACANT/LOCKDOWN: notificación P0/P1 a cola global y panel global.

---

## 9) Observabilidad (logs, métricas, alertas, SLOs)

### Monitoreo “OpsLead Risk Monitoring”

Eventos/señales a vigilar (mínimo):

- `BREAK_GLASS_STARTED/ENDED/EXPIRED` (por COL/ActingCOL)

- `ZONE_STATUS_CHANGED` (frecuencia y fuera de horario)

- `SELLER_APPROVAL_DECISIONED` (bursts + correlación con disputas/refunds)

- `DISPUTE_OUTCOME_SELECTED` (si aplica)

- `REPORT_EXPORT_REQUESTED` (volumen/patrón)

- Seguridad: `SUSPICIOUS_LOGIN`, `ACCOUNT_LOCKED`, `LOGIN_FAIL_BURST`

### Métricas mínimas

- `countries_vacant_count`

- `vacancy_duration_hours{country}`

- `country_lockdown_active{country}`

- `ops_fee_reserve_balance{country}`

- `critical_queue_backlog{country,queue}`

- `break_glass_usage_rate{country,role}`

- `suspicious_login_rate{country}`

### Alertas

- SEV1: `VACANT > X horas` en país con órdenes activas.

- SEV0: `LOCKDOWN` activado o spike de break-glass + eventos críticos correlacionados.

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Break-glass: **2FA + motivo + expiración (TTL) + logging reforzado** para acciones críticas.

- Four-eyes (requester ≠ approver) para:

    - asignación/remoción de COL,

    - disbursements desde reserve,

    - activar/desactivar LOCKDOWN (cuando sea manual).

- Accesos sensibles (reportes/exportaciones) con signed URL TTL + watermark + audit log.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **RBAC + Scope + Guards:** se mantiene, Continuidad solo añade reglas en PolicyGuard.

- **Ledger/Money:** split automático y ledger inmutable; Continuidad decide routing del bucket ops a reserve en vacancia.

- **Payout/Risk por país:** usa cashout_min/max, rolling_reserve_pct, KYC thresholds para hold/lockdown.

- **Auditoría WORM:** todo cambio de gobernanza/roles/acciones críticas queda registrado.

---

## Runbook de Continuidad v2.0 (VACANT → TRANSITION → ACTIVE / LOCKDOWN)

**Scope:** Solo Continuidad (roles críticos por país, reroute, money-plane safety, reserve governance, auditoría WORM, gates de reactivación).

---

### 0) Principios operativos (no negociables)

1. **No retroactividad de dinero:** toda orden usa `locked_fee_structure` y el beneficiario del bucket ops se define al momento del snapshot.

2. **VACANT ≠ “sin ops fee”:** el bucket ops se enruta a `COUNTRY_RESERVE` hasta nuevo aviso.

3. **Break-glass** para acciones críticas: 2FA + motivo + TTL + auditoría reforzada.

4. **Four-eyes** obligatorio para: asignación/remoción de COL y disbursements de `COUNTRY_RESERVE`.

5. **WORM y evidencia:** todo cambio de estado/rol y cada acción sensible genera eventos auditables y adjunta evidencia (links).

---

### 1) Estados y objetivos por fase

1.1 Estados de país (governance_state)

- **ACTIVE:** COL asignado, operación normal.

- **VACANT:** sin COL activo; reroute a cobertura global; bucket ops a reserve.

- **TRANSITION:** hay candidato/acting; se hacen checks, shadowing, y gates.

- **LOCKDOWN:** riesgo alto/integridad comprometida; restricciones fuertes y hold/contención.

1.2 Objetivo por fase

- **VACANT:** detener cambios peligrosos y mantener servicio mínimo, sin perder control ni dinero.

- **TRANSITION:** reinstalar gobernanza local gradualmente con pruebas y límites.

- **ACTIVE (reinstatement):** retorno pleno con monitoreo reforzado post-incidente.

- **LOCKDOWN:** contener daño y preservar evidencia; regreso solo con gates de seguridad.

---

### 2) Roles de respuesta (RACI mínimo)

- **Incident Commander (IC):** SUPER_ADMIN global (único responsable de state transitions).

- **Finance Lead:** FINANCE_ADMIN global (reserve disbursements, holds, reconciliación money-plane).

- **Security Lead:** SecurityAdmin/SRE (sesiones, break-glass monitoring, sospecha de cuenta).

- **Ops Oncall:** cola global (manejo de backlog/tickets/disputas durante vacancia).

- **Audit/Legal Observer:** lectura, evidencia WORM, export si aplica.

---

### 3) Playbooks

## 3A) Vacancia (ACTIVE → VACANT)

Triggers típicos

- Revocación del rol/scope, offboarding, suspensión, pérdida de control de cuenta.

Acciones (en orden)

**A1. “Stop the bleeding” (0–15 min)**

1. **Revocar rol y scope** del COL saliente + invalidar sesiones/tokens.

    - Evidencia WORM: `RBAC_ROLE_REVOKED`, `RBAC_SCOPE_REVOKED`, `SESSION_INVALIDATED`.

2. Set `country_governance_state=VACANT` con reason_code.

    - Evidencia WORM: `COUNTRY_GOVERNANCE_STATE_CHANGED`.

3. Activar **ContinuityPolicyGuard** (automático por policy):

    - bloquear cambios masivos y publicación local,

    - permitir solo acciones globales necesarias.

**A2. Reroute operativo (0–60 min)**\
4) Reroute de colas: approvals, incidentes, tickets/disputas a `GLOBAL_ONCALL_QUEUE/SUPER_ADMIN_QUEUE`.

- Evidencia WORM: `QUEUE_REROUTED` (si existe) o `COUNTRY_GOVERNANCE_STATE_CHANGED` con payload de reroute.

1. Comunicar internamente: notificación P0/P1 a oncall global + finance + audit.

**A3. Money-plane continuity (inmediato + continuo)**\
6) En nuevas órdenes: `ops_fee_beneficiary = COUNTRY_RESERVE`.

- Evidencia WORM: `OPS_FEE_ROUTED_TO_RESERVE`.

1. Si había payout schedule activo al COL saliente: poner **hold** preventivo si policy lo exige (especialmente si vacancia por riesgo).

    - Evidencia WORM: `PAYOUT_HOLD_APPLIED` (si existe) + reason/evidence.

Checklist de evidencia WORM (VACANT)

- Role/scope revoked + sessions invalidated (actor + timestamps).

- `country_governance_state=VACANT` con motivo.

- Reroute aplicado y verificado (colas sin dueño local).

- Confirmación de routing: nuevas órdenes → reserve.

- Alertas emitidas a global oncall + finance.

---

## 3B) Transición (VACANT → TRANSITION)

Objetivo

Restituir control local sin abrir vectores de abuso; se habilita un Acting o COL entrante con permisos progresivos.

Acciones (en orden)

**B1. Nombrar cobertura**

1. Crear `role_delegation` a **ACTING_COUNTRY_OPS_LEAD** con TTL y subset de permisos (mínimo viable).

    - Evidencia WORM: `ROLE_DELEGATION_GRANTED` (TTL, permisos, motivo).

2. Set `country_governance_state=TRANSITION` y asociar acting_user_id.

**B2. Shadow period (24–72h; configurable)**\
3) Acting opera bajo supervisión: todas las acciones “riesgosas” siguen requiriendo break-glass global.\
4) Activar panel de monitoreo reforzado (ver Sección 6).

**B3. Reinstalar COL (si ya hay candidato definitivo)**\
5) Crear `ops_lead_assignment` nuevo con `effective_from` (no retroactivo).\
6) Aprobar asignación bajo **four-eyes** (requester ≠ approver).\
7) Conceder rol `COUNTRY_OPS_LEAD` + scope país, y revocar acting delegation (o dejarla expirar).

Checklist de evidencia WORM (TRANSITION)

- Delegación creada (TTL + permisos subset + reason).

- Estado TRANSITION con acting_user_id.

- Four-eyes de assignment (si aplica) con request_id.

- Rol/scope concedidos al nuevo COL y sesiones emitidas.

- Acting revocado o expirado.

---

## 3C) Investigación (durante VACANT/TRANSITION/LOCKDOWN)

Objetivo

Determinar causa raíz (operativa vs riesgo vs seguridad) y asegurar integridad de money-plane y configuración regional.

Acciones mínimas

1. **Timeline WORM**: extraer y fijar un “incident bundle” con:

    - cambios de governance_state,

    - role grants/revokes/delegations,

    - break-glass usage,

    - cambios de zonas/capacidad/aprobaciones,

    - exportaciones de reportes,

    - señales de seguridad (`SUSPICIOUS_LOGIN`, locks).

2. **Money-plane checks**:

    - confirmar que todo `ops_fee` está yendo a COL o reserve según estado,

    - revisar holds/payouts pendientes,

    - verificar que no existan disbursements sin four-eyes.

3. **Config integrity checks**:

    - cambios recientes en zonas, reglas, flags críticos,

    - bursts fuera de horario.

4. Resultado: clasificar severidad y decidir:

    - seguir en VACANT/TRANSITION,

    - activar LOCKDOWN,

    - reinstatement.

Checklist de evidencia WORM (INVESTIGACIÓN)

- Incident bundle generado y referenciado (evidence_links).

- Conclusión con reason_code y decisión de estado.

- Si hubo acciones sensibles: `VIEW_SENSITIVE` por cada acceso a evidencia.

---

## 3D) Reinstatement (TRANSITION → ACTIVE) con gates de reactivación

Objetivo

Volver a ACTIVE sin riesgo de abuso y con money-plane correcto.

### Gates (todos deben pasar)

**Gate 1 — Identidad y acceso**

- Nuevo COL con 2FA activo y sin alertas de seguridad abiertas (si existen). (Suposición operativa coherente con “seguridad/abuso”; el doc menciona señales de seguridad a monitorear).

- Sesiones antiguas invalidadas para cuentas previas.

**Gate 2 — Gobernanza y permisos**

- `ops_lead_assignment=ACTIVE` con `effective_from` claro.

- Four-eyes registrado en auditoría.

- Delegaciones temporales revocadas/expiradas.

**Gate 3 — Money-plane routing correcto**

- Órdenes nuevas creadas durante TRANSITION:

    - si ya ACTIVE al momento del checkout ⇒ `ops_fee_beneficiary=COL`,

    - si aún no ⇒ `ops_fee_beneficiary=COUNTRY_RESERVE`.

- Confirmación de que **no hay backpay automático**: reserve no se transfiere al nuevo COL.

**Gate 4 — Backlog operacional bajo control**

- Cola global de ese país bajo umbral (tickets/disputas) o plan de descarga.

**Gate 5 — Riesgo bajo**

- No hay burst de break-glass, exportaciones o cambios masivos en ventana reciente.

### Acciones de activación

1. Set `country_governance_state=ACTIVE`.

2. Reroute colas al COL entrante.

3. Activar “Monitoreo reforzado post-reinstatement” por 7–14 días (policy).

Checklist WORM (REINSTATEMENT)

- Gates 1–5 marcados PASS con referencias de evidencia.

- `COUNTRY_GOVERNANCE_STATE_CHANGED → ACTIVE`.

- Reroute a COL aplicado y verificado.

- Monitoreo reforzado activado (flag/policy) y alertas configuradas.

---

## 3E) LOCKDOWN (cualquier estado → LOCKDOWN)

Triggers

- Anomalías/abuso/integridad: bursts de break-glass, cambios de zona fuera de patrón, exportaciones masivas, spikes de decisiones sensibles, señales de seguridad.

Acciones (inmediatas)

1. Set `country_governance_state=LOCKDOWN` con reason_code.

2. Efectos (Policy Engine):

- bloquear onboarding approvals / cambios masivos,

- requerir SUPER_ADMIN para acciones críticas,

- aplicar holds a payouts del COL si existe.

1. Asegurar dinero:

- congelar disbursements salvo aprobaciones explícitas,

- reconciliación intensiva.

1. Notificación P0 a Global Management.

Gates para salir de LOCKDOWN (LOCKDOWN → TRANSITION o ACTIVE)

- Investigación completada con bundle WORM.

- Credenciales/roles saneados y sin sesiones sospechosas.

- Money-plane reconciliado (no mismatches críticos).

- Plan de mitigación implementado (p.ej. límites más estrictos temporalmente).

---

### 4) Matriz de permisos por estado (resumen operativo)

**ACTIVE**

- COL normal (dentro de policy).

- Money overrides: break-glass + evidencia (si aplica).

**VACANT**

- Sin COL; acting solo si delegado.

- Cambios masivos bloqueados.

- Money-plane: beneficiario ops → reserve; overrides solo global con break-glass.

**TRANSITION**

- Acting/COL entrante con permisos progresivos.

- Money-plane estrictamente controlado; disbursements desde reserve con four-eyes.

**LOCKDOWN**

- Solo global; mínimo necesario; holds/kill-switches y contención.

---

### 5) Plantillas de evidencia (WORM bundles)

5.1 “Continuity Incident Bundle” (por país)

Campos mínimos (estructura):

- `country_code`

- `incident_id`

- `start_time`, `end_time`

- `trigger_type` (VACANCY|RISK|SECURITY)

- `timeline_refs[]` (audit event IDs)

- `actions_taken[]` (state changes, reroutes, holds)

- `money_plane_status` (routing, holds, reserve balance snapshot)

- `decision` (stay vacant / transition / active / lockdown)

- `approvals[]` (four-eyes si aplica)

- `evidence_links[]` (exports, logs, reports)

5.2 “Reserve Disbursement Pack”

- `request_id`, `purpose_code`, `amount`

- `evidence_links[]`

- `approver_1`, `approver_2` (si four-eyes estricto)

- `execution_ref` (job_id)

- `ledger_refs[]`

(El sistema define workflow y auditoría; esta estructura es el checklist operativo compatible.)

---

### 6) Monitoreo reforzado (post-vacancia / post-reinstatement)

Señales a vigilar (mínimo definido)

- Break-glass start/end/expired.

- Cambios de zona (frecuencia y fuera de horario).

- Bursts de aprobaciones de sellers/decisiones sensibles.

- Exportaciones de reportes.

- Seguridad: suspicious logins, account locked, login fail bursts.

Acciones automáticas recomendadas por el runbook

- Umbral → auto-escalado a SUPER_ADMIN_QUEUE.

- Umbral crítico → sugerir LOCKDOWN (si policy lo permite) y aplicar holds preventivos.

---

### 7) “Done criteria” por fase (para cerrar incidentes)

**Cerrar VACANT:** existe estado definido (VACANT/TRANSITION), reroute confirmado, ops_fee a reserve y colas bajo control global.\
**Cerrar TRANSITION:** gates de reinstatement PASS o plan de continuidad extendida aprobado.\
**Cerrar LOCKDOWN:** investigación cerrada con bundle WORM + mitigación aplicada + estado downgraded (TRANSITION/ACTIVE).

---

### Suposiciones (marcadas)

- Gate explícito de “2FA activo” y verificación de postura de seguridad: el documento lista señales de seguridad y break-glass; el gate de 2FA se propone como criterio operativo coherente, pero no está textual.

- Eventos técnicos como `QUEUE_REROUTED`/`PAYOUT_HOLD_APPLIED`: el documento define reroute/holds como comportamiento; los nombres exactos de eventos pueden variar, pero deben quedar auditados WORM.