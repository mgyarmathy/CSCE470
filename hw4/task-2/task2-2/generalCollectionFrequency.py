#!/usr/bin/env python

# Reusing wordCount.py from homework 3 to gather word counts of the overall collection

from mrjob.job import MRJob
import re
import simplejson as json

class GeneralCollectionFrequency(MRJob):
    def mapper(self,key,line):
        text=json.loads(line)['text']
        for word in re.findall(r'\w+',text.lower()):
            yield word, 1
    def reducer(self, word, counts):
        yield word, sum(counts)
    def steps(self):
        return [self.mr(mapper = self.mapper, reducer = self.reducer)]
if __name__ == '__main__':
    GeneralCollectionFrequency.run()
