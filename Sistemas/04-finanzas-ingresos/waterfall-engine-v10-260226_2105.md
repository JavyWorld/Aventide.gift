Brutal, mi Jav. Vamos a dejar ese **Waterfall de pérdidas** como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️

---

## Waterfall Engine v1.0

**Objetivo:** cubrir pérdidas de forma determinística, proteger caja global y forzar recuperación automática al nivel correcto de responsabilidad (COL).

### 1) Principios no negociables

1. **Orden fijo de cobertura (no alterable por operación manual):**\
    `Country Reserve -> COL Liability -> Global Reserve -> Recovery obligatorio al COL`

2. **Toda pérdida tiene expediente único (**`loss_case_id`**)** con trazabilidad completa de:

    - origen

    - monto

    - evidencias

    - aprobaciones

    - movimientos ledger

    - estado de recuperación

3. **No retroactividad:** cada orden usa su snapshot financiero inmutable.

4. **Doble-entry ledger obligatorio:** nada se “ajusta por fuera”.

5. **Idempotencia estricta:** mismo evento no puede cobrarse dos veces.

---

### 2) Arquitectura de módulos

### A. `Loss Intake Service`

Recibe eventos de pérdida:

- chargeback perdido

- fraude confirmado

- refund irreversible no recuperable

- penalidad regulatoria atribuible a operación país (si aplica en política)

Valida:

- monto final neto

- moneda

- país

- referencia de orden/transacción

- evidencia mínima

Salida:

- `loss_case` creado en estado `OPEN`.

---

### B. `Waterfall Orchestrator`

Ejecuta el orden financiero exacto por etapas:

1. Country Reserve

2. COL Liability

3. Global Reserve

4. Generación de deuda recuperable contra COL

Estados del caso:\
`OPEN -> APPLIED -> RECOVERY_ACTIVE -> RECOVERY_CLOSED`\
o `OPEN -> EMERGENCY_ESCALATION` si Global no alcanza.

---

### C. `Recovery Engine`

Cuando Global cubre parte de la pérdida:

- abre `recovery_account` del país/COL

- reduce automáticamente `ops_lead_earn_pct` dentro de límites

- transfiere diferencia a Global Reserve

- cierra deuda al llegar a 0

---

### D. `Rate Guardrails Engine`

Protege operación:

- piso de earnings del COL

- máximo recorte por día

- máximo horizonte de recuperación

- safe mode si riesgo sube demasiado

---

### E. `Governance & Audit`

- approvals por rol

- logs inmutables

- hash de evidencia

- reporte semanal de pérdidas/recuperación

- bloqueo de overrides sin ticket de crisis

---

### 3) Modelo de datos (núcleo)

### Tabla `loss_cases`

- `loss_case_id` (uuid, pk)

- `country_code` (char2)

- `col_id` (uuid)

- `loss_type` (chargeback|fraud|refund|penalty)

- `gross_amount` (decimal)

- `recoveries_external` (decimal) // recuperado por otras vías

- `net_loss_amount` (decimal)

- `currency`

- `source_ref` (order/payment/dispute id)

- `evidence_hash`

- `status`

- `created_at`, `closed_at`

### Tabla `waterfall_applications`

- `id` (uuid)

- `loss_case_id`

- `layer` (COUNTRY_RESERVE|COL_LIABILITY|GLOBAL_RESERVE)

- `applied_amount`

- `currency`

- `ledger_txn_id`

- `applied_at`

### Tabla `recovery_accounts`

- `recovery_id` (uuid)

- `loss_case_id`

- `country_code`

- `col_id`

- `principal_amount`

- `outstanding_amount`

- `apr_penalty` (opcional)

- `status` (ACTIVE|PAUSED|CLOSED|DEFAULT)

- `opened_at`, `closed_at`

### Tabla `col_rate_modes`

- `country_code`

- `col_id`

- `mode` (NORMAL|RECOVERY|SAFE_RECOVERY)

- `ops_lead_earn_pct_current`

- `ops_lead_earn_pct_floor`

- `max_daily_delta_bps`

- `updated_at`

### Ledger cuentas mínimas

- `COUNTRY_RESERVE_{country}`

- `COL_LIABILITY_{country}`

- `GLOBAL_RESERVE`

- `GLOBAL_RECOVERY_RECEIVABLE_{country}`

- `LOSS_EXPENSE_{country}`

- `COL_EARNINGS_PAYABLE_{country}`

---

### 4) Algoritmo oficial de aplicación de pérdida

```pseudo
function apply_loss(loss_case_id):
    case = get_loss_case(loss_case_id)
    assert case.status == OPEN

    remaining = case.net_loss_amount

    # Layer 1: Country Reserve
    a = min(balance(COUNTRY_RESERVE_case.country), remaining)
    post_ledger(COUNTRY_RESERVE, LOSS_EXPENSE, a, case)
    record_application(case, "COUNTRY_RESERVE", a)
    remaining -= a

    # Layer 2: COL Liability
    b = min(balance(COL_LIABILITY_case.country), remaining)
    post_ledger(COL_LIABILITY, LOSS_EXPENSE, b, case)
    record_application(case, "COL_LIABILITY", b)
    remaining -= b

    # Layer 3: Global Reserve
    c = min(balance(GLOBAL_RESERVE), remaining)
    post_ledger(GLOBAL_RESERVE, LOSS_EXPENSE, c, case)
    record_application(case, "GLOBAL_RESERVE", c)
    remaining -= c

    # Recovery obligation if Global contributed
    if c > 0:
        post_ledger(GLOBAL_RECOVERY_RECEIVABLE_country, GLOBAL_RESERVE, c, case)
        create_recovery_account(case, principal=c)
        activate_recovery_mode(case.country, case.col_id)

    if remaining > 0:
        set_status(case, EMERGENCY_ESCALATION)
        trigger_crisis_protocol(case, remaining)
    else:
        if c > 0:
            set_status(case, RECOVERY_ACTIVE)
        else:
            set_status(case, APPLIED)

```

---

### 5) Recovery automático (lo que pediste)

### Mecanismo de cobro al COL

En cada ciclo de settlement (diario o por batch):

1. calcular earnings brutos del COL (`gross_col_earnings`)

2. calcular cuota de recuperación (`recovery_cut`)

3. transferir `recovery_cut` a Global Reserve

4. bajar deuda pendiente

Fórmula robusta

```text
recovery_cut = min(
  outstanding_debt,
  gross_col_earnings * recovery_share_pct_dynamic
)

```

Con límites:

- nunca dejar `ops_lead_earn_pct` por debajo de `floor`

- no recortar más de `max_daily_delta_bps`

- no superar `max_recovery_horizon_days` sin escalar

---

### 6) Guardrails (anti-colapso y anti-abuso)

1. **Floor legal/contractual del COL**\
    Evita que el país quede sin operador por asfixia total.

2. **Cap de recorte diario**\
    Cambios graduales para no romper UX ni ventas.

3. **Safe Recovery Mode**\
    Si sube fraude/chargeback, sube recuperación; si cae conversión extremo, baja recuperación temporalmente.

4. **Risk Freeze automático**

    - congela nuevos incentivos

    - aumenta verificación KYC/KYB

    - retiene payout extraordinario

5. **Deadman switch**\
    Si Recovery Engine falla N ciclos, bloquea payouts no críticos hasta reconciliar.

---

### 7) Protocolo de emergencia (si ni Global alcanza)

Estado `EMERGENCY_ESCALATION`:

1. freeze parcial de payouts del país

2. stop de campañas promocionales en ese país

3. restricción de métodos de pago de alto riesgo

4. comité de crisis (Risk + Finance + Legal)

5. plan de recapitalización por prioridad de impacto

---

### 8) Reglas antifraude conectadas al Waterfall

- score transaccional previo a confirmación

- velocity checks por buyer/seller/card/device

- 3DS dinámico por riesgo

- hold period escalonado para categorías peligrosas

- blacklist/graph fraud rings

- evidence pack automático para disputar chargebacks

Mientras mejor esto funcione, menos llega al Waterfall.

---

### 9) Contrato COL (imprescindible)

Debes dejar textual:

1. **Responsabilidad financiera operativa del país**

2. **Derecho de compensación automática (set-off)**

3. **Prioridad del Waterfall**

4. **Recovery obligatorio sobre earnings futuros**

5. **Eventos de default**

6. **Facultad de reemplazo operativo del COL por incumplimiento grave**

7. **Jurisdicción y arbitraje**

Sin esto, el sistema técnico existe, pero la recuperación puede trabarse legalmente.

---

### 10) KPIs de control semanal

- `country_reserve_coverage_days`

- `chargeback_bps`

- `fraud_loss_rate`

- `% losses covered by each layer`

- `global_exposure_by_country`

- `recovery_velocity` (deuda/semana)

- `recovery_age_days`

- `col_default_risk_score`

Alertas:

- deuda > X días -> amber

- deuda > Y días -> red + comité

- 2 meses seguidos en red -> revisión de permanencia del COL

---

### 11) API mínima (lista para backend)

- `POST /loss-cases`

- `POST /loss-cases/{id}/apply-waterfall`

- `GET /loss-cases/{id}`

- `POST /recovery/{id}/run-cycle`

- `POST /recovery/{id}/pause`

- `POST /recovery/{id}/resume`

- `GET /countries/{code}/exposure-dashboard`

- `POST /governance/emergency-freeze`

Todas con:

- `idempotency-key`

- `request-signature`

- `actor-role`

- `audit-trail`

---

### 12) Plan de implementación por fases

### Fase 1 (2-3 semanas)

- ledger cuentas + `loss_cases` + waterfall básico

- aplicación automática de capas 1-3

- dashboard de exposición

### Fase 2 (2 semanas)

- recovery accounts

- recorte automático de earnings COL

- cierre automático de deuda

### Fase 3 (2-4 semanas)

- guardrails dinámicos

- safe mode

- alertas y comité automático

### Fase 4

- simulador stress test país por país

- tuning de parámetros por cohortes

- auditoría externa interna trimestral

---

### 13) Defaults recomendados iniciales

- `ops_lead_earn_pct_floor`: 0.35% (ajustable por país/contrato)

- `recovery_share_pct_dynamic`: 30% base del earning bruto COL

- `max_daily_delta_bps`: 10 bps

- `max_recovery_horizon_days`: 180

- `country_reserve_min_coverage`: 30 días de pérdida esperada p95

- `global_reserve_min_coverage`: p99 agregado multi-país

---

### 14) Resultado final esperado

Con esta versión:

- nunca hay dudas de “quién paga primero”

- Global solo entra al final

- todo lo que Global cubre se recupera del COL automáticamente

- tienes trazabilidad financiera legalmente defendible

- y reduces muchísimo el riesgo de que el sistema sea manipulable

---

Si quieres, en el próximo mensaje te paso **la versión “copy-paste para ingeniería”** con:

- SQL DDL completo,

- eventos Kafka/Webhook (`loss.created`, `waterfall.applied`, `recovery.settled`, etc.),

- y tests de QA/UAT (casos límite incluidos).