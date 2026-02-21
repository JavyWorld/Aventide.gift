# ADR-STR-001: Criterio formal para retiro de `/Sistemas`

## Estado
Pendiente

## Contexto
La transición documental mantiene `/Sistemas/*.docx` como respaldo histórico y `docs/` como fuente operativa. Falta un criterio formal y automatizable para declarar, por dominio, cuándo la paridad está completa y se puede retirar dependencia operativa del histórico.

## Decisión
Definir un criterio único de retiro basado en evidencia verificable por dominio:

1. Cumplimiento 100% de artefactos canónicos (`README`, contratos API/DATA/EVENT, invariantes, runbooks y ADR).
2. Verificación reproducible de enlaces y trazabilidad en `docs/00-INDEX.md` y `docs/06-MASTER-BLUEPRINT.md`.
3. Registro auditable de validación integral 38/38 con responsables y fecha.

## Dominios afectados
- [Retención de datos](../02-DOMAINS/RETENCION-DATOS.md)
- [Privacidad](../02-DOMAINS/PRIVACIDAD.md)
