# Invariantes transversales

Este catálogo es único y de adopción obligatoria para todos los dominios.

## Dinero
- Snapshot **inmutable** de estado monetario por operación.
- **No retroactividad**: ningún cambio normativo o de configuración altera liquidaciones ya cerradas.
- **Recálculo determinístico**: mismo input versionado produce exactamente el mismo output.

## Seguridad
- Modelo **zero-trust** entre servicios, usuarios y actores internos.
- Autorización **RBAC/ABAC** obligatoriamente aplicada y validada en backend.

## Auditoría
- Registro **WORM/append-only** para eventos críticos y trazabilidad de decisiones.

## Integraciones
- **Idempotencia** obligatoria en operaciones externas e internas de borde.
- **Replay safety**: reintentos/reprocesos no deben generar efectos colaterales duplicados.

## Multi-país
- **Policy precedence** explícita y verificable (global > región > país > jurisdicción local, salvo ADR).
- **Scoping territorial obligatorio** en toda regla, dato y operación con impacto regulatorio o fiscal.

## Gobernanza de excepciones
- Ninguna implementación puede introducir excepciones a estos invariantes sin un **ADR aprobado** y trazable.
