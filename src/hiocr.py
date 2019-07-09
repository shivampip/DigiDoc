
import os
import sys

if(sys.platform!= 'win32'):
    try:
        from PIL import Image
    except ImportError:
        import Image
    import pytesseract


def ocr(imgname):
    if(sys.platform=='win32'):
        myCmd = os.popen('src\\Tesseract-OCR\\tesseract {} out'.format(imgname)).read()
        outfile= open("out.txt")
        data= outfile.read()
        return data 
    else:
        if(isinstance(imgname, str)):
            text= pytesseract.image_to_string(Image.open(imgname))
        else:
            text= pytesseract.image_to_string(imgname) 
        return text 
