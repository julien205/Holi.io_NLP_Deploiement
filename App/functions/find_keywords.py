#We use a algotihm suggested by Maarten Grootendorst, creator of KeyBert()

#In this file we define a function that returns keywords when given a text

#We import the needed libraries

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import itertools
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words= set(stopwords.words('english'))


# We begin with a function using Max Sum Similarity in order to diversify our keywords
def max_sum_sim(doc_embedding, candidate_embeddings, candidates, top_n, nr_candidates): # nr_candidates = diversification, high nr -> high diversification
    # Calculate distances and extract keywords
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    distances_candidates = cosine_similarity(candidate_embeddings, 
                                            candidate_embeddings)

    # Get top_n words as candidates based on cosine similarity
    words_idx = list(distances.argsort()[0][-nr_candidates:])
    words_vals = [candidates[index] for index in words_idx]
    distances_candidates = distances_candidates[np.ix_(words_idx, words_idx)]

    # Calculate the combination of words that are the least similar to each other
    min_sim = np.inf
    candidate = None
    for combination in itertools.combinations(range(len(words_idx)), top_n):
        sim = sum([distances_candidates[i][j] for i in combination for j in combination if i != j])
        if sim < min_sim:
            candidate = combination
            min_sim = sim

    return [words_vals[idx] for idx in candidate]

# The function that will find the keywords
def find_keywords(doc, n_length, top_n=5): # n_length the number of keywords in my keyphrases, top_n the number of keyphrases I want
    n_gram_range = (n_length, n_length) # number of keywords wanted, write (2,2) if you want a keyphrase with two keywords
    # Extract candidate words/phrases
    count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
    candidates = count.get_feature_names()
    model = SentenceTransformer('distilbert-base-nli-mean-tokens') # Look at hugging face to go further : https://huggingface.co/sentence-transformers/bert-base-nli-mean-tokens
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)
    keywords = max_sum_sim(doc_embedding, candidate_embeddings, candidates, top_n, 10)
    return keywords