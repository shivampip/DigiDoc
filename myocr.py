import os

def ocr(imgname):
    myCmd = os.popen('Tesseract-OCR\\tesseract imgs/{} out'.format(imgname)).read()
    outfile= open("out.txt")
    data= outfile.read()
    return data 