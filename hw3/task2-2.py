from twitter_api import TwitterAPI

import sys
import re
import collections
import operator

def tokenize(string):
    #return a list of words
    return [str(i) for i in re.findall('\w+', re.sub('@\w+', '', string.lower()))]

def stopword(a_list_of_words):

    stop_words = open('stop_word').read().split('\n')

    #return a list of words 
    return [i for i in a_list_of_words if i not in stop_words]

def improved_similarity(search_results_1, search_results_2):
    a = collections.Counter(stopword(tokenize(' '.join(search_results_1))))
    b = collections.Counter(stopword(tokenize(' '.join(search_results_2))))
    top_terms_1 = list()
    top_terms_2 = list()
    for item in sorted(a.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]:
        key, value = item
        top_terms_1.append(key)

    for item in sorted(b.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]:
        key, value = item
        top_terms_2.append(key)
    a = set(top_terms_1)
    b = set(top_terms_2)
    print a
    print b
    return (float(len(a&b)) / float(len (a|b)))

def main():
    t = TwitterAPI()
    query_1 = sys.argv[1]
    query_2 = sys.argv[2]
    tweet_limit = sys.argv[3]
    search_results_1 = t.search_tweets(query_1, tweet_limit)
    search_results_2 = t.search_tweets(query_2, tweet_limit)

    print improved_similarity(search_results_1, search_results_2)

if __name__ == "__main__":
    main()