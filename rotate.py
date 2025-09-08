import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

def rotate_image(input_path, direction, times):
    img = Image.open(input_path)
    angle = 90 * times if direction == "right" else -90 * times
    rotated = img.rotate(angle, expand=True)
    
    output_path = f"rotated_{os.path.basename(input_path)}"
    rotated.save(output_path)
    print(f"✅ Rotated image saved as {output_path}")


def rotate_pdf(input_path, direction, times):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    rotation = 90 * times if direction == "right" else -90 * times

    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)

    output_path = f"rotated_{os.path.basename(input_path)}"
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✅ Rotated PDF saved as {output_path}")


def main():
    file_path = input("Enter the file path (image or pdf): ").strip()
    direction = input("Rotate 'left' or 'right'? ").strip().lower()
    times = int(input("How many times to rotate (each = 90°)? ").strip())

    if not os.path.exists(file_path):
        print("❌ File not found!")
        return

    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        rotate_image(file_path, direction, times)
    elif ext == ".pdf":
        rotate_pdf(file_path, direction, times)
    else:
        print("❌ Unsupported file type. Use image or PDF.")


if __name__ == "__main__":
    main()
