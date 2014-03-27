# Jake Waksbaum
# IntroCS2 pd 1
# HW#17 - Repetition Two Ways
# 2014-03-13

def input_check(n):
	"""checks for valid input for factorial

	Tests
		>>> input_check(0)
		True

		>>> input_check(5)
		True

		>>> input_check(5.5)
		False

		>>> input_check(-4)
		False
	""" #don't repeat code
	return type(n) == int and n >= 0

def factR(n):
	"""uses recursion to calculate n!

	Tests
		>>> factR(0)
		1

		>>> factR(3)
		6

		>>> factR(12)
		479001600

		>>> factR(-5)
		'Invalid input: must be an integer >= 0'

		>>> factR(1.5)
		'Invalid input: must be an integer >= 0'
	"""
	if input_check(n):
		if n == 0:
			return 1
		else:
			return n*factR(n-1)
	else:
		return "Invalid input: must be an integer >= 0"

def factW(n):
	"""uses iteration (while loop) to calculate n!

	Tests
		>>> factR(0)
		1

		>>> factR(3)
		6

		>>> factR(12)
		479001600

		>>> factR(-5)
		'Invalid input: must be an integer >= 0'

		>>> factR(1.5)
		'Invalid input: must be an integer >= 0'
	"""
	if input_check(n):
		output = 1
		while n > 0:
			output = ouput = output * n
			n = n - 1
		return output
	else:
		return "Invalid input: must be an integer >= 0"

if __name__ == "__main__":
	import doctest
	doctest.testmod()