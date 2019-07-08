'''
import os

def ocr(imgname):
    myCmd = os.popen('Tesseract-OCR\\tesseract imgs/{} out'.format(imgname)).read()
    outfile= open("out.txt")
    data= outfile.read()
    return data 
'''


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract




def ocr(img):
    if(isinstance(img, str)):
        text= pytesseract.image_to_string(Image.open(img))
    else:
        text= pytesseract.image_to_string(img) 
    return text 