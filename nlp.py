import db
import nltk
nltk.data.path.append("./nltk_data")

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from PyDictionary import PyDictionary
import re


class Nlp(object):
    def __init__(self):
        self.dbclient = db.Ecampusdb()
        self.stop_words = (set(stopwords.words('english')))
        self.dictionary = PyDictionary()
        self.keywords_list = []
        
        
    
    def analyzer(self,question):
        # "How do i view my course on Canvas"
        def is_noun(tag):
            return tag in ['NN', 'NNS', 'NNP', 'NNPS']

        def is_verb(tag):
            return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

        def is_adverb(tag):
            return tag in ['RB', 'RBR', 'RBS']

        def is_adjective(tag):
            return tag in ['JJ', 'JJR', 'JJS']

        def penn_to_wn(tag):
            if is_adjective(tag):
                return wn.ADJ
            elif is_noun(tag):
                return wn.NOUN
            elif is_adverb(tag):
                return wn.ADV
            elif is_verb(tag):
                return wn.VERB
            return wn.NOUN

        tagged_sent = nltk.pos_tag(word_tokenize(question))

        for tag in tagged_sent:
            if tag[0].lower() not in self.stop_words and tag:
                wn_tag = penn_to_wn(tag[1])
                word = WordNetLemmatizer().lemmatize(tag[0],wn_tag)
                self.keywords_list.append(word.lower())
        
        print (self.keywords_list,"elf.keywords_list")

        
        response = self.dbclient.findAll(self.keywords_list)
        return response

        
        
        

#s = Nlp()
#s.analyzer("How do i view my course on Canvas")




