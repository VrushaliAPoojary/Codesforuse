from PIL import Image
import numpy as np
import sys
import os

def calculate_brightness(image_path):
    try:
        # Open image (use the function argument, not a hardcoded path)
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"❌ File not found: {image_path}")
        return None
    except Exception as e:
        print(f"❌ Error opening image: {e}")
        return None

    # Convert to NumPy array
    np_img = np.array(img)

    # Separate R, G, B channels
    R = np_img[:, :, 0]
    G = np_img[:, :, 1]
    B = np_img[:, :, 2]

    # Apply brightness formula
    brightness = (0.299 * R + 0.587 * G + 0.114 * B).mean()
    return brightness


if __name__ == "__main__":
    # Allow passing image path as argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # fallback hardcoded path (keep it in quotes!)
        path = r"E:\4SN22AI062VAP\codetrials\PrathamOfficial.png"

    if os.path.exists(path):
        value = calculate_brightness(path)
        if value is not None:
            print(f"✅ Brightness of '{path}': {value:.2f}")
    else:
        print(f"⚠️ Please provide a valid image path.")
