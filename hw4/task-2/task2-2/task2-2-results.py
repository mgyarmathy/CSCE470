import sys
import operator

file = open(sys.argv[1], 'r')

review_probabilities = dict()

for line in file:
	review_id, probability = line.replace('"','').strip().split('\t')
	review_probabilities[review_id] = float(probability)

print sorted(review_probabilities.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]