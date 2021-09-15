'''This function will output 2 topics from a text. The topics are from our model LDA trained on the Microsoft MIND dataset'''

#----------------------The imports--------------------
#!pip install gensim -q

# Gensim
import gensim
#------------------------

def topic_text(model,article):
    topics = []
    doc = model.id2word.doc2bow(article.split())
    doc_topics, word_topics, phi_values = model.get_document_topics(doc, per_word_topics=True) #Be careful to have a model with per_word_topics = True 
    for idd, prop in doc_topics:
        topics.append(model.show_topic(idd)[0][0])
    return topics
    