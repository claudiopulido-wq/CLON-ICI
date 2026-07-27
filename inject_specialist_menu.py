import glob
import os

path = r"c:\Users\ASUS\Desktop\Antigravity\gesacademico-edu-mx\ici-certificaciones-web\*.html"

target = '<li class="dropdown"><a href="#">Conviértete en Especialista</a></li>'

replacement = """                <li class="dropdown">
                    <a href="#">Conviértete en Especialista</a>
                    <div class="mega-menu split-mega-menu">
                        <!-- Left Side -->
                        <div class="mega-left">
                            <h4 class="mega-title"><i class="fa-solid fa-star"></i> Especializaciones Top</h4>
                            
                            <a href="especialista-en-gluteos.html" class="path-card">
                                <span class="badge-small badge-blue"><i class="fa-solid fa-fire"></i> Tendencia</span>
                                <h5>Especialista en Glúteos</h5>
                                <p>Domina el entrenamiento y programación para glúteos</p>
                                <i class="fa-solid fa-arrow-right path-arrow"></i>
                            </a>

                            <a href="especialista-en-fuerza.html" class="path-card">
                                <span class="badge-small badge-yellow"><i class="fa-solid fa-dumbbell"></i> Avanzado</span>
                                <h5>Fuerza y Acondicionamiento</h5>
                                <p>Entrena atletas y mejora el rendimiento deportivo</p>
                                <i class="fa-solid fa-arrow-right path-arrow"></i>
                            </a>
                        </div>
                        
                        <!-- Right Side -->
                        <div class="mega-right">
                            <div class="mega-right-header">
                                <h4>Especializaciones</h4>
                                <a href="#" class="view-all">Ver todas las Especializaciones <i class="fa-solid fa-chevron-right"></i></a>
                            </div>
                            
                            <div class="mega-categories">
                                <div class="mega-column">
                                    <h4><i class="fa-solid fa-person-running"></i> Rendimiento y Fuerza</h4>
                                    <a href="especialista-en-gluteos.html">Especialista en Glúteos</a>
                                    <a href="especialista-en-fuerza.html">Fuerza y Acondicionamiento</a>
                                    <a href="#">Especialista en Fisicoculturismo</a>
                                    <a href="#">Entrenamiento Táctico</a>
                                </div>
                                <div class="mega-column">
                                    <h4><i class="fa-solid fa-heart-pulse"></i> Poblaciones Especiales</h4>
                                    <a href="especialista-en-ejercicio-correctivo.html">Ejercicio Correctivo</a>
                                    <a href="#">Fitness para Adultos Mayores</a>
                                    <a href="#">Entrenamiento Pre/Postnatal</a>
                                    <a href="#">Fitness Juvenil</a>
                                </div>
                                <div class="mega-column">
                                    <h4><i class="fa-solid fa-laptop-code"></i> Negocio y Nicho</h4>
                                    <a href="coach-en-linea.html">Coach en Línea (Online Coaching)</a>
                                    <a href="#">Especialista en Transformación</a>
                                    <a href="#">Instructor de Clases Grupales</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>"""

for file in glob.glob(path):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content and "Especializaciones Top" not in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file)}")
