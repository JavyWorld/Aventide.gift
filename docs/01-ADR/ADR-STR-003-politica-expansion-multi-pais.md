# ADR-STR-003: Política de expansión multi-país

## Estado
Aprobado

## Contexto
La plataforma opera sobre un marco multi-país y necesita un proceso explícito para priorizar nuevos países, fijar ownership legal-operativo y definir controles mínimos de entrada.

## Decisión
Establecer la arquitectura y patrón técnico inicial para la expansión multi-país bajo un enfoque de plataforma compartida y evolución progresiva:

1. **Arquitectura objetivo**
   - `aventide.com` se define como portal global y **control plane**.
   - `admin.aventide.com` y `api.aventide.com` conforman la capa central de administración y servicios.
   - `aventide.co`, `aventide.do` y `aventide.us` se definen como storefronts nacionales.

2. **Patrón técnico inicial**
   - Se adopta la **Opción A multi-tenant** sobre una plataforma compartida.
   - La resolución de contexto de país/tenant se hace por host (`Host` header) + `country_code` + `tenant_id`.
   - La configuración por país se gestiona en **governance-cameleon**, evitando hardcode específico por país.

3. **Política de geolocalización**
   - En `aventide.com` se implementa sugerencia de país con selector manual.
   - El auto-redirect se limita a la homepage; no se permite redirección agresiva en páginas internas.
   - La preferencia de país se persiste mediante cookie/session.

4. **SEO e internacionalización**
   - Se mantienen URLs separadas por país.
   - Se implementa estrategia de `hreflang` y canonical por cada sitio país.

5. **Consecuencias**
   - Se reduce la complejidad inicial de operación y despliegue.
   - Se habilita un escalado progresivo hacia despliegues separados por país cuando volumen o regulación lo exijan.

## Dominios afectados
- [Fiscalidad](../02-DOMAINS/FISCALIDAD.md)
- [Disputas](../02-DOMAINS/DISPUTAS.md)
- [Privacidad](../02-DOMAINS/PRIVACIDAD.md)
