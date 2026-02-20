# 01 · Glosario maestro

Este glosario define el vocabulario oficial de la plataforma. Su objetivo es reducir ambigüedades entre dominios y países.

## Convención obligatoria

> **Toda nueva sigla o término debe incorporarse en este glosario antes de adoptarse en cualquier documento de dominio, especificación técnica, ADR o playbook operativo.**

Reglas operativas:
1. No introducir abreviaturas locales sin alta previa en este documento.
2. Si un término cambia de significado, actualizar primero aquí y luego propagar a dominios.
3. En caso de conflicto entre documentos, prevalece la definición de este glosario.

---

## Formato canónico de entradas

Cada término debe incluir:
- **Término**
- **Definición corta**
- **Definición extendida**
- **Alias permitidos/prohibidos**
- **Dominio dueño**
- **Ejemplo de uso correcto**
- **Anti-ejemplo**
- **Referencias a dominios donde aplica**

---

## Glosario

### Dinero y pagos

#### 1) Monto bruto (Gross Amount)
- **Definición corta:** Valor total cobrado al comprador antes de descuentos, comisiones, impuestos retenidos y ajustes.
- **Definición extendida:** Base monetaria inicial de una transacción. Se utiliza para auditoría, conciliación y cálculo de tasas, pero no representa el ingreso neto ni el payout final.
- **Alias permitidos:** `Monto bruto`, `Gross Amount`.
- **Alias prohibidos:** `Total neto`, `Cobro final seller`.
- **Dominio dueño:** Pagos.
- **Ejemplo correcto:** “La conciliación parte del **monto bruto** y luego aplica comisiones e impuestos.”
- **Anti-ejemplo:** “El **monto bruto** es lo que recibe el seller en su cuenta.”
- **Dominios donde aplica:** Órdenes, Facturación, Auditoría, Analítica.

#### 2) Monto neto liquidable (Net Settlement Amount)
- **Definición corta:** Monto efectivamente transferible al seller tras deducciones y ajustes válidos.
- **Definición extendida:** Resultado posterior a comisiones, impuestos, promociones financiadas por seller, penalidades y contracargos aplicables al ciclo de liquidación.
- **Alias permitidos:** `Neto liquidable`, `Net Settlement Amount`.
- **Alias prohibidos:** `Monto bruto`, `Payout bruto`.
- **Dominio dueño:** Pagos.
- **Ejemplo correcto:** “El **neto liquidable** del ciclo semanal fue de 12,430.50.”
- **Anti-ejemplo:** “El **neto liquidable** no considera disputas cerradas en contra.”
- **Dominios donde aplica:** Disputas, Facturación, Crédito interno, Auditoría.

#### 3) Liquidación (Settlement)
- **Definición corta:** Proceso de cálculo, aprobación y ejecución de transferencias monetarias.
- **Definición extendida:** Incluye ventana de corte, validaciones de riesgo/cumplimiento, cálculo de netos, generación de lote bancario y confirmación de pago.
- **Alias permitidos:** `Liquidación`, `Settlement`.
- **Alias prohibidos:** `Pago inmediato` (cuando existe ciclo), `Reembolso`.
- **Dominio dueño:** Pagos.
- **Ejemplo correcto:** “La **liquidación** T+2 corre al cierre de las 23:00 UTC.”
- **Anti-ejemplo:** “La **liquidación** es sinónimo de devolución al buyer.”
- **Dominios donde aplica:** Finanzas, Cumplimiento, Soporte, Auditoría.

#### 4) Contracargo (Chargeback)
- **Definición corta:** Reversión forzada de un pago iniciada por el emisor del medio de pago.
- **Definición extendida:** Evento financiero y de riesgo que puede implicar pérdida de principal, fee y evidencia documental para defensa dentro de un SLA.
- **Alias permitidos:** `Contracargo`, `Chargeback`.
- **Alias prohibidos:** `Reembolso voluntario`, `Disputa interna simple`.
- **Dominio dueño:** Disputas.
- **Ejemplo correcto:** “El caso se marcó como **contracargo** con plazo de defensa de 7 días.”
- **Anti-ejemplo:** “Todo reembolso solicitado por soporte es **contracargo**.”
- **Dominios donde aplica:** Pagos, Riesgo, Soporte, Auditoría.

---

### Cumplimiento y regulación

#### 5) KYC (Know Your Customer)
- **Definición corta:** Proceso de verificación de identidad del cliente.
- **Definición extendida:** Conjunto de controles para identificar, verificar y mantener evidencia del titular, conforme a exigencias regulatorias por país y nivel de riesgo.
- **Alias permitidos:** `KYC`.
- **Alias prohibidos:** `Validación básica de perfil`.
- **Dominio dueño:** Cumplimiento.
- **Ejemplo correcto:** “No se habilita retiro hasta completar **KYC** nivel requerido.”
- **Anti-ejemplo:** “Con email verificado ya se considera **KYC** completo.”
- **Dominios donde aplica:** Usuarios, Pagos, Seguridad, Gobernanza multi-país.

#### 6) AML (Anti-Money Laundering)
- **Definición corta:** Controles para prevenir lavado de dinero.
- **Definición extendida:** Monitoreo transaccional y de comportamiento para detectar patrones sospechosos, generar alertas y escalar reportes regulatorios según jurisdicción.
- **Alias permitidos:** `AML`.
- **Alias prohibidos:** `Filtro antifraude simple`.
- **Dominio dueño:** Cumplimiento.
- **Ejemplo correcto:** “La operación quedó retenida por regla **AML** de umbral agregado.”
- **Anti-ejemplo:** “**AML** aplica solo a cuentas enterprise.”
- **Dominios donde aplica:** Pagos, Riesgo, Auditoría, Gobernanza multi-país.

#### 7) PEP (Persona Expuesta Políticamente)
- **Definición corta:** Persona con rol público relevante y exposición de riesgo regulatorio.
- **Definición extendida:** Categoría de riesgo que requiere debida diligencia reforzada, revisión periódica y trazabilidad de aprobación.
- **Alias permitidos:** `PEP`, `Persona Expuesta Políticamente`.
- **Alias prohibidos:** `Usuario VIP`.
- **Dominio dueño:** Cumplimiento.
- **Ejemplo correcto:** “El alta de cuenta PEP exige revisión manual y aprobación dual.”
- **Anti-ejemplo:** “PEP se clasifica por volumen de ventas, no por rol público.”
- **Dominios donde aplica:** Usuarios, Seguridad, Auditoría.

---

### Seguridad

#### 8) MFA (Multi-Factor Authentication)
- **Definición corta:** Autenticación que exige dos o más factores de verificación.
- **Definición extendida:** Mecanismo para reducir toma de cuentas usando factores de conocimiento, posesión o inherencia; su política varía por operación sensible.
- **Alias permitidos:** `MFA`, `Autenticación multifactor`.
- **Alias prohibidos:** `Doble contraseña`.
- **Dominio dueño:** Seguridad.
- **Ejemplo correcto:** “Para cambio de cuenta bancaria se requiere **MFA** step-up.”
- **Anti-ejemplo:** “Enviar OTP opcional ya cumple política **MFA obligatoria**.”
- **Dominios donde aplica:** Usuarios, Pagos, Soporte.

#### 9) Tokenización de datos sensibles
- **Definición corta:** Sustitución de datos críticos por tokens no explotables fuera de contexto.
- **Definición extendida:** Técnica de protección de datos (por ejemplo PAN o documento) para limitar exposición y alcance de cumplimiento.
- **Alias permitidos:** `Tokenización`, `Tokenización de datos sensibles`.
- **Alias prohibidos:** `Cifrado reversible simple` (cuando no hay vault/token service).
- **Dominio dueño:** Seguridad.
- **Ejemplo correcto:** “El PAN nunca se persiste; solo se almacena su **token**.”
- **Anti-ejemplo:** “Base64 del número de tarjeta cuenta como **tokenización**.”
- **Dominios donde aplica:** Pagos, Cumplimiento, Auditoría.

#### 10) Incidente de seguridad
- **Definición corta:** Evento confirmado que compromete confidencialidad, integridad o disponibilidad.
- **Definición extendida:** Requiere clasificación de severidad, contención, erradicación, recuperación y post-mortem con acciones preventivas.
- **Alias permitidos:** `Incidente de seguridad`, `Security Incident`.
- **Alias prohibidos:** `Bug menor` (si no hay impacto CIA), `Ticket técnico`.
- **Dominio dueño:** Seguridad.
- **Ejemplo correcto:** “Se declaró **incidente de seguridad SEV-1** por acceso no autorizado.”
- **Anti-ejemplo:** “Todo timeout de API es automáticamente incidente de seguridad.”
- **Dominios donde aplica:** Soporte, Auditoría, Gobernanza.

---

### Disputas

#### 11) Disputa
- **Definición corta:** Proceso formal para resolver desacuerdo transaccional entre partes.
- **Definición extendida:** Flujo con estados, evidencia, responsables y resolución vinculante (a favor buyer/seller/plataforma), con efectos contables y reputacionales.
- **Alias permitidos:** `Disputa`.
- **Alias prohibidos:** `Queja informal`, `Ticket de soporte`.
- **Dominio dueño:** Disputas.
- **Ejemplo correcto:** “La **disputa** pasó a etapa de evidencia documental.”
- **Anti-ejemplo:** “Cualquier conversación de chat abierta es una **disputa**.”
- **Dominios donde aplica:** Soporte, Pagos, Reputación buyer/seller.

#### 12) Evidencia de disputa
- **Definición corta:** Conjunto de pruebas verificables usadas para sustentar una resolución.
- **Definición extendida:** Puede incluir logs firmados, comprobantes, trazas de entrega, comunicaciones y políticas aplicables con sello temporal.
- **Alias permitidos:** `Evidencia`, `Evidencia de disputa`.
- **Alias prohibidos:** `Opinión del agente`, `Captura sin contexto`.
- **Dominio dueño:** Disputas.
- **Ejemplo correcto:** “La **evidencia** incluye OTP validado y geolocalización del evento.”
- **Anti-ejemplo:** “Sin trazabilidad, el comentario interno basta como **evidencia**.”
- **Dominios donde aplica:** Seguridad, Auditoría, Soporte.

---

### Geografía y cobertura

#### 13) País operativo
- **Definición corta:** Jurisdicción donde existe operación habilitada de la plataforma.
- **Definición extendida:** Define reglas regulatorias, fiscales, medios de pago disponibles y políticas comerciales válidas.
- **Alias permitidos:** `País operativo`.
- **Alias prohibidos:** `Región` (si no es jurisdicción país), `Mercado genérico`.
- **Dominio dueño:** Gobernanza multi-país.
- **Ejemplo correcto:** “El producto se habilita solo en **países operativos** con KYC activo.”
- **Anti-ejemplo:** “Un idioma habilitado implica automáticamente **país operativo**.”
- **Dominios donde aplica:** Cumplimiento, Pagos, Facturación, Soporte.

#### 14) Cobertura geográfica
- **Definición corta:** Alcance territorial efectivo de servicios y operaciones.
- **Definición extendida:** Determina disponibilidad por zona/ciudad/área de servicio, con restricciones por logística, riesgo y normativa local.
- **Alias permitidos:** `Cobertura geográfica`, `Cobertura`.
- **Alias prohibidos:** `Disponibilidad global` (cuando hay restricciones).
- **Dominio dueño:** Cobertura.
- **Ejemplo correcto:** “La **cobertura geográfica** en la ciudad A excluye zona rural.”
- **Anti-ejemplo:** “Si existe una orden histórica, la **cobertura** es vigente.”
- **Dominios donde aplica:** Reserva nacional/global, Geo Intelligence Map, Soporte.

---

### Soporte

#### 15) SLA de soporte
- **Definición corta:** Tiempo objetivo comprometido para respuesta y/o resolución de casos.
- **Definición extendida:** Acuerdo medible por prioridad, canal y tipo de incidente, con relojes de negocio y reglas de pausa/reapertura.
- **Alias permitidos:** `SLA`, `SLA de soporte`.
- **Alias prohibidos:** `Tiempo estimado informal`.
- **Dominio dueño:** Soporte.
- **Ejemplo correcto:** “El caso P1 incumplió **SLA de primera respuesta** por 12 minutos.”
- **Anti-ejemplo:** “Resolver rápido cuando se pueda también cuenta como SLA.”
- **Dominios donde aplica:** Disputas, Seguridad, Operaciones.

#### 16) Escalamiento
- **Definición corta:** Derivación formal de un caso a un nivel de mayor especialización o autoridad.
- **Definición extendida:** Puede ser funcional (otro equipo) o jerárquico (aprobación/decisión), preservando contexto, trazabilidad y reloj SLA.
- **Alias permitidos:** `Escalamiento`, `Escalación`.
- **Alias prohibidos:** `Reasignación sin contexto`, `Pase manual informal`.
- **Dominio dueño:** Soporte.
- **Ejemplo correcto:** “Se ejecutó **escalamiento funcional** a Seguridad con bitácora completa.”
- **Anti-ejemplo:** “Mover el ticket entre colas sin criterio es **escalamiento**.”
- **Dominios donde aplica:** Seguridad, Disputas, Gobernanza.

---

### Gobernanza multi-país

#### 17) Política global
- **Definición corta:** Norma base común aplicable a todas las jurisdicciones, salvo excepción explícita.
- **Definición extendida:** Marco corporativo transversal que define mínimos obligatorios de seguridad, cumplimiento y operación para toda la plataforma.
- **Alias permitidos:** `Política global`.
- **Alias prohibidos:** `Regla local`, `Convenio de equipo`.
- **Dominio dueño:** Gobernanza multi-país.
- **Ejemplo correcto:** “La retención mínima de logs responde a **política global**.”
- **Anti-ejemplo:** “Cada país puede ignorar la política global sin excepción documentada.”
- **Dominios donde aplica:** Seguridad, Auditoría, Cumplimiento, Plataforma.

#### 18) Excepción local documentada
- **Definición corta:** Desviación aprobada de una política global por requisito legal/regulatorio local.
- **Definición extendida:** Debe contar con fundamento normativo, fecha de vigencia, responsable y plan de revisión periódica.
- **Alias permitidos:** `Excepción local documentada`, `Excepción local`.
- **Alias prohibidos:** `Arreglo temporal permanente`, `Bypass operativo`.
- **Dominio dueño:** Gobernanza multi-país.
- **Ejemplo correcto:** “La residencia de datos en país X opera por **excepción local documentada**.”
- **Anti-ejemplo:** “Se cambió el flujo por presión operativa sin registro de excepción.”
- **Dominios donde aplica:** Cumplimiento, Seguridad, Datos, Infraestructura.

#### 19) Matriz país-regla
- **Definición corta:** Inventario oficial de reglas por país, producto y dominio.
- **Definición extendida:** Tabla de trazabilidad que vincula políticas, obligaciones y capacidades habilitadas por jurisdicción, con versionado.
- **Alias permitidos:** `Matriz país-regla`.
- **Alias prohibidos:** `Checklist suelto`, `Wiki no controlada`.
- **Dominio dueño:** Gobernanza multi-país.
- **Ejemplo correcto:** “La habilitación de wallets se validó contra la **matriz país-regla**.”
- **Anti-ejemplo:** “Se lanzó por intuición sin revisar matriz vigente.”
- **Dominios donde aplica:** Producto, Cumplimiento, Pagos, Soporte.

---

## Notas de mantenimiento

- Toda propuesta de término nuevo debe incluir dueño y fecha de alta.
- Si un alias prohibido se detecta en documentación vigente, abrir tarea de normalización.
- Revisar este documento en cada release cross-dominio de alto impacto.
