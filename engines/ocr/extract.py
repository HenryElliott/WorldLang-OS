import pytesseract
from PIL import Image
import sys

def extract(image):
    return pytesseract.image_to_string(Image.open(image))

if __name__ == "__main__":
    print(extract(sys.argv[1]))
