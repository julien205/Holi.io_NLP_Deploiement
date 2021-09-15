from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.patches as patches

mycolors = [color for name, color in mcolors.CSS4_COLORS.items()]

def color_text(model, article):
    doc = model.id2word.doc2bow(article.split())
    doc_topics, word_topics, phi_values = model.get_document_topics(doc, per_word_topics=True) #Be careful to have, when you train tour LDA model, the option per_word_topics=True
    topic_colors = { i : mycolors[i] for i in range(model.num_topics)}
    
    # set up fig to plot
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

    # a sort of hack to make sure the words are well spaced out.
    word_pos = 1/len(doc)

    # use matplotlib to plot words
    for word, topics in word_topics:
        try:
            ax.text(word_pos, 0.8, model.id2word[word],
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20, color=topic_colors[topics[0]],  # choose just the most likely topic
                transform=ax.transAxes)
        except IndexError:
            ax.text(word_pos, 0.8, model.id2word[word],
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20, color='black',  # choose just the most likely topic
                transform=ax.transAxes)
        word_pos += 0.2 # to move the word for the next iter

    ax.set_axis_off()
    plt.show()
    
    return fig