import os
import re

STYLE_FILE = "css/style.css"

def update_css():
    with open(STYLE_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Change background of .ask-advisor-section to #f9f9f9 (the gray used in Encuentra tu camino)
    css = re.sub(
        r'\.ask-advisor-section\s*\{[^}]*\}',
        '.ask-advisor-section {\n  display: flex;\n  background-color: #f9f9f9;\n  padding: 4rem 0;\n  min-height: 80vh;\n}',
        css
    )

    # 2. Remove mask from .ask-advisor-image
    css = re.sub(
        r'\.ask-advisor-image\s*\{[^}]*\}',
        '.ask-advisor-image {\n  flex: 1;\n  background-image: url(\'../assets/block2.jpg\');\n  background-size: cover;\n  background-position: center;\n  position: relative;\n}',
        css
    )

    # 3. Make yellow brush translucent
    css = re.sub(
        r'\.ask-advisor-image::before\s*\{[^}]*\}',
        '.ask-advisor-image::before {\n  content: \'\';\n  position: absolute;\n  top: 30%;\n  left: 5%;\n  width: 90%;\n  height: 40%;\n  background: var(--color-secondary);\n  opacity: 0.6;\n  border-radius: 50% 50% 30% 70% / 60% 40% 70% 40%;\n  transform: rotate(-10deg);\n  z-index: 1;\n  mix-blend-mode: multiply;\n}',
        css
    )

    with open(STYLE_FILE, "w", encoding="utf-8") as f:
        f.write(css)

if __name__ == "__main__":
    update_css()
    print("CSS updated successfully.")
