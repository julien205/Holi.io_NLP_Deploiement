mycolors = ['#FF0000', '#dde031', '#892ed9', '#0ff1ce', '#ff7518', '#ff6699']

def color_text(model, article, n_topics):
    doc = model.id2word.doc2bow(article.split())
    doc_topics, word_topics, phi_values = model.get_document_topics(doc, per_word_topics=True) #Be careful to have, when you train tour LDA model, the option per_word_topics=True
    topics_used = sorted(doc_topics,key=lambda x: x[1], reverse=True)[:n_topics]
    topic_colors = { topics_used[i][0] : mycolors[i] for i in range(n_topics)}
    text=""
    for word, topics in word_topics:
        try:
            text+="<font color=\"" + topic_colors[topics[0]] + "\">" + model.id2word[word] + ' ' + "</font>"
        except: 
            text+="<font color=\"#ffffff\">" + model.id2word[word] + ' ' + "</font>" #If the word does not have topics affiliated, we print it white  
    return text