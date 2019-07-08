from .hiocr import ocr 
from .summarizer import get_keywords, get_summary

def addbr(text):
    text= text.replace("\n", "<br>")
    return text 


def process(file_path):
    out= ""

    text= ocr(file_path)
    out+= "<h3>Extracted Text</h3>"
    out+= addbr(text)

    out+= "<h3>Summary</h3>"
    out+= get_summary(text)

    out+= "<h3>Keywords</h3>"
    out+= get_keywords(text)

    return out
