# reservas-country

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)
- Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)

## Dependencias
- Integración con Waterfall Engine para cubrir pérdidas (Layer 1).
- si aplica: ejecuta payout vía proveedor (por Integraciones/Pagos).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Pagos/Integraciones
- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
- Título extraído: "Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)".
