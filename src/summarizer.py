from gensim.summarization import summarize, keywords

def get_summary(text):
    # summarize(text, word_count=50)
    # summarize(text, ratio=0.5)
    return summarize(text) 

def get_keywords(text):
    return keywords(text).split("\n")


'''
text= """
Historians consider India's modern age to have begun sometime between 1848 and 1885. The appointment in 1848 of Lord Dalhousie as Governor General of the East India Company set the stage for changes essential to a modern state. These included the consolidation and demarcation of sovereignty, the surveillance of the population, and the education of citizens. Technological changes—among them, railways, canals, and the telegraph—were introduced not long after their introduction in Europe.[87][88][89][90] However, disaffection with the company also grew during this time, and set off the Indian Rebellion of 1857. Fed by diverse resentments and perceptions, including invasive British-style social reforms, harsh land taxes, and summary treatment of some rich landowners and princes, the rebellion rocked many regions of northern and central India and shook the foundations of Company rule.[91][92] Although the rebellion was suppressed by 1858, it led to the dissolution of the East India Company and the direct administration of India by the British government. Proclaiming a unitary state and a gradual but limited British-style parliamentary system, the new rulers also protected princes and landed gentry as a feudal safeguard against future unrest.[93][94] In the decades following, public life gradually emerged all over India, leading eventually to the founding of the Indian National Congress in 1885.
"""

keywords= get_keywords(text)
print("Len of text: {}".format(len(text)))
print("Len of keywords: {}".format(len(keywords)))
print("Type: {}".format(type(keywords)))

print(keywords)
'''