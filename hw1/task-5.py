from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'

hw=Hw1()
top_unigrams, top_unigrams_stemmed = hw.unigram_count(infilename)

print 'task-5.py // '
print 'i) Find the top twenty unigrams in all reviews without stemming:'
print str(top_unigrams)+'\n'
print 'ii) Find the top twenty unigrams in all reviews with stemming:'
print top_unigrams_stemmed