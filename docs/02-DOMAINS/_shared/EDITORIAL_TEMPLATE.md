# Plantilla editorial estricta (dominios canónicos)

## Reglas globales
- Estructura obligatoria por tipo de archivo respetando títulos/orden de secciones.
- Todo bullet debe ser verificable, sin numeración heredada (`1)`, `2)`, `3)`).
- Prohibido texto de relleno (`TODO`, `TBD`, `por definir`, placeholders vacíos).
- Incluir trazabilidad explícita al `.docx` de origen.
- Cerrar siempre con checklist de calidad documental.

## README.md
### Campos obligatorios
- `# <dominio>`
- `## Propósito`
- `## Límites`
- `## Dependencias`
- `## Trazabilidad`
- `## Checklist de calidad documental`
### Campos prohibidos
- Detalle de endpoints HTTP.
- Tabla de códigos de error API.
- Tabla de estados/transiciones detalladas.

## API_CONTRACTS.md
### Campos obligatorios
- `# API_CONTRACTS · <dominio>`
- `## Endpoints`
- `## Auth`
- `## Códigos de error`
- `## Idempotency`
- `## Trazabilidad`
- `## Checklist de calidad documental`
### Campos prohibidos
- Narrativa de propósito del dominio (mover a README).
- Definición de máquina de estados (mover a STATE_MACHINE).
- Listas de placeholders o pasos numerados heredados.

## STATE_MACHINE.md
### Campos obligatorios
- `# STATE_MACHINE · <dominio>`
- `## Estados`
- `## Transiciones`
- `## Triggers`
- `## Trazabilidad`
- `## Checklist de calidad documental`
### Campos prohibidos
- Endpoints/autenticación HTTP.
- Catálogo de errores API.
- Secciones de alcance/dependencias generales (mover a README).
