# ADR-0001: Contexto y decisiones clave (analytics)

- **Estado**: Aprobado
- **Contexto**: Moderación/Riesgo:USER_REPORTED, PRODUCT_REVIEWED, CONTENT_TAKEDOWN, ACCOUNT_SUSPENDED, FRAUD_FLAGGED, TRUST_SCORE_UPDATED

## Decisiones
- Moderación/Riesgo:USER_REPORTED, PRODUCT_REVIEWED, CONTENT_TAKEDOWN, ACCOUNT_SUSPENDED, FRAUD_FLAGGED, TRUST_SCORE_UPDATED
- Sistema de Analítica v2.0 (corregido y unificado)
- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema de Analítica es el “HUB central” que captura, consolida y expone métricas de negocio y operación del marketplace, derivadas de:
- Eventos críticos server-side (inmutables, append-only).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`
