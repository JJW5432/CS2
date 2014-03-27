# Jake Waksbaum
# IntroCS2 pd 1
# HW#19
# 2014-03-17

def addMultPrint(a,b):
	"""takes 2 numeric inputs and prints a message:
		"the sum of {a} and {b} is {a+b}
		their product is {a*b}"

	Tests
		>>> addMultPrint(3,6)
		the sum of 3 and 6 is 9
		their product is 18
	"""
	print "the sum of " + str(a) + " and " + str(b) + " is " + str(a+b) + "\ntheir product is " + str(a*b)


def addMultHTML(a,b):
	"""takes 2 numeric inputs and returns a string of HTML code that will render as shown below:
		"the <i>sum</i> of {a} and {b} is <b>{a+b}</b>
		their <i>product</i> is <b>{a*b}</b>"

	Tests
		>>> addMultHTML(3,6)
		'the <i>sum</i> of 3 and 6 is <b>9</b><br>their <i>product</i> is <b>18</b>'
	"""
	output = "the <i>sum</i> of " + str(a) + " and " + str(b) + " is <b>" + str(a+b) + "</b><br>their <i>product</i> is <b>" + str(a*b) + "</b>"
	return output

def sumDigits(n):
	"""helper function for tablefy; returns the sum of the digits of n.
	
	Tests
		>>> sumDigits(123)
		6

		>>> sumDigits(12345)
		15

		>>> sumDigits(4)
		4

		>>> sumDigits(110)
		2
	"""
	sumD=0
	while n>=10:
				sumD=sumD+(n%10)
				n=n//10
	return sumD+n #the last digit



def tablefy(start, end):
	output = ""
	output += "<style> table, tr, td, th {border: 1px black solid} th {font-weight: bold}</style>"
	output += "<table>"
	output += "<tr>"
	output += "\t<th>n</th>"
	output += "\t<th>n^2</th>"
	output += "\t<th>sumDigits</th>"
	output += "</tr>"
	if end < start:
		start, end = end, start
	while start <= end:
		output += "<tr>"
		output += "\t<td>" + str(start)+ "</td>"
		output += "\t<td>" + str(start**2)+ "</td>"
		output += "\t<td>" + str(sumDigits(start))+ "</td>"
		output += "</tr>"
		start += 1
	output += "</table>"
	return output

if __name__ == "__main__": #runs doctest
	import doctest
	doctest.testmod()
