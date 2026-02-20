# DATA_CONTRACTS

Este documento referencia los contratos máquina de entidades clave (JSON Schema) por bounded context.

## Convención de versionado semántico

- `v1`: modelo base de entidad.
- `v1.1`: añade campos opcionales o catálogos extensibles sin romper consumidores.
- `v2`: redefine estructura o tipos de campos de forma no retrocompatible.

## Política de compatibilidad hacia atrás

1. Dentro de la misma mayor se permiten solo cambios aditivos o de documentación.
2. No se puede volver opcional→obligatorio un campo sin cambio mayor.
3. La eliminación o cambio de tipo de campos requiere `v2`.
4. Los pipelines de datos deben soportar lectura de al menos la versión mayor actual y la inmediatamente anterior durante migración.

## Punteros a artefactos JSON Schema

| Dominio | Contrato |
|---|---|
| `disputas` | `contracts/data/disputas.json` |
| `estructura-v2` | `contracts/data/estructura-v2.json` |
| `facturacion-documentos` | `contracts/data/facturacion-documentos.json` |
| `sistema-de-analitica` | `contracts/data/sistema-de-analitica.json` |
| `sistema-de-archivos` | `contracts/data/sistema-de-archivos.json` |
| `sistema-de-auditoria` | `contracts/data/sistema-de-auditoria.json` |
| `sistema-de-barrio` | `contracts/data/sistema-de-barrio.json` |
| `sistema-de-busqueda` | `contracts/data/sistema-de-busqueda.json` |
| `sistema-de-capacidad-disponibilidad` | `contracts/data/sistema-de-capacidad-disponibilidad.json` |
| `sistema-de-cobertura` | `contracts/data/sistema-de-cobertura.json` |
| `sistema-de-contenido` | `contracts/data/sistema-de-contenido.json` |
| `sistema-de-continuidad-v2` | `contracts/data/sistema-de-continuidad-v2.json` |
| `sistema-de-copia-de-seguridad` | `contracts/data/sistema-de-copia-de-seguridad.json` |
| `sistema-de-credito-interno` | `contracts/data/sistema-de-credito-interno.json` |
| `sistema-de-cupones` | `contracts/data/sistema-de-cupones.json` |
| `sistema-de-genie` | `contracts/data/sistema-de-genie.json` |
| `sistema-de-integraciones` | `contracts/data/sistema-de-integraciones.json` |
| `sistema-de-jerarqua` | `contracts/data/sistema-de-jerarqua.json` |
| `sistema-de-lealtad` | `contracts/data/sistema-de-lealtad.json` |
| `sistema-de-memory` | `contracts/data/sistema-de-memory.json` |
| `sistema-de-mensajeria` | `contracts/data/sistema-de-mensajeria.json` |
| `sistema-de-moderacion` | `contracts/data/sistema-de-moderacion.json` |
| `sistema-de-notificaciones` | `contracts/data/sistema-de-notificaciones.json` |
| `sistema-de-observalidad` | `contracts/data/sistema-de-observalidad.json` |
| `sistema-de-ordenes` | `contracts/data/sistema-de-ordenes.json` |
| `sistema-de-pagos` | `contracts/data/sistema-de-pagos.json` |
| `sistema-de-referido` | `contracts/data/sistema-de-referido.json` |
| `sistema-de-reputacion-buyer` | `contracts/data/sistema-de-reputacion-buyer.json` |
| `sistema-de-reputacion-seller` | `contracts/data/sistema-de-reputacion-seller.json` |
| `sistema-de-reserva-global` | `contracts/data/sistema-de-reserva-global.json` |
| `sistema-de-reserva-nacional` | `contracts/data/sistema-de-reserva-nacional.json` |
| `sistema-de-seguridad` | `contracts/data/sistema-de-seguridad.json` |
| `sistema-de-soporte` | `contracts/data/sistema-de-soporte.json` |
| `sistema-de-usuarios` | `contracts/data/sistema-de-usuarios.json` |
| `sistema-geo-intelligence-map` | `contracts/data/sistema-geo-intelligence-map.json` |
| `sistema-gobernanza-multi-pais-app-camaleon` | `contracts/data/sistema-gobernanza-multi-pais-app-camaleon.json` |
| `sistema-unificado-take-rate-engine-revenue-rate-engine-v20` | `contracts/data/sistema-unificado-take-rate-engine-revenue-rate-engine-v20.json` |
| `waterfall-engine-v10` | `contracts/data/waterfall-engine-v10.json` |

## Ejemplo válido

```json
{
  "id": "6454089f-2a06-43fe-a1de-ef11738ef4f7",
  "domain": "sistema-de-usuarios",
  "version": "v1",
  "status": "active",
  "createdAt": "2026-02-07T10:49:00Z",
  "updatedAt": "2026-02-07T10:50:00Z",
  "attributes": {"country": "AR"}
}
```

## Ejemplo inválido

```json
{
  "id": 123,
  "domain": "otro-dominio",
  "version": "1",
  "status": "enabled"
}
```

Inválido porque `id` debe ser string UUID, `domain` debe coincidir con el dominio del schema, `version` no sigue `vN` y `status` no pertenece al enum.
