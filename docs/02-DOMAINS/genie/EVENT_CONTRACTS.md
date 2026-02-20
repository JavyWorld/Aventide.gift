# EVENT_CONTRACTS · genie

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Multi-país contextual: re-evaluación por policy_context (clima/eventos/riesgo) por país/hub/zona.
- Telemetría de Genie (eventos de funnel) para analítica.
- COUNTRY_OPS_LEAD: gobierna policies (clima/eventos) que afectan candidatos; no “tunea” Genie por fuera del policy engine.
- PolicyGate (hard): restricciones por clima/eventos/riesgo.
- Policy gate (clima/eventos).
- 5.5 Policy Gate (clima/eventos/riesgo)
- 6.3 genie_events (telemetría)
- Eventos definidos:
- event_id, session_id, buyer_id, country/hub/zone, event_type, payload_json, created_at
- (event_type,created_at desc)

## Trazabilidad
- Documento origen: `sistema-de-genie-260207_1012.docx`
