# ADR-0001: Contexto y decisiones clave (support)

- **Estado**: Aprobado
- **Contexto**: Order Dashboard 360° (caja negra): timeline + tridente + señales de riesgo.

## Decisiones
- Order Dashboard 360° (caja negra): timeline + tridente + señales de riesgo.
- Acciones operativas controladas (botones con guardrails): reenvío de PIN, extender timers, congelar fondos, solicitar reembolso (no ejecuta libre).
- Se activa por señales como: seller no llega, buyer no responde, dirección dudosa, riesgo de fallo del tridente, bloqueo operativo. Se enruta con alta prioridad a L3 (Country Ops Lead).
- Buyer extorsiona (“pago extra o disputa”): se revisa GPS/PIN/foto + patrón; escalar a T&S.
- Señales internas: “usuario con 30% disputas”, “seller con reportes de calidad” y detector de colusión por IP/dispositivo/GPS patrón.
- Decisión sin evidencia → caja negra + tridente + señales de riesgo como base objetiva.

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
