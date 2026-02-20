# DO - Policy Overrides vs Baseline Global

| Override local | Cambio vs baseline global | Justificación | ADR | Dominios afectados |
|---|---|---|---|---|
| Cálculo de ITBIS por tipo de servicio | El baseline usa motor fiscal genérico; DO exige reglas locales y exenciones específicas | Cumplimiento tributario local y precisión de facturación | [ADR-DO-001](../../01-ADR/ADR-DO-001-itbis-servicios-digitales.md) | [Fiscalidad](../../02-DOMAINS/FISCALIDAD.md), [Facturación](../../02-DOMAINS/FACTURACION.md) |
| Retención fiscal en payouts a proveedores locales | El baseline liquida payout neto sin retención local por defecto | Mitigar riesgo de incumplimiento y contingencia fiscal | [ADR-DO-002](../../01-ADR/ADR-DO-002-retencion-fiscal-proveedores.md) | [Payouts](../../02-DOMAINS/PAYOUTS.md), [Fiscalidad](../../02-DOMAINS/FISCALIDAD.md) |
