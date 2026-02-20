# EVENT_CONTRACTS

Este documento referencia los contratos máquina de eventos (JSON Schema) por bounded context.

## Convención de versionado semántico

- `v1`: primer formato de evento estable.
- `v1.1`: extensión retrocompatible (nuevos campos opcionales en `data`).
- `v2`: cambio rompiente (ej. rename de `eventType`, cambios de tipos, campos obligatorios nuevos sin default).

## Política de compatibilidad hacia atrás

1. Consumidores deben tolerar campos adicionales desconocidos en `data` dentro de la misma mayor.
2. Productores no deben remover campos obligatorios en la misma mayor.
3. Cambios rompientes de esquema requieren `eventVersion` mayor nueva (`v2`) y doble publicación transitoria cuando aplique.
4. Versiones menores deben mantener el mismo `eventType` y semántica.

## Punteros a artefactos JSON Schema

| Dominio | Contrato |
|---|---|
| `disputas` | `contracts/events/disputas.json` |
| `estructura-v2` | `contracts/events/estructura-v2.json` |
| `facturacion-documentos` | `contracts/events/facturacion-documentos.json` |
| `sistema-de-analitica` | `contracts/events/sistema-de-analitica.json` |
| `sistema-de-archivos` | `contracts/events/sistema-de-archivos.json` |
| `sistema-de-auditoria` | `contracts/events/sistema-de-auditoria.json` |
| `sistema-de-barrio` | `contracts/events/sistema-de-barrio.json` |
| `sistema-de-busqueda` | `contracts/events/sistema-de-busqueda.json` |
| `sistema-de-capacidad-disponibilidad` | `contracts/events/sistema-de-capacidad-disponibilidad.json` |
| `sistema-de-cobertura` | `contracts/events/sistema-de-cobertura.json` |
| `sistema-de-contenido` | `contracts/events/sistema-de-contenido.json` |
| `sistema-de-continuidad-v2` | `contracts/events/sistema-de-continuidad-v2.json` |
| `sistema-de-copia-de-seguridad` | `contracts/events/sistema-de-copia-de-seguridad.json` |
| `sistema-de-credito-interno` | `contracts/events/sistema-de-credito-interno.json` |
| `sistema-de-cupones` | `contracts/events/sistema-de-cupones.json` |
| `sistema-de-genie` | `contracts/events/sistema-de-genie.json` |
| `sistema-de-integraciones` | `contracts/events/sistema-de-integraciones.json` |
| `sistema-de-jerarqua` | `contracts/events/sistema-de-jerarqua.json` |
| `sistema-de-lealtad` | `contracts/events/sistema-de-lealtad.json` |
| `sistema-de-memory` | `contracts/events/sistema-de-memory.json` |
| `sistema-de-mensajeria` | `contracts/events/sistema-de-mensajeria.json` |
| `sistema-de-moderacion` | `contracts/events/sistema-de-moderacion.json` |
| `sistema-de-notificaciones` | `contracts/events/sistema-de-notificaciones.json` |
| `sistema-de-observalidad` | `contracts/events/sistema-de-observalidad.json` |
| `sistema-de-ordenes` | `contracts/events/sistema-de-ordenes.json` |
| `sistema-de-pagos` | `contracts/events/sistema-de-pagos.json` |
| `sistema-de-referido` | `contracts/events/sistema-de-referido.json` |
| `sistema-de-reputacion-buyer` | `contracts/events/sistema-de-reputacion-buyer.json` |
| `sistema-de-reputacion-seller` | `contracts/events/sistema-de-reputacion-seller.json` |
| `sistema-de-reserva-global` | `contracts/events/sistema-de-reserva-global.json` |
| `sistema-de-reserva-nacional` | `contracts/events/sistema-de-reserva-nacional.json` |
| `sistema-de-seguridad` | `contracts/events/sistema-de-seguridad.json` |
| `sistema-de-soporte` | `contracts/events/sistema-de-soporte.json` |
| `sistema-de-usuarios` | `contracts/events/sistema-de-usuarios.json` |
| `sistema-geo-intelligence-map` | `contracts/events/sistema-geo-intelligence-map.json` |
| `sistema-gobernanza-multi-pais-app-camaleon` | `contracts/events/sistema-gobernanza-multi-pais-app-camaleon.json` |
| `sistema-unificado-take-rate-engine-revenue-rate-engine-v20` | `contracts/events/sistema-unificado-take-rate-engine-revenue-rate-engine-v20.json` |
| `waterfall-engine-v10` | `contracts/events/waterfall-engine-v10.json` |

## Ejemplo válido

```json
{
  "eventId": "c5f7382d-62d4-437c-a14e-91abf3f5a54b",
  "eventType": "sistema-de-usuarios.updated",
  "eventVersion": "v1.1",
  "occurredAt": "2026-02-07T10:49:00Z",
  "data": {"userId": "u-123", "status": "active"}
}
```

## Ejemplo inválido

```json
{
  "eventType": "otro.evento",
  "eventVersion": "1.1",
  "data": "texto"
}
```

Inválido porque faltan campos obligatorios (`eventId`, `occurredAt`), `eventVersion` no sigue formato `vN` y `data` debe ser objeto.
