from PIL import Image, ImageOps
import numpy as np
import os

# Input path
INPUT_PATH = r"E:\4SN22AI062VAP\codetrials\preethi.jpg"

# Standard passport photo size (in pixels, 300 DPI)
WIDTH, HEIGHT = 413, 531

def get_dominant_background_color(img, border=10):
    """
    Detects the dominant background color by sampling pixels near the border.
    """
    img_np = np.array(img)
    
    # Sample pixels from all 4 sides
    top = img_np[:border, :, :]
    bottom = img_np[-border:, :, :]
    left = img_np[:, :border, :]
    right = img_np[:, -border:, :]
    
    border_pixels = np.concatenate([top.reshape(-1,3),
                                    bottom.reshape(-1,3),
                                    left.reshape(-1,3),
                                    right.reshape(-1,3)], axis=0)
    
    # Calculate mean color
    dominant_color = tuple(np.mean(border_pixels, axis=0).astype(int))
    return dominant_color

def create_passport_photo(input_path):
    img = Image.open(input_path).convert("RGB")

    # Detect background color
    bg_color = get_dominant_background_color(img)

    # Resize and fit image
    img_resized = ImageOps.fit(img, (WIDTH, HEIGHT), method=Image.LANCZOS, centering=(0.5, 0.5))
    background = Image.new("RGB", (WIDTH, HEIGHT), bg_color)
    background.paste(img_resized, (0, 0))
    
    # Generate output filename (A4-<original_name>.jpg)
    folder, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"passport-{name}.jpg"
    output_path = os.path.join(folder, output_filename)

    # Save result
    background.save(output_path, quality=95, dpi=(300,300))
    print(f"✅ Passport photo saved at: {output_path}")

if __name__ == "__main__":
    create_passport_photo(INPUT_PATH)
