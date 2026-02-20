# CO - Policy Overrides vs Baseline Global

| Override local | Cambio vs baseline global | Justificación | ADR | Dominios afectados |
|---|---|---|---|---|
| Facturación electrónica validada para operaciones gravables | El baseline permite documentos fiscales no validados en tiempo real | Cumplimiento con exigencias locales de facturación electrónica | [ADR-CO-001](../../01-ADR/ADR-CO-001-factura-electronica-dian.md) | [Facturación](../../02-DOMAINS/FACTURACION.md), [Fiscalidad](../../02-DOMAINS/FISCALIDAD.md) |
| Evidencia de consentimiento y retención reforzada de datos personales | El baseline define privacidad general; CO requiere trazabilidad reforzada de autorizaciones | Mitigación de riesgo sancionatorio por Habeas Data | [ADR-CO-002](../../01-ADR/ADR-CO-002-retencion-datos-habeas-data.md) | [Privacidad](../../02-DOMAINS/PRIVACIDAD.md), [Retención de datos](../../02-DOMAINS/RETENCION-DATOS.md) |
