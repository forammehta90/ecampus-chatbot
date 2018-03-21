import db
import nltk
nltk.data.path.append("./nltk_data")

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
        tagged_sent = pos_tag(question.split())
        tokenizer = []
        mongo_dict ={}
        for word in question.split():
            if word.lower() not in self.stop_words:
                self.keywords_list.append(word.lower())
        
        print (self.keywords_list,"elf.keywords_list")

        
        response = self.dbclient.findAll(self.keywords_list)
        return response

        
        
        

#s = Nlp()
#s.analyzer("How do i view my course on Canvas")




