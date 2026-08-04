import os
import sys

def compress_png():
    try:
        from PIL import Image
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image

    file_path = "assets/Block2_final.png"
    webp_path = "assets/Block2_final.webp"
    
    if os.path.exists(file_path):
        print("Compressing Block2_final.png...")
        img = Image.open(file_path)
        
        max_size = 1920
        if max(img.width, img.height) > max_size:
            ratio = max_size / max(img.width, img.height)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            
        img.save(webp_path, "WEBP", optimize=True, quality=80)
        print("Saved as WEBP.")

if __name__ == "__main__":
    compress_png()
