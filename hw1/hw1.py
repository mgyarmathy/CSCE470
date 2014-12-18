import json #or cjson
import re
import operator
from stemming.porter import stem

class Hw1(object):
    def __init__(self):
        pass
        
    @staticmethod
    def read_line(a_json_string_from_document):
        return json.loads(a_json_string_from_document)
        
    
    @staticmethod
    def tokenize(string):
        #return a list of words
        return [str(i) for i in re.findall('\w+', string.lower())]
    
    
    @staticmethod
    def stopword(a_list_of_words):

        stop_words = open('stop_word').read().split('\n')

        #return a list of words 
        return [i for i in a_list_of_words if i not in stop_words]
    
    
    @staticmethod
    def stemming(a_list_of_words):        
        #return a list of words
        return [stem(i) for i in a_list_of_words]
    
    
    def unigram_count(self, a_document_name):

        unigrams = dict()
        unigrams_stemmed = dict()

        file = open(a_document_name)
        
        for review in file:
            tokens = self.stopword(self.tokenize(self.read_line(review)['text']))
            for token in tokens:
                if token in unigrams:
                    unigrams[token] += 1
                else:
                    unigrams[token] = 1
            for stemmed_token in self.stemming(tokens):
                if stemmed_token in unigrams_stemmed:
                    unigrams_stemmed[stemmed_token] += 1
                else:
                    unigrams_stemmed[stemmed_token] = 1

        top_unigrams = sorted(unigrams.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]
        top_unigrams_stemmed = sorted(unigrams_stemmed.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]
        
        #return top 20 unigrams e.g. {[hot,99],[dog,66],...}
        return top_unigrams, top_unigrams_stemmed

    
    def bigram_count(self,a_document_name):

        bigrams = dict()

        file = open(a_document_name)
        
        for review in file:
            tokens = self.stopword(self.tokenize(self.read_line(review)['text']))
            i = 0
            while i < len(tokens)-1:
                bigram = tokens[i] + " " + tokens[i+1]
                if bigram in bigrams:
                    bigrams[bigram] += 1
                else:
                    bigrams[bigram] = 1
                i += 1

        #return top 20 bigrams and frequency pairs, e.g. {[hot dog,88],[apple pie,54],...}
        return sorted(bigrams.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]


if __name__ == '__main__':
    pass
    #hw=Hw1()
    #your code
