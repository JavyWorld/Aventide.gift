# ADR-0001: Contexto y decisiones clave (continuity)

- **Estado**: Aprobado
- **Contexto**: Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).

## Decisiones
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- Control de riesgo/abuso: acciones críticas requieren break-glass + 2FA + motivo + TTL + auditoría; y cuando sube el riesgo existe LOCKDOWN.
- 4.4 Caso D — Riesgo alto (LOCKDOWN)
- aplicar holds a payouts del COL (si existe), usando políticas de payout/riesgo por país.
- cobertura de riesgo (chargebacks/costos externos),
- Payout/riesgo por país: cashout_min/max, rolling_reserve_pct, thresholds KYC (se reutiliza para holds y lockdown).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
