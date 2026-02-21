# ADR-STR-004: Estándar de pruebas de caos y DR para money-critical

## Estado
Pendiente

## Contexto
La cadena `order → payment → escrow → dispute → settlement` concentra riesgo financiero y regulatorio. Se requiere un estándar mínimo de caos/DR para validar resiliencia operativa con evidencia objetiva.

## Decisión
Adoptar un estándar transversal de pruebas de caos y recuperación con:

1. Escenarios mínimos obligatorios (caída de proveedor de pago, atraso de eventos, inconsistencia de settlement).
2. Medición y aprobación formal de RTO/RPO por escenario.
3. Registro de simulacros y acciones correctivas con responsables.

## Dominios afectados
- [Payouts](../02-DOMAINS/PAYOUTS.md)
- [Disputas](../02-DOMAINS/DISPUTAS.md)
- [Facturación](../02-DOMAINS/FACTURACION.md)
