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


class htmlparser(object):
    def __init__(self):
        self.dbclient = db.Ecampusdb()
        self.stop_words = (set(stopwords.words('english')))
        self.dictionary = PyDictionary()
        self.keywords_list = []
        
    
    def analyzer(self,question):
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
        # "How do i view my course on Canvas"
        
        tagged_sent = nltk.pos_tag(word_tokenize(question))
        tokenizer = []
        mongo_dict ={}
        for word_tuple in tagged_sent:
            if word_tuple[0] not in self.stop_words and word_tuple[0]:
                word_list = list(word_tuple)
                word_list[0] = re.sub('[!?%$*.@]','',word_list[0])
                tokenizer.append(tuple(word_list))
        
        for tag in tokenizer:
            print ("tag",tag[0])
            print (self.dictionary.synonym(tag[0].lower()))
            if tag[1] == 'NNP':
                self.keywords_list.append(tag[0].lower())
            else:
                wn_tag = penn_to_wn(tag[1])
                word = WordNetLemmatizer().lemmatize(tag[0],wn_tag)
                print ("word -->", word)
                print ("self.dictionary.synonym(word.lower()) -->",self.dictionary.synonym(word.lower()))
                self.keywords_list.append(word.lower())
                synonym_list = self.dictionary.synonym(word.lower())
                if synonym_list:
                    self.keywords_list.extend(synonym_list)

        mongo_dict["keywords"] = list(set(self.keywords_list))
        mongo_dict["text"] = "Yes, Canvas can be integrated with products like: McGraw-Hill Connect, Macmillan Education, Cengage Learning MindTap, and Pearson's MyLab & Mastering. \
Please visit: http://www.sjsu.edu/ecampus/teaching-tools/canvas/integrating-publisher-db/index.html for more information."

        print (mongo_dict)
        self.dbclient.insert(mongo_dict)    

        
        
        

s = htmlparser()
s.analyzer("Can I integrate my course with any publisher's database like McGraw-Hill Connect?")




