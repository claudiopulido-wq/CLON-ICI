import re

INDEX_FILE = "index.html"
STYLE_FILE = "css/style.css"

# 1. Update index.html
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Change promo banner text and color
html = re.sub(
    r'<div class="promo-banner-top" style="background-color: var\(--color-primary\);(.*?)>.*?</div>',
    r'<div class="promo-banner-top" style="background-color: var(--color-secondary);\1>\n        Save 40% with the Movement Coach Package and earn all three certifications with one payment.\n    </div>',
    html,
    flags=re.DOTALL
)

# Change hero text
html = html.replace(
    '<h1>CONVIÉRTETE EN ENTRENADOR PERSONAL <span>CERTIFICADO</span></h1>',
    '<h1><span style="color: var(--color-primary);">STEP INTO COACHING</span><br><span style="color: var(--color-white); font-size: 0.6em; font-weight: normal; text-transform: none; line-height: 1.3; display: inline-block; margin-top: 10px;">Certification with official and international endorsement.</span></h1>'
)

# Change hero description
old_desc = '<p>Únete a más de 500,000 profesionales del fitness en todo el mundo. Estudia a tu propio ritmo, aprueba el examen en línea y comienza tu carrera con nuestra garantía de empleo.</p>'
new_desc = '<p style="color: var(--color-dark); font-weight: 500;">Join a global community of over 70,000 certified professionals. Our certifications are officially recognized and internationally valid through the appropriate governing authority. Stay updated on our in-person certification editions, offered on select dates in cities across the United States.<br><br>Already an experienced coach? Our distance-based Competency Assessments Certifications allow you to validate your knowledge and skills through formal evaluations and documentation.</p>'
html = html.replace(old_desc, new_desc)

# Change hero image
html = html.replace(
    '<div class="hero-image-bg" style="background-image: url(\'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1200&q=80\');"></div>',
    '<div class="hero-image-bg" style="background-image: url(\'assets/portada_1.jpg\');"></div>'
)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update style.css
with open(STYLE_FILE, "r", encoding="utf-8") as f:
    css = f.read()

# Change hero gradient
css = css.replace(
    'background: linear-gradient(to right, #fff 0%, transparent 100%);',
    'background: linear-gradient(to right, var(--color-secondary) 0%, transparent 100%);'
)

# Media query gradient
css = css.replace(
    'linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9))',
    'linear-gradient(rgba(253, 203, 0, 0.9), rgba(253, 203, 0, 0.9))' # Yellow with opacity
)

# Also ensure .hero-issa has yellow background if the image doesn't cover
css = css.replace(
    '.hero-issa {\n  position: relative;\n  min-height: 85vh;\n  display: flex;\n  align-items: center;\n  background-color: var(--color-white);\n}',
    '.hero-issa {\n  position: relative;\n  min-height: 85vh;\n  display: flex;\n  align-items: center;\n  background-color: var(--color-secondary);\n}'
)

with open(STYLE_FILE, "w", encoding="utf-8") as f:
    f.write(css)

print("Modifications applied successfully.")
