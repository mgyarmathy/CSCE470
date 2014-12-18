
from __future__ import division
from operator import itemgetter
from math import log, sqrt
from utility import TextProcess
import re
import collections
class Hw2(object):
    def __init__(self, a_document_name):
        # term counts: number of documents that contain a given term (key)
        self.term_counts = dict()
        self.reviews = dict()

        file = open(a_document_name)

        for review in file:
            review_id = TextProcess.read_line(review)['review_id'].encode('utf8')
            review_content = TextProcess.read_line(review)['text'].encode('utf8')
            self.reviews[review_id] = review_content
            tokens = TextProcess.stemming(TextProcess.stopword(TextProcess.tokenize(TextProcess.read_line(review))))
            unique_tokens = list(set(tokens))
            for token in unique_tokens:
                if token in self.term_counts:
                    self.term_counts[token] += 1
                else:
                    self.term_counts[token] = 1

        self.idf = dict()
        for term, term_count in self.term_counts.iteritems():
            self.idf[term] = log(len(self.reviews)/term_count)

        self.tfidf_dict = dict()
        for review_id, review in self.reviews.iteritems():
            tokens = TextProcess.stemming(TextProcess.stopword(re.findall(r'\w+',review.lower())))
            tf = collections.Counter(tokens)
            review_tfidfs = list()
            for term, term_count in self.term_counts.iteritems():
                if term in tf:
                    review_tfidfs.append((1+log(tf[term]))*self.idf[term])
                else:
                    review_tfidfs.append(0)
            self.tfidf_dict[review_id] = review_tfidfs

    def cosine_similarity_matrix(self):
        #return a dictionary with each key,value pair as review_id1,[review_id2,cosine_socre]
        # note to self, no need to do review_id1, [review_id2, score] and review_id2, [review_id1, score]
        # (score is the same)
        # start at first review, and compare to all 633 others, then do review 2, and compare to remaining 363
        cosine_similarity = dict()
        tfidf_list = self.tfidf_dict.items()
        for i in xrange(0, len(tfidf_list)-1):
            review1_id, review1_tfidf_vector = tfidf_list[i]
            for j in xrange(i+1, len(tfidf_list)):
                review2_id, review2_tfidf_vector = tfidf_list[j]
                cosine_similarity[review1_id+' '+review2_id] = self.cosine(tfidf_list[i], tfidf_list[j])
                print review1_id+' '+review2_id+": "+str(cosine_similarity[review1_id+' '+review2_id])
        return cosine_similarity

    def get_similar_review(self,cosine_similarity_matrix):
        print '\nHomework 2, Part 2: list the top-10 most similar reviews'
        for pair in sorted(cosine_similarity_matrix.iteritems(), key=itemgetter(1), reverse=True)[:10]:
            review_pair, similarity = pair
            review_ids = review_pair.split(' ')
            print review_ids[0]+": "+self.reviews[review_ids[0]]
            print review_ids[1]+": "+self.reviews[review_ids[1]]
            print '\n----\n'

    @staticmethod
    def cosine(review1,review2):
        review1_id, v1 = review1
        review2_id, v2 = review2
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        if sumxx == 0 or sumyy == 0:
            # avoid divide by 0 error. cosine similarity with zero vector is undefined
            # (reviews with all stop words produce a zero vector!)
            return None
        return sumxy/sqrt(sumxx*sumyy)

hw = Hw2('review_KcSJUq1kwO8awZRMS6Q49g')
hw.get_similar_review(hw.cosine_similarity_matrix())