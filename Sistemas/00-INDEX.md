# Sistemas · Índice estructurado

Este índice organiza las 37 especificaciones base del proyecto en clústeres funcionales para facilitar diseño, implementación y operación.

## Principios de organización

- **Canónico por dominio:** el detalle normativo final vive en `docs/02-DOMAINS/*`.
- **Trazabilidad:** cada sistema aquí se mapea a su dominio canónico.
- **Cohesión funcional:** los archivos se agrupan por dependencias operativas reales.

## Estructura

1. [`01-identidad-seguridad/`](./01-identidad-seguridad/) · IAM, jerarquía y controles de seguridad.
2. [`02-comercial-catalogo/`](./02-comercial-catalogo/) · contenido y búsqueda.
3. [`03-ordenes-fulfillment/`](./03-ordenes-fulfillment/) · órdenes, cobertura y capacidad.
4. [`04-finanzas-ingresos/`](./04-finanzas-ingresos/) · pagos, precios, facturación e incentivos.
5. [`05-riesgo-compliance/`](./05-riesgo-compliance/) · disputas, auditoría, reputación, reservas.
6. [`06-experiencia-comunicacion/`](./06-experiencia-comunicacion/) · soporte, mensajería, notificaciones, memory/genie.
7. [`07-datos-plataforma/`](./07-datos-plataforma/) · integraciones, continuidad, backups, observabilidad, analítica, archivos.
8. [`08-gobernanza-expansion/`](./08-gobernanza-expansion/) · gobernanza multi-país.

## Cobertura actual

- **Total sistemas fuente en `/Sistemas`:** 37
- **Estado esperado:** todos con mapeo a dominio canónico.
- **Diferencia conocida vs universo canónico 38:** `platform-structure` se mantiene solo en `docs/07-SISTEMAS-TRANSCRITOS/platform-structure.md` y `docs/02-DOMAINS/platform-structure/`.

## Mapa de migración de rutas

Consulta [`MIGRATION_MAP.md`](./MIGRATION_MAP.md) para equivalencias `ruta legacy -> ruta nueva`.
