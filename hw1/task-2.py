from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'
f=open(infilename,'r')

print 'task-2.py // print out the tokenized "text" part of the first 3 reviews'

for i in xrange(0,3):
    tokens = Hw1.tokenize(Hw1.read_line(f.readline())['text'])
    print tokens
