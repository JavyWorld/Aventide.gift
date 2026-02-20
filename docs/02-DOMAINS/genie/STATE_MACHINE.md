# STATE_MACHINE · genie

## Estados detectados/derivados
- Multi-país contextual: re-evaluación por policy_context (clima/eventos/riesgo) por país/hub/zona.
- Wizard 3 pasos y su sesión (genie_session) con estado y respuestas.
- Telemetría de Genie (eventos de funnel) para analítica.
- COUNTRY_OPS_LEAD: gobierna policies (clima/eventos) que afectan candidatos; no “tunea” Genie por fuera del policy engine.
- PolicyGate (hard): restricciones por clima/eventos/riesgo.
- 4) Flujos end-to-end (happy path + edge cases)

## Transiciones y eventos de entrada/salida
- Multi-país contextual: re-evaluación por policy_context (clima/eventos/riesgo) por país/hub/zona.
- Telemetría de Genie (eventos de funnel) para analítica.
- COUNTRY_OPS_LEAD: gobierna policies (clima/eventos) que afectan candidatos; no “tunea” Genie por fuera del policy engine.
- PolicyGate (hard): restricciones por clima/eventos/riesgo.
- Policy gate (clima/eventos).
- 5.5 Policy Gate (clima/eventos/riesgo)
- Eventos definidos:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad
- Documento origen: `sistema-de-genie-260207_1012.docx`
