#import nltk
#nltk.download('stopwords')

from nltk.corpus import stopwords

class Stopwords(object):
    def __init__(self):
        self.stop_words = (set(stopwords.words('english')))
