import pytest
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

#proof of concept for dict_html
def cutoff(d, cutoff):
	"""returns a dictionary of length cutoff of the key value pairs from d with the highest values"""
	#pytest.set_trace()
	new_dict = {}
	while len(new_dict) < cutoff:
		highest = max(d.values())
		for key in d:
			if d[key] == highest:
				new_dict[key] = highest
				del d[key]
				break
	return new_dict

def dict_html(d, cutoff=None, key_header="key", value_header="value"):
	#pytest.set_trace()
	if cutoff == None: cutoff = len(d)
	outstring = ["<table border='1px'>"]
	outstring += ["<tr><th>" + key_header + "</th><th>" + value_header + "</th></tr>"]
	while len(outstring)-2 < cutoff:
		highest = max(d.values())
		for key in d:
			if d[key] == highest:
				outstring += ["<tr><td>" + str(key) + "</td><td>" + str(highest) + "</td></tr>"]
				del d[key]
				break
	outstring += ["</table>"]
	return '\n'.join(outstring)