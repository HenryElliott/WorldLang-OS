import pytesseract
from PIL import Image
import sys

def extract_text(image_path):
    print(f"📸 Processing image: {image_path}")
    text = pytesseract.image_to_string(Image.open(image_path))
    print("📝 Extracted Text:\n", text.strip())
    return text.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract.py <image_file>")
    else:
        extract_text(sys.argv[1])
