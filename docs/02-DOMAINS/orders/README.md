# orders

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (límites, ventanas, validaciones)
- Sistema de Órdenes v2.0 (corregido y unificado)

## Dependencias
- Sistema valida entregabilidad/capacidad (depende de Contenido/Capacidad).
- Si zona no activa / sin capacidad para la ventana: no se permite crear o se crea como “no confirmable” (según policy); en cualquier caso, no se debe pagar si no es entregable. (Integración obligatoria con Capacidad/Logística; aquí se fija el enforcement en el gate de checkout, coherente con “lo visible debe ser comprable”.)
- escrow JSON {provider, escrow_id, amount, currency, status}
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Integridad

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
- Título extraído: "Sistema de Órdenes v2.0 (corregido y unificado)".
