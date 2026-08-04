import os
import re

CSS_FILE = r"c:\Users\ASUS\Desktop\Antigravity\gesacademico-edu-mx\ici-certificaciones-web\css\style.css"
HTML_DIR = r"c:\Users\ASUS\Desktop\Antigravity\gesacademico-edu-mx\ici-certificaciones-web"

def update_css():
    with open(CSS_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Update root variables
    old_root = r":root \{.*?\}"
    new_root = """:root {
  /* Colores Principales */
  --color-primary: #0651a3;
  --color-secondary: #fdcb00;
  --color-tertiary: #d10000;
  --color-white: #ffffff;
  
  /* Colores Extendidos y de UI */
  --color-dark: #1a1a1a;
  --color-light: #f4f4f4;
  --color-bg-gray: #f2f5f8;
  --color-bg-light-blue: #e8eff6;
  
  /* Tipografía */
  --font-primary: 'Montserrat', sans-serif;
  --font-secondary: 'Outfit', sans-serif;
}"""
    css = re.sub(old_root, new_root, css, flags=re.DOTALL)

    # 2. Map old variables to new variables
    var_map = {
        "var(--ici-yellow)": "var(--color-primary)",
        "var(--ici-blue)": "var(--color-secondary)",
        "var(--ici-red)": "var(--color-tertiary)",
        "var(--ici-white)": "var(--color-white)",
        "var(--ici-text-dark)": "var(--color-dark)",
        "var(--ici-text-light)": "var(--color-light)",
        "var(--ici-bg-gray)": "var(--color-bg-gray)",
        "var(--ici-bg-light-blue)": "var(--color-bg-light-blue)"
    }
    for old, new in var_map.items():
        css = css.replace(old, new)

    # 3. Specific dark-to-light theme changes
    # .hero-issa
    css = css.replace("background-color: #000;", "background-color: var(--color-white);")
    css = css.replace("linear-gradient(to right, #000 0%, transparent 100%)", "linear-gradient(to right, #fff 0%, transparent 100%)")
    
    # Hero text colors
    css = css.replace(".hero-text-box h1 {\n  font-size: 4rem;\n  color: var(--color-white);", ".hero-text-box h1 {\n  font-size: 4rem;\n  color: var(--color-dark);")
    css = css.replace(".hero-text-box p {\n  font-size: 1.25rem;\n  color: #ccc;", ".hero-text-box p {\n  font-size: 1.25rem;\n  color: #555;")
    css = css.replace(".hero-trust span {\n  color: #fff;", ".hero-trust span {\n  color: #555;")
    
    # Top bar
    css = css.replace(".top-bar {\n  background-color: var(--color-dark);\n  color: var(--color-white);", ".top-bar {\n  background-color: var(--color-white);\n  color: var(--color-dark);\n  border-bottom: 1px solid #ddd;")
    css = css.replace(".top-bar a {\n  color: #ccc;", ".top-bar a {\n  color: #555;")
    css = css.replace(".top-bar a:hover {\n  color: var(--color-white);", ".top-bar a:hover {\n  color: var(--color-primary);")
    
    # Guarantee section (was --ici-blue)
    # the mapping already made it var(--color-secondary) which is yellow. Let's make it white.
    css = css.replace(".guarantee-section {\n  background-color: var(--color-secondary);\n  color: var(--color-white);", ".guarantee-section {\n  background-color: var(--color-white);\n  color: var(--color-dark);\n  border-top: 1px solid #ddd;")
    css = css.replace(".guarantee-icon {\n  font-size: 8rem;\n  color: rgba(255,255,255,0.1);", ".guarantee-icon {\n  font-size: 8rem;\n  color: rgba(0,0,0,0.05);")
    
    # Footer
    css = css.replace("footer {\n  background-color: var(--color-dark);\n  color: var(--color-light);", "footer {\n  background-color: var(--color-white);\n  color: var(--color-dark);\n  border-top: 1px solid #ddd;")
    css = css.replace(".footer-brand p {\n  font-size: 0.9rem;\n  color: #ccc;", ".footer-brand p {\n  font-size: 0.9rem;\n  color: #555;")
    css = css.replace(".social-icons a {\n  color: var(--color-white);", ".social-icons a {\n  color: var(--color-dark);\n  background-color: var(--color-bg-gray);")
    css = css.replace(".link-group h4 {\n  color: var(--color-white);", ".link-group h4 {\n  color: var(--color-dark);")
    css = css.replace(".link-group ul a {\n  color: #ccc;", ".link-group ul a {\n  color: #555;")
    
    # Media query for hero
    css = css.replace("linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7))", "linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9))")
    
    # Also fix guarantee text h2 that might have been mapped to primary
    # ".guarantee-text h2 {\n  font-size: 2.5rem;\n  color: var(--color-primary);" (no change needed)

    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(css)

def update_html_files():
    # Replace inline styles in html files
    var_map = {
        "var(--ici-yellow)": "var(--color-primary)",
        "var(--ici-blue)": "var(--color-secondary)",
        "var(--ici-red)": "var(--color-tertiary)",
        "var(--ici-white)": "var(--color-white)",
        "var(--ici-text-dark)": "var(--color-dark)",
    }
    
    html_files = [f for f in os.listdir(HTML_DIR) if f.endswith(".html")]
    for hf in html_files:
        hf_path = os.path.join(HTML_DIR, hf)
        with open(hf_path, "r", encoding="utf-8") as f:
            html = f.read()
            
        for old, new in var_map.items():
            html = html.replace(old, new)
            
        # specifically for inline dark backgrounds
        html = html.replace('background-color: #111;', 'background-color: var(--color-white); border-bottom: 1px solid #ddd;')
        html = html.replace('background-color: #000;', 'background-color: var(--color-white);')
        html = html.replace('color: #fff;', 'color: var(--color-dark);')
        html = html.replace('color: #ccc;', 'color: #555;')
        
        # fix the promo banner which says "background: #000; color: #fff;"
        html = html.replace('background: #000; color: var(--color-dark);', 'background: var(--color-bg-gray); color: var(--color-dark);')
        
        with open(hf_path, "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    update_css()
    update_html_files()
    print("Update complete")
