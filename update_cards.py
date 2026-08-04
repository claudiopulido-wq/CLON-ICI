import os

INDEX_FILE = "index.html"

def update_cards():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # --- CARD 1 ---
    # Delete rating
    html = html.replace('<p class="card-rating"><i class="fa-solid fa-star"></i> 4.9 (2,145 Reseñas)</p>\n', '')
    html = html.replace('<p class="card-rating"><i class="fa-solid fa-star"></i> 4.9 (2,145 Reseñas)</p>', '')
    
    html = html.replace('<span class="card-badge">Más Popular</span>', '<span class="card-badge">⭐ Most Popular</span>')
    html = html.replace('<h3>Entrenador Personal Certificado</h3>', '<h3>Individual Certifications</h3>')
    html = html.replace(
        '<p class="card-desc">Conviértete en un experto en fitness y comienza a entrenar clientes en el gimnasio o en línea de inmediato.</p>',
        '<p class="card-desc">Become certified in Sculpt & Burn, Barre, or Mat Pilates through our in-person certification programs. View the details of our upcoming edition, including the date, city, venue, and schedule, and choose the discipline that best supports your professional goals.</p>'
    )
    html = html.replace('<span class="price-monthly">$83.25/mes</span>', '<span class="price-monthly">$850 USD One-Time Payment</span>')
    html = html.replace('<span class="price-full">o $999 pago único</span>', '<span class="price-full">$300 USD Enrollment Fee (credited toward the total tuition).</span>')


    # --- CARD 2 ---
    # Delete rating
    html = html.replace('<p class="card-rating"><i class="fa-solid fa-star"></i> 5.0 (4,890 Reseñas)</p>\n', '')
    html = html.replace('<p class="card-rating"><i class="fa-solid fa-star"></i> 5.0 (4,890 Reseñas)</p>', '')
    
    html = html.replace('<span class="card-badge badge-red">Mejor Valor</span>', '<span class="card-badge badge-red">⭐ Best Value</span>')
    html = html.replace('<h3 style="color:var(--color-dark);">Paquete Entrenador Élite</h3>', '<h3 style="color:var(--color-dark);">Movement Coach Package</h3>')
    html = html.replace(
        '<p class="card-desc">Nuestra oferta más completa. Incluye Entrenador Personal, Nutrición y 4 especializaciones a tu elección.</p>',
        '<p class="card-desc">Earn your Sculpt & Burn, Barre, and Mat Pilates Certifications with one enrollment and save 40% compared to purchasing each certification separately. Explore the details of our upcoming certification edition, including the date, city, venue, and schedule.</p>'
    )
    html = html.replace('<span class="price-monthly">$139.00/mes</span>', '<span class="price-monthly">$1,500 USD One-Time Payment</span>')
    html = html.replace('<span class="price-full">o $1,668 pago único</span>', '<span class="price-full">$300 USD Enrollment Fee (credited toward the total tuition).</span>')
    html = html.replace(
        '<a href="#" class="btn-card" style="background-color: var(--color-primary); color: var(--color-dark); border-color: var(--color-primary);">Ahorra $150 Hoy</a>',
        '<a href="#" class="btn-card" style="background-color: var(--color-primary); color: var(--color-white); border-color: var(--color-primary);">View Next Edition</a>'
    )

    # --- CARD 3 ---
    # Delete rating
    html = html.replace('<p class="card-rating"><i class="fa-solid fa-star"></i> 4.8 (1,340 Reseñas)</p>\n', '')
    html = html.replace('<p class="card-rating"><i class="fa-solid fa-star"></i> 4.8 (1,340 Reseñas)</p>', '')
    
    html = html.replace('<span class="card-badge badge-blue">Tendencia</span>', '<span class="card-badge badge-blue">⭐ For Experienced Coaches</span>')
    html = html.replace('<h3>Coach de Nutrición Certificado</h3>', '<h3>Competency Assessments</h3>')
    html = html.replace(
        '<p class="card-desc">Ayuda a tus clientes a alcanzar sus objetivos dominando la ciencia de la nutrición y el coaching de hábitos.</p>',
        '<p class="card-desc">Designed for experienced coaches, this distance-based assessment pathway allows you to validate your professional knowledge and skills without attending the in-person certification edition. Complete the entire assessment remotely through required documentation and formal evaluations.</p>'
    )
    html = html.replace('<span class="price-monthly">$66.58/mes</span>', '<span class="price-monthly">$200 USD Per Discipline</span>')
    html = html.replace('<span class="price-full">o $799 pago único</span>', '<span class="price-full">$600 USD for all three disciplines.</span>')

    # Since button texts for Card 1 and 3 are the same ("Inscríbete Ahora"), we can just replace the first one with "View Next Edition" 
    # and the second one with "Start Your Assessment".
    html = html.replace('>Inscríbete Ahora<', '>View Next Edition<', 1)
    html = html.replace('>Inscríbete Ahora<', '>Start Your Assessment<', 1)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    update_cards()
    print("Cards updated successfully.")
