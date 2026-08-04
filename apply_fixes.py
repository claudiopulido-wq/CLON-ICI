import os

INDEX_FILE = "index.html"
STYLE_FILE = "css/style.css"

def update_css():
    with open(STYLE_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    # Increase container max-width to reduce left margin on large screens
    css = css.replace("max-width: 1280px;", "max-width: 1400px;")
    
    # Reduce hero text box width so it doesn't go too far into the image
    css = css.replace(
        ".hero-text-box {\n  width: 55%;\n  padding-right: 3rem;\n}",
        ".hero-text-box {\n  width: 45%;\n  padding-right: 2rem;\n}"
    )

    # Boton "comienza hoy mismo" -> "In-Person Certifications"
    css = css.replace(
        ".btn-hero-primary {\n  background-color: var(--color-primary);\n  color: var(--color-dark);",
        ".btn-hero-primary {\n  background-color: var(--color-white);\n  color: #000;"
    )
    # the hover for primary:
    css = css.replace(
        ".btn-hero-primary:hover {\n  background-color: var(--color-white);\n}",
        ".btn-hero-primary:hover {\n  background-color: #f0f0f0;\n}"
    )

    # Boton "compara programas" -> "Competency Assessments"
    css = css.replace(
        ".btn-hero-secondary {\n  border: 2px solid var(--color-white);\n  color: var(--color-white);",
        ".btn-hero-secondary {\n  border: 2px solid var(--color-primary);\n  background-color: var(--color-primary);\n  color: var(--color-white);"
    )
    # hover for secondary:
    css = css.replace(
        ".btn-hero-secondary:hover {\n  background-color: var(--color-white);\n  color: var(--color-dark);\n}",
        ".btn-hero-secondary:hover {\n  background-color: #054082;\n  border-color: #054082;\n  color: var(--color-white);\n}"
    )

    with open(STYLE_FILE, "w", encoding="utf-8") as f:
        f.write(css)

def update_html():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Badge text color -> white.
    html = html.replace(
        '<div class="badge">NUEVO: Coach de Salud Aprobado por NBHWC</div>',
        '<div class="badge" style="background-color: var(--color-primary); color: var(--color-white);">NUEVO: Coach de Salud Aprobado por NBHWC</div>'
    )

    # Buttons
    html = html.replace(">Comienza Hoy Mismo<", ">In-Person Certifications<")
    html = html.replace(">Compara Programas<", ">Competency Assessments<")

    # Why choose us section titles
    html = html.replace("<h2>Por qué funciona <span>ICI</span></h2>", "<h2>Certify Your Future:</h2>")
    
    html = html.replace(
        "<p>Tu compra está respaldada por nuestra garantía de empleo con devolución del 100% del dinero. Consigue un puesto después de certificarte o tu matrícula corre por nuestra cuenta.</p>",
        "<p>More than a certification, ICI is a pathway to professional success. From internationally recognized credentials to career opportunities and ongoing support, we are committed to helping you build a successful future in the fitness industry.</p>"
    )

    # Grid features
    # Feature 1
    html = html.replace("<h3>Estudia en Cualquier Lugar</h3>", "<h3>Official & International Endorsement</h3>")
    html = html.replace("<p>Nuestros programas son 100% en línea. Estudia a tu propio ritmo desde tu computadora, tableta o teléfono inteligente.</p>", "<p>Earn credentials with official and international recognition through the appropriate governing authority, giving your certification credibility and value wherever your career takes you.</p>")

    # Feature 2
    html = html.replace("<h3>Exámenes a Libro Abierto</h3>", "<h3>97% Career Success Rate</h3>")
    html = html.replace("<p>Creemos en el aprendizaje del mundo real. Toma tus exámenes a tu propio ritmo, a libro abierto y sin estrés.</p>", "<p>97% of our graduates successfully launch their careers by securing employment or building their own fitness business after completing their certification.</p>")

    # Feature 3
    html = html.replace("<h3>Garantía de Empleo</h3>", "<h3>Career Opportunities</h3>")
    html = html.replace("<p>Te garantizamos que encontrarás trabajo dentro de los 6 meses posteriores a tu certificación, o te devolvemos tu dinero.</p>", "<p>Through our partnerships with studios and fitness centers across the United States and Mexico, we help connect our graduates with real employment opportunities.</p>")

    # Feature 4
    html = html.replace("<h3>Soporte Ilimitado</h3>", "<h3>Beyond Certification</h3>")
    html = html.replace("<p>Accede a nuestro equipo de tutores y expertos en éxito estudiantil siempre que necesites ayuda con el material.</p>", "<p>Our support continues after graduation. Whether you're looking for your first coaching position or planning to open your own studio, ICI provides guidance to help you achieve your professional goals.</p>")

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    update_css()
    update_html()
    print("Fixes applied successfully.")
