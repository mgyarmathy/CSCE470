#!/usr/bin/env python
# -*- coding: utf-8  -*-
#encoding=utf-8

import tweepy
import sys

class TwitterAPI():
    # Fill in the blanks here for your own Twitter app.
    consumer_key = "YUnDNCjuS4cr6ACScO9vScHIT"
    consumer_secret = "yRBmuGM4b65jDi0nJDnaGvFFXUoWJHGwZyPlIfZmm21T5EBhTm"
    access_key = "155607388-oeL64uExr4OrQpEvoFTon5QJGNqQboHrPCcd4C6C"
    access_secret = "SQBvMMqgvgPusr9JQ6d79t0G28zTECnLmoHf5w60GVV6X"
    auth = None
    api = None

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())
        # print self.api.rate_limit_status()

    def re_init(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())

    def search_tweets(self, query, count):
        search_results = self.api.search(q=query, count=count, result_type="popular")
        tweets = list()
        for tweet in search_results['statuses']:
            tweets.append(tweet['text'].encode('utf-8'))
        return tweets

if __name__ == "__main__":
    pass