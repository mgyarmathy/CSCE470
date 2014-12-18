from twitter_api import TwitterAPI

import sys
import re

def tokenize(string):
    #return a list of words
    return [str(i) for i in re.findall('\w+', string.lower())]

def jaccard_similarity(a, b):
    return (float(len(a&b)) / float(len (a|b)))

def main():
    t = TwitterAPI()
    query_1 = sys.argv[1]
    query_2 = sys.argv[2]
    tweet_limit = sys.argv[3]
    search_results_1 = t.search_tweets(query_1, tweet_limit)
    search_results_2 = t.search_tweets(query_2, tweet_limit)

    query_token_set_1 = set(tokenize(' '.join(search_results_1)))
    query_token_set_2 = set(tokenize(' '.join(search_results_2)))

    print jaccard_similarity(query_token_set_1, query_token_set_2)

if __name__ == "__main__":
    main()