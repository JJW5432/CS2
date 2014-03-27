# Jake Waksbaum
# IntroCS2 pd 1
# HW#22
# 2014-mm-dd


def bondify(name):
	"""takes a name written in First Last format, and returns the sassy version
	Tests:
		>>> bondify("James Bond")
		'Bond, James Bond'

		>>> bondify("Jake Waksbaum")
		'Waksbaum, Jake Waksbaum'
	"""
	space = name.find(' ')
	first, last = name[0:space], name[space+1:len(name)]
	return last + ', ' + first + ' ' + last

def replace(s,q,r):
	"""takes 3 string inputs and replaces any occurrences of q in s with r. If there is no occurrence of q in s, then s is returned unchanged

	Tests:
		>>> replace('Winter is coming', 'Winter', 'Spring')
		'Spring is coming'

		>>> replace('Mice run this planet', 'mice', 'dolphins')
		'Mice run this planet'
	"""
	index = s.find(q)
	if index != -1:
		return s[0:index] + r + s[index + len(r) : len(s)]
	else:
		return s

def tablefyASCII():
	"""returns a string of valid HTML code generating a 2-column, 53-row table. This table will show the letters of the alphabet and their associated ASCII value. Letters on the left, numbers on the right."""
	outstring = "<table>\n"
	outstring += "\t<tr>\n"
	outstring += "\t\t<th>Letter</th>\n"
	outstring += "\t\t<th>ASCII value</th>\n"
	outstring += "\t</tr>\n"
	for x in range(65, 91) + range(97, 123):
		outstring += "\t<tr>\n"
		outstring += "\t\t<td>" + chr(x) + "</td>\n"
		outstring += "\t\t<td>" + str(x) + "</td>\n"
		outstring += "\t</tr>\n"
	outstring += "</table>\n"
	return outstring

if __name__ == "__main__": #runs tests in correct context
	import doctest
	doctest.testmod()