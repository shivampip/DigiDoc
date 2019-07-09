from .hiocr import ocr 
from .summarizer import get_keywords, get_summary
from markdown2 import Markdown

md= Markdown()

def addbr(text):
    text= text.replace("\n", "<br>")
    return text 


def process(file_path):
    out= {}

    text= ocr(file_path)
    out['text']= addbr(text)

    out['summary']= get_summary(text)

    out['keywords']= get_keywords(text)
    
    out['img']= file_path

    return out
