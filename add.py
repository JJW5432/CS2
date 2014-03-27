def add(a, b):
	"""Adds two numeric inputs, a and b
	Tests:
		>>> add(1,2)
		3

		>>> add(5,10)
		15
	"""
	return a + b

if __name__ == "__main__": 	# check for appropriate context
	import doctest		# import necessary module
	doctest.testmod()		# run tests