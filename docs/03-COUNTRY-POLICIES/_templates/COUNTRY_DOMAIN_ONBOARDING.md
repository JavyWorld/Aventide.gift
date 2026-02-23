# Country + Domain Onboarding Template

> Usar esta plantilla para habilitar un nuevo país + dominio local (`aventide.xx`) con cobertura técnica, operativa y de cumplimiento.

## Metadata
- `country_code`:
- `country_name`:
- `tenant_id`:
- `domain` (ej. `aventide.xx`):
- `owner_team`:
- `target_launch_date`:
- `status` (`draft` | `in_progress` | `ready` | `live`):

---

## 1) Dominio y DNS

### 1.1 Alta de dominio
- [ ] Dominio registrado: `aventide.xx`
- [ ] DNS zone creada en proveedor autorizado
- [ ] Contactos administrativos/técnicos definidos

### 1.2 Seguridad y entrega
- [ ] SSL/TLS provisionado (certificado válido y auto-renovación)
- [ ] CDN habilitado para el dominio
- [ ] WAF habilitado con baseline de reglas global

### 1.3 Cache y edge headers
- [ ] Reglas de cache definidas por tipo de contenido
- [ ] Invalidation strategy documentada
- [ ] Edge headers configurados (ejemplos):
  - [ ] `X-Country-Code`
  - [ ] `X-Tenant-Id`
  - [ ] `X-Request-Id`
  - [ ] Security headers (`HSTS`, `CSP`, etc.)

---

## 2) Routing y experiencia

### 2.1 Mapeo host -> country/tenant
- [ ] Hostname mapeado a `country_code`
- [ ] Hostname mapeado a `tenant_id`
- [ ] Configuración en servicio de routing desplegada y validada

### 2.2 Comportamiento en `aventide.com`
- [ ] Estrategia definida para usuarios del país:
  - [ ] Sugerencia de país en homepage
  - [ ] Redirect (si aplica) a `aventide.xx`
- [ ] Fallback definido para geolocalización incierta

### 2.3 Selector manual de país
- [ ] Selector visible y accesible
- [ ] Persistencia de preferencia (cookie/session/account)
- [ ] No rompe checkout ni sesión activa al cambiar de país

---

## 3) Configuración de negocio

### 3.1 Comercial
- [ ] Moneda local configurada
- [ ] Idioma por defecto configurado
- [ ] Formatos locales (fecha, dirección, teléfono)

### 3.2 Pagos y envíos
- [ ] Métodos de pago habilitados por país
- [ ] Métodos de envío habilitados por país
- [ ] Reglas de disponibilidad/zonas logísticas validadas

### 3.3 Impuestos
- [ ] Reglas fiscales e impuestos configurados
- [ ] Cálculo validado con casos de prueba representativos
- [ ] Mensajería de precios/impuestos revisada

---

## 4) Cumplimiento

### 4.1 Checklist legal/fiscal/privacidad
- [ ] Legal aprobado
- [ ] Fiscal/tributario aprobado
- [ ] Privacidad y protección de datos aprobado

### 4.2 Documentación local requerida
- [ ] ADR local creado/actualizado: `docs/adr/ADR-XXXX-<country>-domain-onboarding.md`
- [ ] `docs/03-COUNTRY-POLICIES/<CC>/POLICY_OVERRIDES.md` actualizado
- [ ] `docs/03-COUNTRY-POLICIES/<CC>/COMPLIANCE_CHECKLIST.md` alineado

---

## 5) Observabilidad y operación

### 5.1 Dashboards por país
- [ ] Dashboard operativo por país creado
- [ ] Dashboard de negocio por país creado
- [ ] Alertas principales configuradas

### 5.2 Métricas mínimas requeridas
- [ ] Tráfico por host/país
- [ ] Conversión por país
- [ ] Fallas de resolución de tenant
- [ ] Redirecciones (tasa y errores)
- [ ] Errores de policy (autorización/reglas/compliance)

### 5.3 Runbook de incidentes routing multi-país
- [ ] Runbook creado o referenciado
- [ ] Escalación on-call definida
- [ ] Simulación/tabletop ejecutada

---

## Go/No-Go
- [ ] Validación técnica final
- [ ] Validación de negocio final
- [ ] Validación de cumplimiento final
- [ ] Sign-off de lanzamiento

## Notas
- Riesgos abiertos:
- Decisiones pendientes:
- Dependencias externas:
