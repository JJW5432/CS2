#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html>"
print "<html>"
print """
<head>
<title>
Word Frequency
</title>
</head>
"""
print "<body>"

print "<h1> Word Frequency in <a href ='http://www.gutenberg.org/ebooks/22381'> Myths and Legends of Ancient Greece and Rome, by E.M. Berens</a></h1>"
##################################
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
		elif word != '':
			buckets[word] = 1
	return buckets

#proof of concept for dict_html
def cutoff(old_dict, cutoff):
	"""returns a dictionary of length cutoff of the key value pairs from d with the highest values"""
	#pytest.set_trace()
	d = old_dict.copy() #make a copy
	new_dict = {}
	while len(new_dict) < cutoff:
		highest = max(d.values())
		for key in d:
			if d[key] == highest:
				new_dict[key] = highest
				del d[key]
				break
	return new_dict

def dict_html(old_dict, cutoff, key_header="key", value_header="value"):
	#pytest.set_trace()
	d = old_dict.copy() #make a copy
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


FILE = './lit.txt'

f = open(FILE, 'r')
text = f.read()
print dict_html(word_count(text), 30, "word", "frequency")
f.close()
##################################
print """
</body>
</html>
"""

### Credit to Team Rando: Joseph Han, Alonzo Ding, Vincent Tang