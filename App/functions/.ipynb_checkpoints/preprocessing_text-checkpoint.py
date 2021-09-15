'''This function will have as input a text and will give as output a preprocessized text, for instance without URL, without stop words, etc...'''

#------------------The imports-------------------
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
#!spacy download en_core_web_sm -q
import en_core_web_sm



# First we use the cleaning function

def clean (article):
    
  # Deletes urls
  article = re.sub(r"https:[A-Za-z0-9]+", "", article)
  article = re.sub(r"http:[A-Za-z0-9]+", "", article)
  article = re.sub(r"www\.[A-Za-z0-9]+", "", article)
  
  # We force the utf-8 encoding
  article.encode("utf-8").decode("utf-8")
  
  # We delete the \r and the \n
  article = re.sub(r"\\r|\\n", "", article)
  
  #We delete the 's
  article = re.sub(r"'s", "", article)
  
  # We delete everything that is not alphabetic
  pattern = re.compile(r'[^a-zA-Z]+')
  article = pattern.sub(' ', article)
  
  # Transform multiples spaces in one space
  article = re.sub(r"\s{2,}", " ", article)

  # strip 
  article = article.strip()

  return article


#-------------------------------------- Words to replace or delete, based on observations
to_replace={
    'sen':'senate',
    'senator':'senate',
    'teacher':'teaching'
}
add_stop_words={'tonight',
                'yes',
                'no',
                'hey',
                'okay',
                'etc',
                'mr',
                'mss',
                'ms',
                'er',
                'v',
                'monthly',
                'tb',
                'sec',
                'mind'}
STOP_WORDS |= add_stop_words

# Then we create a function to transform the text_cleaned to have a text nlp_ready
def text_to_nlp_ready (article):
    nlp = en_core_web_sm.load()
    excluded_tags = {"ADV", "ADP", "AUX", "NUM"}
    article_tokenized = [ token.lemma_ for token in nlp(article) if (token.pos_ not in excluded_tags) & (token.lemma_.lower() not in STOP_WORDS) & (len(token.lemma_) >1) ]
    article_nlp_ready = ' '.join(article_tokenized).lower()
    
    return article_nlp_ready

#The funciton that will and Clean And create a text NLP ready
def preprocess_text(article):
    return text_to_nlp_ready((clean(article)))