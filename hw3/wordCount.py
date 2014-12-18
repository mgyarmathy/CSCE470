#!/usr/bin/env python
from mrjob.job import MRJob
import re
import simplejson as json
class CountWords(MRJob):
    def mapper(self,key,line):
        text=json.loads(line)['text']
        for word in re.findall(r'\w+',text.lower()):
            yield word, 1
    def reducer(self, word, counts):
        yield word, sum(counts)
    def steps(self):
        return [self.mr(mapper = self.mapper, reducer = self.reducer)]
if __name__ == '__main__':
    CountWords.run()
