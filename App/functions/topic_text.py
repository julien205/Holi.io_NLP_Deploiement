'''This function will output n topics from a text. The topics are from our model LDA trained on the Microsoft MIND dataset'''

#----------------------The imports--------------------

#------------------------The topics found by the model-----------
list_topics = ['garbage', 'fooding', 'competition', 'people', 'weather', 'entertainment', 'finance', 'household', 'tourism', 'football', 'law', 'environment', 'university sport', 'cooking', 'urbanism', 'Police', 'foreign affairs', 'education', 'consumption', 'nfl', 'motors', 'basketball', 'baseball', 'health', 'US elections']
topics_number =len(list_topics) #Total number of topics in our model 
dict_topics = {i: list_topics[i] for i in range(topics_number)}

#---------------------The model

def topic_text(model, article, n_topics):
    topics = []
    doc = model.id2word.doc2bow(article.split())
    doc_topics, word_topics, phi_values = model.get_document_topics(doc, per_word_topics=True) #Be careful to have a model with per_word_topics = True 
    for idd, prop in sorted(doc_topics,key=lambda x: x[1], reverse=True)[:n_topics+1]: #We sort the list to have the best topics  at the beginning, and add 1 because we handle the topic "11" which is the trash topic
        if idd != 0:
            topics.append(dict_topics[idd])
    if len(topics)>n_topics: topics = topics[:n_topics]  
    return topics