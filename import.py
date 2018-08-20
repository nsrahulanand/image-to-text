import pytesseract
from PIL import Image

b=Image.open('test.png')
a=pytesseract.image_to_string(b)
print (a)
