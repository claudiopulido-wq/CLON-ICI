import os
import re

STYLE_FILE = "css/style.css"

def update_css():
    with open(STYLE_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    css = css.replace("url('../assets/block2.jpg')", "url('../assets/Block2_final.webp')")

    with open(STYLE_FILE, "w", encoding="utf-8") as f:
        f.write(css)

if __name__ == "__main__":
    update_css()
    print("CSS updated with new image.")
