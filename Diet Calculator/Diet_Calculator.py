import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r"C:\Users\jboob\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open("pork.png")
text = tess.image_to_string(img)

print(text)
