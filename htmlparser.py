import db
import nltk
nltk.data.path.append("./nltk_data")

from nltk.corpus import stopwords
from nltk.tag import pos_tag
from PyDictionary import PyDictionary
import re


class htmlparser(object):
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
        for word_tuple in tagged_sent:
            if word_tuple[0] not in self.stop_words:
                word_list = list(word_tuple)
                word_list[0] = re.sub('[!?%$*.@]','',word_list[0])
                tokenizer.append(tuple(word_list))
        
        for word_tuple in tokenizer:
            if word_tuple[1] == 'NNP':
                self.keywords_list.append(word_tuple[0].lower())
            else:
                if self.dictionary.synonym(word_tuple[0].lower()):
                    self.keywords_list.append(word_tuple[0].lower())
                    self.keywords_list.extend(self.dictionary.synonym(word_tuple[0].lower()))
                   
        mongo_dict["keywords"] = list(set(self.keywords_list))
        mongo_dict["text"] = "While creating a new assignment, click on More options. Set the submission type to Online submissions. From the short list of options that appear, you will want to check the box next to Enable Turnitin Submissions. You may also click on Advanced Settings to explore more options for your Turnitin assignment."

        
        self.dbclient.insert(mongo_dict)

        
        
        

s = htmlparser()
s.analyzer("How do I enable Turnitin for my assignments?")




