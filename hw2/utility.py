from __future__ import division
import json #or cjson
import re
from stemming.porter2 import stem
from operator import itemgetter
from math import log
class TextProcess(object):
    def __init__(self):
        pass
    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
        return json.loads(a_json_string_from_document)
    @staticmethod
    def tokenize(string):
        unicode_word=re.findall(r'\w+',string['text'].lower())
        return [str(word) for word in unicode_word ]
        #return a list of words

    @staticmethod
    def stopword(a_list_of_words):
        stopword = []
        for line in open('stop_word','r'):
            stopword.append(re.split('\n',line)[0])
        new_list=[word for word in a_list_of_words if word not in stopword]
        return new_list
        #or alternatively use new_list=filter(lambda x: x not in stopword, a_list_of_words)
        #return a list of words 
    @staticmethod
    def stemming(a_list_of_words):
        stems=[stem(word) for word in a_list_of_words]
        return stems
        #return a list of words
if __name__ == '__main__':
    pass