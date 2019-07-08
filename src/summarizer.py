from gensim.summarization import summarize, keywords

def get_summary(text):
    # summarize(text, word_count=50)
    # summarize(text, ratio=0.5)
    return summarize(text) 

def get_keywords(text):
    return keywords(text)