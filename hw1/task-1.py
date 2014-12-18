from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'
f=open(infilename,'r')
line_num=1
while(line_num<300):
    f.readline()
    line_num+=1
    
print 'task-1.py // print out the "text" part of the 300th review'
print Hw1.read_line(f.readline())['text']
