from .hiocr import ocr, ocrpdf
from .summarizer import get_keywords, get_summary
from markdown2 import Markdown
from .myscanner import Scanner

md= Markdown()

def addbr(text):
    text= text.replace("\n", "<br>")
    return text 


def imgprocess(file_path):
    sc= Scanner(file_path)
    edged, image= sc.preprocess()
    contours= sc.get_contours(edged)
    target= sc.get_best(contours)
    outline= sc.draw_contours(image, target)
    outline_path= sc.save(outline, "_outline")

    out= sc.transform(image, target)
    out_path= sc.save(out, "_out")
    return outline_path, out_path

def textprocess(file_path):
    out= {}

    text= ocr(file_path)
    out['file_path']= file_path
    out['html']= addbr(text)
    out['text']= text 

    out['summary']= get_summary(text)

    keywords= get_keywords(text)
    out['keywords_len']= len(keywords)
    out['keywords']= keywords
    
    out['img']= file_path

    return out

def process(file_path):
    outline, out= imgprocess(file_path)
    output = textprocess(out)
    output['outline_path']= outline
    output['out_path']= out 
    return output


def get_pdf(file_path):
    return ocrpdf(file_path)