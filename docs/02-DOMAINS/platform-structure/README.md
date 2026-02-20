# platform-structure

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- Regional OS incluye Studio para operar config/UI/merchandising bajo guardrails y auditoría.
- 2) Alcance

## Dependencias
- componentes (API, DB, workers, storage, webhooks, UI Config),
- Un core único (misma API/reglas/datos) para web+mobile+paneles.
- Separación explícita Client / Server / Integraciones para evitar acoplamientos peligrosos (especialmente dinero).
- Plano asíncrono obligatorio (BullMQ/workers) para integraciones y procesos críticos.
- Monorepo: apps (API/workers/webs/mobile/paneles) + packages (DTOs/contracts/UI-LEGO) + infra + docs/ADR.

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`
- Título extraído: "Estructura v2.0 (Estructura del Proyecto / Plataforma Aventide Gift)".
