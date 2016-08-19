from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class Indexer:

    '''Creates an inverted index:
    Takes urlToText map returned by Extractor as input
    Returns a tokenToUrlsList map as output
    Can be improved with abstract class for indexes'''

    tokenToUrlsList = {}

    def __init__(self, myTextDict):
        self.myDict = myDict
        Indexer.tokenToUrlsList = tokenToUrlsList

    def build_index(self):
        # get urls corresponding texts in list
        documents = (value for key, value in (self.myDict).iteritems())
        # remove common words and tokenize
        stoplist = set(stopwords.words('english'))
        texts = [[word for word in document.lower().split() if word not in stoplist]
                 for document in documents]
        # assign unique ids to unique tokens from texts, can be stored on disk
        dictionary = corpora.Dictionary(texts)
        # create inverted index from dictionary
        for tok in dictionary:
            for key, value in (self.myDict).iteritems():
                if dictionary[tok] in value:
                    if any(dictionary[tok] is term for term, urls in (Indexer.tokenToUrlsList).iteritems()):
                        if key not in tokenToUrlsList[(dictionary[tok])]:
                            Indexer.tokenToUrlsList[(dictionary[tok])].append(key)
                    else:
                        Indexer.tokenToUrlsList[(dictionary[tok])] = [key]

        return Indexer.tokenToUrlsList
