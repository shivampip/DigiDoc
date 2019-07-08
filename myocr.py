import pytesseract


def ocr(img):
    return pytesseract.image_to_string(img)