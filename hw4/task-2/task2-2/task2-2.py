from mrjob.job import MRJob
import re
import simplejson as json
import math

class Task2(MRJob):
    @classmethod
    def setup(self):
        self.query_terms = ["best", "cookie", "store"]
        self._lambda = 0.7
        self.general_collection_frequency = dict()
        self.overall_term_count = 0;
        file = open('generalCollectionFrequencyOutput', 'r')
        for line in file:
            term, count = line.replace('"','').strip().split('\t')
            self.general_collection_frequency[term] = int(count)
            self.overall_term_count += int(count)

    def mapper(self,key,line):
        review_id, text = json.loads(line)['review_id'], json.loads(line)['text']
        counts = {}
        words = re.findall(r'\w+',text.lower())
        for word in words:
            counts[word] = counts.get(word, 0) + 1

        for term in self.query_terms:
            if term in counts:
                doc_probability = self._lambda * (float(counts[term]) / float(len(words)))
            else:
                doc_probability = 0.0
            
            if term in self.general_collection_frequency:
                term_probability = (1.0 - self._lambda) * (self.general_collection_frequency[term] / self.overall_term_count)
            else:
                term_probability = 0.0

            # if we're working with log probabilities:
            # yield review_id, math.log(doc_probability + term_probability)

            # if we're working with probabilities:
            yield review_id, (doc_probability + term_probability)

    def reducer(self, review_id, values):
        # if we're working with sum of log probabilities:
        # log_probability = math.fsum(values)
        # yield review_id, log_probability

        # if we're working with product of probabilities:
        probability = reduce(lambda x, y: x * y, values)
        yield review_id, probability


    def steps(self):
        return [self.mr(mapper = self.mapper, reducer = self.reducer)]
        
if __name__ == '__main__':
    Task2.setup()
    Task2.run()