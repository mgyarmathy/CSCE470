from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'
f=open(infilename,'r')

tokens = Hw1.tokenize(Hw1.read_line(f.readline())['text'])
stop_removed = Hw1.stopword(tokens)

print 'task-3.py // print out the "text" part of the first review after stopword removal'
print stop_removed