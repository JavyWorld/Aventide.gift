# ADR-0001: Contexto y decisiones clave (coupons)

- **Estado**: Aprobado
- **Contexto**: Pago falla o reservation expira: no se consume definitivamente; se libera hold y no cuenta como redención final (Suposición: consistente con patrón de reservas TTL del proyecto).

## Decisiones
- Pago falla o reservation expira: no se consume definitivamente; se libera hold y no cuenta como redención final (Suposición: consistente con patrón de reservas TTL del proyecto).
- Señales de abuso por patrón de redención → ticket/señal a Trust/Moderation.
- Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos → 10.2 Cupones del Seller”
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
