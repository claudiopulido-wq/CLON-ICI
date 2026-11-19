# Publicación del sitio ICI (certifyyourfuture.org)

Documento interno. El sitio en vivo es estático y está en **SiteGround, en la cuenta propia de ICI**. Claudio lo confirmó el 2026-11-18. No se usa ninguna cuenta ni sitio de GES Académico.

| Dato | Valor |
|---|---|
| Repo | `claudiopulido-wq/CLON-ICI`, rama `main` |
| Sitio | https://certifyyourfuture.org/ |
| Servidor SSH | `ssh.certifyyourfuture.org`, puerto `18765` |
| Carpeta destino | `~/www/certifyyourfuture.org/public_html/` |
| Workflow | `.github/workflows/deploy.yml` («Publicar en SiteGround») |

## Cómo funciona

1. La publicación se lanza **solo a mano** desde GitHub Actions. Un push a `main` no publica nada.
2. El job usa el entorno `production`, y GitHub **pausa cada ejecución hasta que Claudio la aprueba**. Esa aprobación es el «sí» que se necesita en cada publicación. Sin ella no se sube nada.
3. Se suben los archivos con `rsync` por SSH. La huella del servidor va fija en el workflow.
   - **No se borra nada del servidor**, porque no se usa `--delete`.
   - No se suben los scripts `*.py`, `preview_email.html`, `.github/`, `.claude/` ni este archivo.
4. Al final se comprueba que `/` y `/our-story.html` respondan 200.

Las claves y contraseñas **solo las captura Claudio** en GitHub. Nadie las escribe en el repo, en chats ni en notas.

## Configuración (una sola vez, la hace Claudio)

### A. Clave SSH en SiteGround
1. Entra a Site Tools de **certifyyourfuture.org** y ve a **Devs → SSH Keys Manager**.
2. Usa **Generate**. Nombre: `github-actions`. Elige una frase de acceso.
3. En la lista de claves, abre el menú ⋮ → **Private Key** y copia el texto completo, incluidas las líneas `-----BEGIN…` y `-----END…`.
4. En ⋮ → **SSH Credentials**, anota el **usuario** (algo como `u1234-abcd`). Revisa también que host y puerto coincidan con la tabla de arriba.

### B. Entorno y secretos en GitHub
1. En el repo, ve a **Settings → Environments → production**. Si no existe, créalo con **New environment**.
   - **Required reviewers**: `claudiopulido-wq`.
   - **Deployment branches**: solo `main`.
2. En ese mismo entorno, en **Environment secrets → Add secret**:
   - `SG_SSH_KEY`: la clave privada del paso A.3.
   - `SG_SSH_PASSPHRASE`: la frase de acceso del paso A.2.
   - `SG_USER`: el usuario del paso A.4.

## Publicar (cada vez)

1. Asegúrate de que lo que se va a publicar ya está en `main` (`git push`).
2. Ve a GitHub → **Actions → Publicar en SiteGround → Run workflow** (rama `main`).
   - La primera vez, o si hay dudas, marca **Simulación** (`dry_run`). Así ves la lista de archivos sin cambiar nada.
   - Un agente también puede lanzarlo con `gh workflow run deploy.yml -R claudiopulido-wq/CLON-ICI`, pero solo después del «sí» de Claudio.
3. GitHub muestra **Review deployments**. Claudio revisa y pulsa **Approve and deploy**.
4. Verifica en vivo (ver abajo).

### Verificación en vivo
```bash
curl -sI "https://certifyyourfuture.org/our-story.html?v=$(date +%s)" | head -1        # 200
curl -s https://certifyyourfuture.org/our-story.html | grep -iE 'canonical|robots'    # canonical a sí misma, sin noindex
```
SiteGround tiene caché propia. Si se sigue viendo la versión vieja, ve a **Site Tools → Speed → Caching → Flush Cache**.

## WordPress: el panel lo marca, pero no hay nada en public_html
Site Tools muestra certifyyourfuture.org con ícono de WordPress. Pero el dry_run del 2026-11-19 (run 44570721217) listó el contenido real de `public_html`: solo están los HTML del 30-sep, `assets/`, `css/`, `js/`, `.well-known/`, `send_email.php` y `php_errorlog`. No hay archivos de WordPress ni `.htaccess`.
- Las respuestas 403 en `wp-admin/`, `wp-includes/` y `wp-content/` que se ven desde fuera son una regla de seguridad de SiteGround, no carpetas reales.
- Puede quedar una base de datos de WordPress en la cuenta. Borrarla solo se hace con el «sí» explícito de Claudio.

Antes de cada publicación, el paso «Mostrar qué hay hoy en el destino» lista `public_html`, los `index.*` y el `.htaccess`.

## Caché
Las páginas cargan `css/style.css?v=AAAAMMDD`. Cuando cambie el CSS, sube ese número en las 8 páginas para que los visitantes no vean el CSS viejo. Si aun así se ve la versión anterior, ve a Site Tools → Speed → Caching → Flush Cache.

## Revertir
Haz `git revert` del commit que causó el problema, haz push a `main` y publica de nuevo con el flujo normal, que también necesita aprobación. Como rsync no borra, un archivo **nuevo** que haya que quitar del servidor se elimina a mano desde el Administrador de archivos de Site Tools.

## Historial
| Fecha | Commit | Notas |
|---|---|---|
| 2026-09-30 | `cc485b5` | Subida manual previa. Es la versión que estaba en vivo antes de este método. |
