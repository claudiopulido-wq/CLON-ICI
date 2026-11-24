"""Genera online-course.html a partir del JSON público del curso y de la plantilla de our-story.html."""
import json, sys, html
from pathlib import Path

repo = Path(sys.argv[1]); data = Path(sys.argv[2])
c = json.loads(data.read_text(encoding='utf-8'))['cursos'][0]
tpl = (repo / 'our-story.html').read_text(encoding='utf-8')
e = lambda s: html.escape(s, quote=True)

PORTAL = 'https://learn.certifyyourfuture.org/portal'
COURSE = f"{PORTAL}?course={c['slug']}"
FREE = f"{COURSE}&lesson={c['muestra_ids'][0]}"
ENROLL = f"{PORTAL}?enroll={c['slug']}"
URL = 'https://certifyyourfuture.org/online-course.html'

title = 'Train With a Plan: Online Strength & Conditioning Course | ICI'
desc = ("An intermediate online video course: measure your effort, progress week by week, "
        "move well under load and recover. Watch the first lesson free.")

head_end = tpl.index('</head>')
header_start = tpl.index('<body')
header_end = tpl.index('</header>') + len('</header>')
footer_start = tpl.index('<footer>')

head = tpl[:head_end]
head = head.replace('<title>Our Story | ICI</title>', f'<title>{e(title)}</title>')
head = head.replace(
    '<meta name="description" content="Who we are: ICI is an online fitness training company in Texas. Learn about our mission and the technology behind our courses.">',
    f'<meta name="description" content="{e(desc)}">')
head = head.replace('https://certifyyourfuture.org/our-story.html', URL)
assert e(title) in head and e(desc) in head and URL in head

ld = {
    "@context": "https://schema.org",
    "@type": "Course",
    "name": c['titulo'],
    "description": c['descripcion'],
    "url": URL,
    "inLanguage": "en",
    "educationalLevel": c['nivel'],
    "image": "https://certifyyourfuture.org/assets/og-online-course.jpg",
    "provider": {"@type": "Organization", "name": "ICI", "url": "https://certifyyourfuture.org/"},
    "teaches": c['aprenderas'],
    "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": f"PT{c['minutos']}M"},
}
head += f"""    <meta property="og:type" content="website">
    <meta property="og:site_name" content="ICI">
    <meta property="og:title" content="{e(c['titulo'])}">
    <meta property="og:description" content="{e(desc)}">
    <meta property="og:url" content="{URL}">
    <meta property="og:image" content="https://certifyyourfuture.org/assets/og-online-course.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
    </script>
"""

li = lambda items: '\n'.join(f'                    <li>{e(x)}</li>' for x in items)

modules = []
for m in c['temario']:
    rows = []
    for l in m['lecciones']:
        tag = f' <a class="oc-free" href="{PORTAL}?course={c["slug"]}&amp;lesson={l["id"]}">Free preview</a>' if l['gratis'] else ''
        rows.append(f'                        <li><span class="oc-num">{e(l["numero"])}</span> {e(l["titulo"])}{tag}</li>')
    modules.append(f"""                <details class="oc-module"{' open' if m['numero'] == 0 else ''}>
                    <summary><span>Module {m['numero']}</span> {e(m['titulo'])} <small>{len(m['lecciones'])} lessons</small></summary>
                    <ul>
{chr(10).join(rows)}
                    </ul>
                </details>""")

faq = '\n'.join(f"""                <details class="oc-faq">
                    <summary>{e(f['p'])}</summary>
                    <p>{e(f['r'])}</p>
                </details>""" for f in c['faq'])

free_href = FREE.replace('&', '&amp;')
body = f"""
    <!-- Página del curso en línea. Texto tomado del JSON público del portal ({c['clave']}); se regenera si cambia. -->
    <section class="oc-hero">
        <div class="container oc-hero-grid">
            <div>
                <p class="oc-kicker">Online course · {e(c['nivel'])}</p>
                <h1>{e(c['titulo'])}</h1>
                <p class="oc-lead">{e(c['objetivo'])}</p>
                <ul class="oc-chips">
                    <li>{c['total_lecciones']} video lessons</li>
                    <li>Self-paced, on any device</li>
                    <li>Certificate of Completion</li>
                </ul>
                <div class="oc-cta">
                    <a href="{free_href}" class="btn-hero-online">Watch a free lesson</a>
                    <a href="{ENROLL}" class="btn-hero-secondary">Enroll now</a>
                </div>
            </div>
            <a href="{free_href}" class="oc-poster" aria-label="Watch a free lesson">
                <img src="assets/online-course-poster.webp" alt="Lesson 0.1 of Train With a Plan" width="1280" height="720">
                <span class="oc-play"><i class="fa-solid fa-play"></i></span>
            </a>
        </div>
    </section>

    <section class="oc-section">
        <div class="container oc-two">
            <div>
                <h2 class="story-h2">Who this course is for</h2>
                <ul class="oc-list">
{li(c['para_quien'])}
                </ul>
                <p class="oc-note"><strong>Not for:</strong> {e(c['no_es_para'])}</p>
            </div>
            <div>
                <h2 class="story-h2">What you'll learn</h2>
                <ul class="oc-list">
{li(c['aprenderas'])}
                </ul>
            </div>
        </div>
    </section>

    <section class="oc-section oc-alt">
        <div class="container" style="max-width: 860px;">
            <h2 class="story-h2">What's included</h2>
            <ul class="oc-list oc-included">
{li(c['incluye'])}
            </ul>
        </div>
    </section>

    <section class="oc-section">
        <div class="container" style="max-width: 860px;">
            <h2 class="story-h2">Course content</h2>
{chr(10).join(modules)}
        </div>
    </section>

    <section class="oc-section oc-alt">
        <div class="container" style="max-width: 860px;">
            <h2 class="story-h2">Frequently asked questions</h2>
{faq}
            <p class="oc-base">{e(c['base'])}</p>
        </div>
    </section>

    <section class="oc-final">
        <div class="container">
            <h2>Start with the first lesson, free</h2>
            <p>No account needed to watch it.</p>
            <div class="oc-cta" style="justify-content: center;">
                <a href="{free_href}" class="btn-hero-online">Watch a free lesson</a>
                <a href="{ENROLL}" class="btn-hero-secondary">Enroll now</a>
            </div>
        </div>
    </section>

    <style>
        .story-h2 {{ font-family: var(--font-primary); color: var(--color-primary); font-size: 1.5rem; text-transform: uppercase; margin: 0 0 1rem; }}
        .oc-hero {{ padding: 8.5rem 0 4rem; background: var(--color-white); border-bottom: 1px solid #ddd; }}
        .oc-hero-grid {{ display: grid; grid-template-columns: 1.1fr 1fr; gap: 3rem; align-items: center; }}
        .oc-kicker {{ font-family: var(--font-primary); font-weight: 800; text-transform: uppercase; color: var(--color-tertiary, #d10000); letter-spacing: .05em; font-size: .85rem; margin-bottom: .75rem; }}
        .oc-hero h1 {{ font-family: var(--font-primary); color: var(--color-primary); font-size: clamp(1.8rem, 4vw, 2.6rem); line-height: 1.15; margin-bottom: 1rem; }}
        .oc-lead {{ font-size: 1.1rem; line-height: 1.6; color: #444; margin-bottom: 1.25rem; }}
        .oc-chips {{ list-style: none; display: flex; flex-wrap: wrap; gap: .5rem; padding: 0; margin: 0 0 1.75rem; }}
        .oc-chips li {{ background: var(--color-bg-light-blue, #e8eff6); color: var(--color-primary); font-weight: 600; font-size: .9rem; padding: .4rem .8rem; border-radius: 999px; }}
        .oc-cta {{ display: flex; flex-wrap: wrap; gap: .75rem; }}
        .oc-cta a {{ text-align: center; }}
        .oc-poster {{ position: relative; display: block; border-radius: 10px; overflow: hidden; box-shadow: 0 12px 30px rgba(0,0,0,.18); }}
        .oc-poster img {{ display: block; width: 100%; height: auto; }}
        .oc-play {{ position: absolute; inset: 0; margin: auto; width: 72px; height: 72px; border-radius: 50%; background: rgba(253,203,0,.95); color: var(--color-dark); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; transition: transform .2s; }}
        .oc-poster:hover .oc-play {{ transform: scale(1.08); }}
        .oc-section {{ padding: 4rem 0; }}
        .oc-alt {{ background: var(--ici-bg-gray, #f2f5f8); }}
        .oc-two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; }}
        .oc-list {{ list-style: none; padding: 0; margin: 0; }}
        .oc-list li {{ position: relative; padding: .45rem 0 .45rem 1.8rem; line-height: 1.55; color: #333; }}
        .oc-list li::before {{ content: "\\f00c"; font-family: "Font Awesome 6 Free"; font-weight: 900; position: absolute; left: 0; top: .5rem; color: var(--color-primary); }}
        .oc-included {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 2rem; }}
        .oc-note {{ margin-top: 1rem; font-size: .95rem; color: #555; line-height: 1.55; }}
        .oc-module, .oc-faq {{ background: var(--color-white); border: 1px solid #e1e6ec; border-radius: 8px; margin-bottom: .75rem; }}
        .oc-module summary, .oc-faq summary {{ cursor: pointer; padding: 1rem 1.25rem; font-weight: 700; color: var(--color-dark); list-style-position: inside; }}
        .oc-module summary span {{ color: var(--color-primary); font-family: var(--font-primary); text-transform: uppercase; font-size: .85rem; margin-right: .4rem; }}
        .oc-module summary small {{ font-weight: 400; color: #777; margin-left: .4rem; }}
        .oc-module ul {{ list-style: none; margin: 0; padding: 0 1.25rem 1rem; }}
        .oc-module li {{ padding: .45rem 0; border-top: 1px solid #f0f2f5; color: #333; }}
        .oc-num {{ display: inline-block; min-width: 2.4rem; color: #777; font-variant-numeric: tabular-nums; }}
        .oc-free {{ margin-left: .5rem; font-size: .8rem; font-weight: 700; color: var(--color-primary); background: var(--color-secondary); padding: .15rem .55rem; border-radius: 999px; white-space: nowrap; }}
        .oc-faq p {{ padding: 0 1.25rem 1rem; margin: 0; color: #444; line-height: 1.6; }}
        .oc-base {{ margin-top: 1.5rem; font-size: .85rem; color: #666; line-height: 1.55; }}
        .oc-final {{ padding: 4rem 0; background: var(--color-primary); color: var(--color-white); text-align: center; }}
        .oc-final h2 {{ font-family: var(--font-primary); text-transform: uppercase; font-size: 1.8rem; margin-bottom: .5rem; }}
        .oc-final p {{ margin-bottom: 1.5rem; opacity: .9; }}
        @media (max-width: 900px) {{
            .oc-hero {{ padding-top: 7rem; }}
            .oc-hero-grid, .oc-two, .oc-included {{ grid-template-columns: 1fr; }}
            .oc-hero-grid {{ gap: 2rem; }}
        }}
    </style>

"""

out = head + '</head>\n' + tpl[head_end + len('</head>\n'):header_end] + '\n' + body + tpl[footer_start - 4:]
(repo / 'online-course.html').write_text(out, encoding='utf-8', newline='\n')
print('ok', len(out))
