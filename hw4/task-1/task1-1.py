import json
import operator
from copy import deepcopy

def read_list_data(list_file):
	twitter_lists = dict();
	file = open(list_file)

	for line in file:
		user_id, info = json.loads(line)
		twitter_lists[user_id] = info;
		twitter_lists[user_id]['hub'] = len(info['out'])
		twitter_lists[user_id]['auth'] = len(info['in'])

	return twitter_lists

def iterate_hits(twitter_lists):
	new_lists = deepcopy(twitter_lists)

	for user_id, info in new_lists.items():
		hub_score = 0
		auth_score = 0
		for out_link_id in info['out']:
			hub_score = hub_score + twitter_lists[out_link_id]['auth']
		for in_link_id in info['in']:
			auth_score = auth_score + twitter_lists[in_link_id]['hub']
		new_lists[user_id]['hub'] = hub_score
		new_lists[user_id]['auth'] = auth_score

	return new_lists


def main():
	twitter_lists = read_list_data('sports_list.json')

	for x in range(5):
		twitter_lists = iterate_hits(twitter_lists)

	top_hubs_dict = dict()
	top_auth_dict = dict()
	for user_id, info in twitter_lists.items():
		top_hubs_dict[user_id] = info['hub']
		top_auth_dict[user_id] = info['auth']

	top_hubs = sorted(top_hubs_dict.items(), key=operator.itemgetter(1), reverse=True)
	top_auth = sorted(top_auth_dict.items(), key=operator.itemgetter(1), reverse=True)
	
	print "Top Hubs"
	for x in range(10):
		print str(x+1) + ".\tUser ID: " + str(top_hubs[x][0]) + "\tScore: " + str(top_hubs[x][1])

	print "\nTop Authorities"
	for x in range(10):
		print str(x+1) + ".\tUser ID: " + str(top_auth[x][0]) + "\tScore: " + str(top_auth[x][1])

if __name__ == '__main__':
    main()
