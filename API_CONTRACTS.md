# API_CONTRACTS

Este documento referencia los contratos máquina OpenAPI mínimos por bounded context.

## Convención de versionado semántico

- `v1`: primera versión mayor estable del contrato.
- `v1.1`: versión menor retrocompatible (nuevos campos opcionales, nuevos endpoints no rompientes).
- `v2`: versión mayor con cambios rompientes.

## Política de compatibilidad hacia atrás

1. Mantener compatibilidad durante toda la misma versión mayor (`v1`, `v1.1`, `v1.2`).
2. No eliminar ni cambiar semántica de campos obligatorios dentro de la misma mayor.
3. Cualquier cambio rompiente requiere nueva versión mayor (`v2`) y convivencia mínima de 1 ciclo de release.
4. Deprecaciones deben anunciarse antes de removerse, con fecha objetivo.

## Punteros a artefactos OpenAPI

| Dominio | Contrato |
|---|---|
| `disputas` | `contracts/api/disputas.yaml` |
| `estructura-v2` | `contracts/api/estructura-v2.yaml` |
| `facturacion-documentos` | `contracts/api/facturacion-documentos.yaml` |
| `sistema-de-analitica` | `contracts/api/sistema-de-analitica.yaml` |
| `sistema-de-archivos` | `contracts/api/sistema-de-archivos.yaml` |
| `sistema-de-auditoria` | `contracts/api/sistema-de-auditoria.yaml` |
| `sistema-de-barrio` | `contracts/api/sistema-de-barrio.yaml` |
| `sistema-de-busqueda` | `contracts/api/sistema-de-busqueda.yaml` |
| `sistema-de-capacidad-disponibilidad` | `contracts/api/sistema-de-capacidad-disponibilidad.yaml` |
| `sistema-de-cobertura` | `contracts/api/sistema-de-cobertura.yaml` |
| `sistema-de-contenido` | `contracts/api/sistema-de-contenido.yaml` |
| `sistema-de-continuidad-v2` | `contracts/api/sistema-de-continuidad-v2.yaml` |
| `sistema-de-copia-de-seguridad` | `contracts/api/sistema-de-copia-de-seguridad.yaml` |
| `sistema-de-credito-interno` | `contracts/api/sistema-de-credito-interno.yaml` |
| `sistema-de-cupones` | `contracts/api/sistema-de-cupones.yaml` |
| `sistema-de-genie` | `contracts/api/sistema-de-genie.yaml` |
| `sistema-de-integraciones` | `contracts/api/sistema-de-integraciones.yaml` |
| `sistema-de-jerarqua` | `contracts/api/sistema-de-jerarqua.yaml` |
| `sistema-de-lealtad` | `contracts/api/sistema-de-lealtad.yaml` |
| `sistema-de-memory` | `contracts/api/sistema-de-memory.yaml` |
| `sistema-de-mensajeria` | `contracts/api/sistema-de-mensajeria.yaml` |
| `sistema-de-moderacion` | `contracts/api/sistema-de-moderacion.yaml` |
| `sistema-de-notificaciones` | `contracts/api/sistema-de-notificaciones.yaml` |
| `sistema-de-observalidad` | `contracts/api/sistema-de-observalidad.yaml` |
| `sistema-de-ordenes` | `contracts/api/sistema-de-ordenes.yaml` |
| `sistema-de-pagos` | `contracts/api/sistema-de-pagos.yaml` |
| `sistema-de-referido` | `contracts/api/sistema-de-referido.yaml` |
| `sistema-de-reputacion-buyer` | `contracts/api/sistema-de-reputacion-buyer.yaml` |
| `sistema-de-reputacion-seller` | `contracts/api/sistema-de-reputacion-seller.yaml` |
| `sistema-de-reserva-global` | `contracts/api/sistema-de-reserva-global.yaml` |
| `sistema-de-reserva-nacional` | `contracts/api/sistema-de-reserva-nacional.yaml` |
| `sistema-de-seguridad` | `contracts/api/sistema-de-seguridad.yaml` |
| `sistema-de-soporte` | `contracts/api/sistema-de-soporte.yaml` |
| `sistema-de-usuarios` | `contracts/api/sistema-de-usuarios.yaml` |
| `sistema-geo-intelligence-map` | `contracts/api/sistema-geo-intelligence-map.yaml` |
| `sistema-gobernanza-multi-pais-app-camaleon` | `contracts/api/sistema-gobernanza-multi-pais-app-camaleon.yaml` |
| `sistema-unificado-take-rate-engine-revenue-rate-engine-v20` | `contracts/api/sistema-unificado-take-rate-engine-revenue-rate-engine-v20.yaml` |
| `waterfall-engine-v10` | `contracts/api/waterfall-engine-v10.yaml` |

## Ejemplo válido (request `POST /<dominio>/commands`)

```json
{
  "id": "8e62fc42-81ea-42ea-8e4f-7099b8388c66",
  "type": "sistema-de-usuarios.execute",
  "timestamp": "2026-02-07T10:49:00Z",
  "payload": {"action": "sync"}
}
```

## Ejemplo inválido

```json
{
  "id": "not-a-uuid",
  "type": 42,
  "payload": {"action": "sync"}
}
```

Inválido porque `id` no es UUID, `type` no es string y falta `timestamp`.
