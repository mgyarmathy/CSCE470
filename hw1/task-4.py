from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'
f=open(infilename,'r')

tokens = Hw1.tokenize(Hw1.read_line(f.readline())['text'])
stop_removed = Hw1.stopword(tokens)
stemmed = Hw1.stemming(stop_removed)

print 'task-4.py // print out the "text" part of the first review after stemming'
print stemmed