# Auditoría de certifyyourfuture.org (2026-11-25)

Documento interno, hecho por el agente web. Es **solo de lectura**: no se publicó ni se cambió nada. Revisé el sitio en vivo (commit `b726822`) con un rastreo automático de las 9 páginas, curl, axe-core (WCAG 2 A/AA) y mediciones en el navegador con vista de celular (375 px).

**Respuesta corta a Claudio:** no, el sitio no está «perfecto».
- **Lo que sí está bien:** los enlaces funcionan (ninguno da 404) y la página del curso en línea está bien armada para Google.
- **Lo que falta:**
  - Dos huecos legales para EE. UU.: no hay aviso de privacidad aunque el quiz pide datos personales, y no hay términos.
  - Textos que prometen cosas que ICI no puede respaldar.
  - Las páginas presenciales tienen muy poco contenido y ninguna forma de inscribirse.
  - No hay analítica, así que hoy no se puede medir nada.

Prioridades: 🔴 crítico (riesgo legal o de confianza), 🟠 importante, 🟡 mejora.

---

## 1. Enlaces y formularios

**Resultado:** revisé 45 enlaces distintos y todos responden 200: internos, portal, WhatsApp, Google Fonts, Font Awesome, Unsplash y GES. No hay ningún enlace roto.

| Destino | Estado |
|---|---|
| «Online Course» (encabezado y hero) → `learn…/portal?course=train-with-a-plan` | 200 ✔ |
| «Watch a free lesson» → `…&lesson=1` (también `&lesson=2` en el temario) | 200 ✔. Abre sin cuenta (lo probé el 23-nov). |
| «Enroll now» → `…/portal?enroll=train-with-a-plan` | 200 ✔ |
| «Student Login» (pie) → `…/portal` | 200 ✔ |
| WhatsApp `wa.me/19567393519` (5 lugares) | 200 ✔. **Claudio debe confirmar que ese número es de ICI y que alguien lo atiende.** |
| Email `mailto:contact@certifyyourfuture.org` | Ver 🔴 F1 |
| «Courses» | No existe en el sitio. Solo está en el portal. |

**Hallazgos:**
- 🔴 **F1. No sé si los correos a contact@ llegan.** El dominio recibe correo en Google Workspace (MX smtp.google.com, SPF correcto). Pero en pendientes sigue abierto «Alias contact@ en el grupo contacto@». Lo usan los avisos del quiz (`send_email.php`) y el botón Email. Si el alias no existe, **se pierden los prospectos sin que nadie lo note**. Hay que mandar una prueba real: Claudio llena el quiz con sus datos y confirma que el aviso llega con teléfono y respuestas.
- 🔴 **F2. No hay redirección a https ni a la versión sin www.** `http://certifyyourfuture.org/`, `http://www.…` y `https://www.…` responden 200 sin redirigir. Un visitante puede navegar sin cifrado, y Google ve el sitio duplicado; el canonical lo mitiga pero no lo resuelve. Se arregla con 3 líneas en `.htaccess`, más el certificado de `www`, si ya existe. Es una publicación normal.
- 🟠 **F3. La página 404 es la genérica de SiteGround**, sin logo ni menú. Hay que hacer un `404.html` propio, con `ErrorDocument` en `.htaccess`.
- 🟡 **F4. Los menús CERTIFICATIONS y CONTACT usan `href="#"`.** Funcionan, pero no avisan a los lectores de pantalla que abren un submenú. Ver la sección 4.
- ✔ Los archivos sensibles están protegidos: `php_errorlog` y `.htaccess` → 403. `send_email.php` → 405 a GET. `preview_email.html` → 404 (no se sube).

---

## 2. Redacción

Encontré la palabra «certification» o «certified» **en todas las páginas**, porque está en el megamenú, más promesas sin respaldo. Claudio ya decidió dejar los **titles** con «Certification» en las páginas presenciales. Lo de abajo es lo demás, y casi todo necesita su decisión.

| # | Texto (dónde) | Problema | Propuesta |
|---|---|---|---|
| 🔴 R1 | «**International certification.**» (resultado del quiz para Sculpt & Burn, portada) | Afirma una certificación internacional que no existe. Es lo más riesgoso del sitio. | Quitarlo ya. |
| 🔴 R2 | «Its content is reviewed by a **certified fitness trainer**» (Our Story) | En pendientes sigue abierto «entrenador certificado». Si todavía no hay uno, la frase es falsa. | Quitarla hasta que exista, o confirmar quién es. |
| 🔴 R3 | «More than a certification, ICI is a **pathway to professional success**… build a successful future» (portada) · «**Career guidance after graduation**» (Sculpt) · «Graduate prepared to… **build your own fitness business**» (paquete) · «Perfect addition to your fitness **career**» (quiz) · «start your fitness **career** path today» (in-person) | Prometen resultados de carrera o negocio. Va contra la regla de no prometer resultados. | Cambiarlos por lo que el programa enseña, sin prometer resultados. |
| 🟠 R4 | «**Save** compared to enrolling separately» (quiz) · «⭐ **Best Value**» (megamenú y tarjeta) | Prometen ahorro sin precios publicados. | Quitarlos hasta que haya precios. |
| 🟠 R5 | «View the details of our upcoming edition, including the **date, city, venue**, and schedule» (portada, in-person y megamenú) | Promete fechas y sedes que no existen en el sitio (U3 de la revisión del 20-nov). | Cambiarlo por «Ask us about upcoming dates» con WhatsApp, o publicar la próxima edición real. |
| 🟠 R6 | Competency: «earn a **certificate of completion**» y, en la misma página, «does not guarantee **certification**» y «📋 **Certification** Awarded Upon Successful Evaluation». En la portada: «Competency Assessments **Certifications**». | Se contradice: ¿certificado de terminación o certificación? | Usar un solo término en toda la página. Lo decide Claudio. |
| 🟠 R7 | Insignias «🎓 In-Person Professional Certification» y «🎓 Three Professional Certifications» | Pendiente U4. Claudio dijo mantenerlas por el futuro centro evaluador, pero ese acuerdo todavía no existe. | Decisión de Claudio. Recomiendo quitar «Professional» mientras tanto. |
| 🟠 R8 | Página de Pilates: title «**Instructor de Pilates** \| ICI», en español. URLs en español: `instructor-de-pilates.html` y `paquete-entrenador-elite.html`. | El cliente ve español y el SEO sale mal. | Title «Mat Pilates Instructor Training \| ICI», sujeto a la decisión del nombre. Las URLs pueden cambiar a `mat-pilates.html` y `movement-coach-package.html` con redirección 301. |
| 🟡 R9 | Our Story menciona a GES Académico, CONOCER y México | Está aprobado por Claudio (18-nov) y aclara que no son certificaciones del CONOCER. Choca con la regla de «nada de México». | Confirmar que se queda. |
| 🟡 R10 | Pie: «Building the Next Generation of Fitness Professionals» | Aceptable como lema, pero «Professionals» junto con todo lo anterior refuerza la idea de credencial profesional. | Revisarlo junto con R3. |

**Lo que está bien:**
- La página `online-course.html` aclara bien «Certificate of Completion… not a professional license» y el aviso médico.
- No aparecen CURP, pesos ni MXN.
- Inglés de EE. UU. sin faltas de ortografía en lo que revisé.

**Falta un deslinde visible en todo el sitio:** hoy solo está en la página del curso. Propuesta para el pie: «ICI programs are educational. They do not replace advice from a physician. A Certificate of Completion is not a professional license.»

---

## 3. SEO técnico

| Página | Title | Description | H1 | Canonical | og/twitter | JSON-LD |
|---|---|---|---|---|---|---|
| / | ✔ (66) | ✔ | ✔ «STEP INTO COACHING» | ✔ | ✔ | ✖ |
| online-course | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ Course |
| in-person | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| competency | ✔ | ✔ | 🟠 **no tiene** | ✔ | ✔ | ✖ |
| sculpt-and-burn | ✔ | ✔ | 🟠 **no tiene** | ✔ | ✔ | ✖ |
| barre | ✔ | ✔ | 🟠 **no tiene** | ✔ | ✔ | ✖ |
| pilates | 🟠 en español | ✔ | ✔ | ✔ | ✔ | ✖ |
| paquete | ✔ | ✔ | 🟠 **no tiene** | ✔ | ✔ | ✖ |
| our-story | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |

- ✔ Titles y descriptions únicos. `lang="en"`. robots.txt permite todo y apunta al sitemap (9 URLs). Todas las `<img>` tienen alt.
- 🟠 **S1. Cuatro páginas sin H1:** el título visible es un `<h2>` o un `<div>`. Se arregla en 10 minutos.
- 🟠 **S2. Las páginas presenciales tienen poco contenido** (unas 60–100 palabras: un hero y una insignia). Google las ve como páginas delgadas y el visitante no tiene qué leer. La de Pilates es la única con contenido real.
- 🟠 **S3. No hay JSON-LD `Organization`** (nombre, logo, url, contacto, sameAs) en la portada. Sí conviene ponerlo.
  - `FAQPage`: Google ya casi no muestra resultados de FAQ para sitios comerciales. No vale la pena.
  - `Course`: ya está en online-course.
- 🟡 **S4. hreflang:** no aplica mientras el sitio solo esté en inglés.
- 🟠 **S5. Search Console:** el DNS tiene un `google-site-verification`, así que alguien verificó el dominio, quizá solo para Workspace. **Claudio debe confirmar que tiene acceso a Search Console** y enviar `sitemap.xml` ahí.
- 🔴 **S6. No hay analítica** (ni GA4, ni gtag, ni GTM). Hoy no se puede saber cuántos visitantes llegan, de dónde vienen ni cuántos hacen clic en «Watch a free lesson» o «Enroll». Para un sitio que vende, esto es crítico. Requiere un banner de cookies si hay visitantes de la UE o California; con GA4 en modo de consentimiento básico basta.

**Rendimiento (Core Web Vitals):** no pude correr PageSpeed porque la API pública agotó su cuota diaria, y no se permitió Lighthouse local. Medí en el navegador con vista de celular:
- CLS 0.000 en las 4 páginas: no hay saltos de contenido.
- Sin desborde horizontal a 375 px.
- 🟠 **S7. Imágenes pesadas o mal dimensionadas:**
  - El megamenú carga en **todas** las páginas miniaturas de 60 px que en realidad son imágenes de 1600–1920 px: `portada_1.webp` 224 KB, `block2.webp` 283 KB, `Block2_final.webp` 173 KB y `para-mail.jpg`.
  - El logo de 1063 px se muestra a 108–144 px.
  - Arreglo: miniaturas de 120 px, logo de 300 px y `loading="lazy"` en el megamenú. Ahorra unos 600 KB por página en el primer acceso desde celular.
- 🟡 **S8. Cuatro fotos se cargan directo desde images.unsplash.com.** La licencia de Unsplash lo permite, pero el sitio depende de un tercero. Mejor copiarlas a `assets/` en webp.
- **Pendiente:** que Claudio corra https://pagespeed.web.dev con la portada y online-course (modo móvil) y pase las cifras de LCP e INP. Yo no tengo cifras reales de campo.

---

## 4. Experiencia de usuario (UX) y accesibilidad

### Recorrido del visitante hasta inscribirse
1. **Llega a la portada.** El hero dice «Step into coaching» y luego ofrece el curso en línea o «in-person training programs». Hay dos mensajes distintos: «coaching», que suena a formar entrenadores, y un curso para quien ya entrena. 🟠 **U1.** Hay que decidir a quién le habla la portada primero.
2. **Curso en línea:** hero → bloque del curso → lección gratis o detalles → inscripción en el portal. **Este es el mejor recorrido del sitio:** son 2 o 3 clics, hay prueba gratis y una página con temario y preguntas frecuentes.
3. **Cursos presenciales:** portada → tarjeta → página de Barre o Sculpt → **no hay botón para inscribirse, ni precio, ni fechas**. El único botón lleva al curso en línea, que es otro tema. 🔴 **U2. El visitante interesado en lo presencial no tiene a dónde ir**, salvo WhatsApp en el menú.
4. **Competency:** no hay botón para aplicar (U6 del 20-nov). 🔴 Mismo caso.
5. **Quiz «Ask an Advisor»:** tiene 7 pasos, pide correo, nombre y teléfono, y promete «Our team will reach out to you by email». 🔴 Depende de F1 y de que alguien conteste. No ofrece el curso en línea como opción (🟠 **U3**).

### Lo que falta para generar confianza (sin inventar nada)
- 🔴 **U4. Aviso de privacidad y términos en el sitio.** El quiz recoge datos personales y en EE. UU. eso exige un aviso de privacidad (por ejemplo, la ley CalOPPA de California). El portal sí tiene `/legal/privacy` y `/legal/terms`. **Arreglo rápido:** enlazarlos desde el pie del sitio y desde el quiz. Que el texto aplique al sitio lo confirma el Director o el abogado de EE. UU. (pendiente en la lista).
- 🟠 **U5. Precio visible.** `precio_texto` es `null` en el portal. Para este público, no ver el precio frena la compra. Cuando Claudio lo defina, se pone en online-course y en la tarjeta de la portada.
- 🟠 **U6. Quién está detrás.** No aparecen el entrenador o instructores (con nombre, foto y su credencial real), ni el domicilio en Texas, ni el nombre legal de la empresa en el pie. Son señales básicas de confianza en EE. UU.
- 🟡 **U7. Prueba social.** No hay ninguna, y está bien así: no se inventa. Cuando haya alumnos reales, se piden reseñas con permiso por escrito.
- 🟡 **U8. Política de reembolso visible** junto a «Enroll now». Ya está en pendientes de Claudio.

### Accesibilidad (axe-core, WCAG 2 AA, portada)
- 🟠 **A1. Contraste insuficiente en los enlaces del pie:** #aaa sobre fondo oscuro da 2.32:1 y el mínimo es 4.5:1. Son 8 elementos.
- 🟠 **A2. El botón del menú en celular es un `<div>`**, así que con teclado no se puede abrir. Debe ser un `<button>`. Ya tiene aria-label y aria-expanded.
- 🟡 **A3. Los submenús (CERTIFICATIONS y CONTACT)** no tienen `aria-haspopup`/`aria-expanded` y usan `href="#"`.
- 🟡 **A4. No hay `<main>` ni enlace para saltar al contenido.**
- 🟡 **A5. El quiz valida con `alert()`.** Es mejor un mensaje junto al campo, con `aria-live`.

---

## 5. Propuestas priorizadas (impacto / esfuerzo)

| Prioridad | Propuesta | Impacto | Esfuerzo | ¿Quién decide? |
|---|---|---|---|---|
| 1 | Prueba real del quiz y del alias contact@ (F1) | Muy alto | 10 min | Claudio |
| 2 | Quitar «International certification», el «certified trainer» si no existe y las promesas de carrera (R1–R3) | Muy alto (legal) | 30 min | Director (textos) + Claudio |
| 3 | Enlazar Privacy y Terms en el pie y en el quiz; deslinde en el pie (U4) | Muy alto (legal) | 30 min | Director / abogado |
| 4 | Redirección a https y sin www; 404 propia (F2, F3) | Alto | 30 min | Agente web |
| 5 | GA4 con eventos «free_lesson_click», «enroll_click», «quiz_submit» y «whatsapp_click», más Search Console con el sitemap (S5, S6) | Muy alto (medición) | 1–2 h | Claudio da las cuentas de ICI |
| 6 | Formularios «Reserve your seat» (presencial) y «Apply for an assessment» (Competency), con aviso a contact@ y WhatsApp (U2) | Muy alto (ventas) | 3–4 h | Director (textos) + Claudio |
| 7 | Imágenes del megamenú y logo optimizados (S7, S8) | Medio | 1 h | Agente web |
| 8 | H1 en 4 páginas, JSON-LD Organization, title de Pilates (S1, S3, R8) | Medio | 1 h | Agente web / Director |
| 9 | Accesibilidad: contraste, botón del menú, submenús, `<main>` (A1–A5) | Medio | 2 h | Agente web |
| 10 | Contenido real en las páginas presenciales: qué se aprende, duración, requisitos, quién enseña y preguntas frecuentes (S2) | Alto | Depende del texto | Director + Claudio |
| 11 | Precio, política de reembolso y sección «Who teaches» (U5, U6, U8) | Alto | Depende de decisiones | Claudio |
| 12 | Unificar «certificate of completion» y «certification» en Competency y en las insignias (R6, R7) | Alto | 30 min, una vez decidido | Claudio |

**Nivel «enterprise», más adelante (cuando haya tráfico medido):**
- Pruebas A/B del hero.
- Píxel de Meta y Google Ads con consentimiento.
- CRM para los prospectos del quiz (por ejemplo, HubSpot gratis) en vez de un correo suelto.
- Página de estado y monitoreo de disponibilidad (UptimeRobot) para el sitio y el portal.
- Copia del sitio en un CDN con caché por URL.

No propongo cifras ni testimonios: no hay datos reales todavía.

---

## Lo que necesita decisión de Claudio
1. Confirmar que llegan los correos a contact@ (prueba del quiz) y que el WhatsApp +1 956-739-3519 es de ICI.
2. ¿Ya existe el «certified fitness trainer» de Our Story? Si no, se quita la frase.
3. Qué hacer con las insignias «Professional Certification» y el término de Competency (R6 y R7).
4. Si se quedan las menciones de GES, CONOCER y México en Our Story (R9).
5. Cuentas de ICI para GA4 y Search Console.
6. Precio del curso en línea y política de reembolso.
7. Arrancar los formularios de inscripción presencial y de Competency.
