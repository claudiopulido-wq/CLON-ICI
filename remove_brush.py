import os
import re

STYLE_FILE = "css/style.css"

def update_css():
    with open(STYLE_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    # Remove the yellow brush pseudo-element block
    css = re.sub(
        r'\.ask-advisor-image::before\s*\{[^}]*\}',
        '',
        css
    )

    with open(STYLE_FILE, "w", encoding="utf-8") as f:
        f.write(css)

if __name__ == "__main__":
    update_css()
    print("CSS brush strokes removed.")
