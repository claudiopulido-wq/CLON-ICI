import os
import sys

def compress_images():
    try:
        from PIL import Image
    except ImportError:
        import subprocess
        print("Installing Pillow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image

    assets_dir = "assets"
    
    for filename in os.listdir(assets_dir):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            file_path = os.path.join(assets_dir, filename)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            
            # If greater than 1 MB, compress it
            if size_mb > 1:
                print(f"Compressing {filename} ({size_mb:.2f} MB)...")
                try:
                    img = Image.open(file_path)
                    
                    # Resize if it's super huge
                    max_size = 1920
                    if max(img.width, img.height) > max_size:
                        ratio = max_size / max(img.width, img.height)
                        new_size = (int(img.width * ratio), int(img.height * ratio))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                        
                    # Save back with optimization
                    img.save(file_path, "JPEG", optimize=True, quality=80)
                    new_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                    print(f"-> Reduced to {new_size_mb:.2f} MB.")
                except Exception as e:
                    print(f"Error compressing {filename}: {e}")

if __name__ == "__main__":
    compress_images()
