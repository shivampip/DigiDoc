from .hiocr import ocr 
from .summarizer import get_keywords, get_summary
from markdown2 import Markdown

md= Markdown()

def addbr(text):
    text= text.replace("\n", "<br>")
    return text 


def process(file_path):
    out= ""

    text= ocr(file_path)
    out+= "## Extracted Text\n"
    out+= addbr(text)+"\n"

    out+= "## Summary\n"
    out+= get_summary(text)+"\n"

    out+= "## Keywords\n"
    for word in get_keywords(text).split(" "):
        out+= "* "+word+"\n"
    out+= " :smile: "

    out= md.convert(out) 
    return "<center>"+out+"</center>"
