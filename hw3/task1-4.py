import sys
import operator

file = open(sys.argv[1], 'r')

term_frequencies = dict()

for line in file:
	term, count = line.replace('"','').strip().split('\t')
	term_frequencies[term] = int(count)

print sorted(term_frequencies.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
