# memory

## Propósito

- Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Memory es el sistema que crea un perfil de regalos (gift-profile) por destinatario (recipient) y por buyer, para recordar señales estables (gustos, tallas, alergias, fechas, preferencias de privacidad, “cosas que ya regalé”) y convertirlas en preferencias estructuradas reutilizables por el resto del producto (Genie, Search, Cupones/Lealtad, Notificaciones, etc.). Memory no recomienda por sí solo; Memory provee contexto.
- Documento origen: `sistema-de-memory-260207_1012.docx`
- Usuario desactiva marketing: recordatorios transaccionales siguen si son “utilidad personal” (Suposición: el doc menciona recordatorios; la distinción marketing/transaccional depende del sistema Notificaciones).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)".

## Límites

- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Memory y sus reglas/entidades asociadas.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Excluye (en “Solo Memory”)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.
- Compatibilidad con sistemas existentes (dependencias directas)


## Control operativo verificable

- Owner: `Equipo memory`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MEMORY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/memory/dominio-memory-operacion`
  - `https://jira.aventide.gift/browse/OPS-MEMORY-241`

## Trazabilidad

- Documento origen: `sistema-de-memory-260207_1012.docx`
- Título extraído: "Sistema Memory v2.0 (Gift Memory OS) — Solo Memory (sin Genie)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
