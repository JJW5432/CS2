#import pytest
from string import punctuation

def word_count(text):
	"""returns a dictionary where every word in text is a key and the value is the occurances of that word"""
	words = text.split(' ')
	buckets = {}
	for word in words:
		#preprocess
		word = word.strip(punctuation).lower()
		if word in buckets.keys():
			buckets[word] += 1
		else:
			buckets[word] = 1
	return buckets

def cutoff(old_dict, cutoff):
	"""returns a dictionary of length cutoff of the key value pairs from old_dict with the highest values"""
	#pytest.set_trace()
	new_dict = {}
	while len(new_dict) < cutoff:
		highest = max(old_dict.values())
		for key in old_dict:
			if old_dict[key] == highest:
				new_dict[key] = highest
				del old_dict[key]
				break
	return new_dict