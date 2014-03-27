"""
Jake Waksbaum
IntroCS2 pd 1
HW#16
2014-03-12
"""

import math

def sign(x):
	"""returns -1 if x is negative, 0 if x is 0, and 1 if x is 1

	Tests
	>>> sign(5)
	1

	>>> sign(1)
	1

	>>> sign(0.0000001)
	1

	>>> sign(0)
	0

	>>> sign(-4)
	-1
	"""
	return cmp(x, 0)

def discriminant(a,b,c):
	"""takes numeric inputs a, b, c -- representing coefficients of a quadratic equation in standard form -- and returns the disciminant of said equation.

	Tests
		>>> discriminant(1,2,3)
		-8

		>>> discriminant(2,4,2)
		0

		>>> discriminant(1,3,2)
		1
	"""
	return b**2 - 4*a*c

def numRealRoots(a,b,c):
	"""takes numeric inputs a, b, c -- representing coefficients of a quadratic equation in standard form -- and returns the number of real roots of said equation.
	
	Tests
		>>> numRealRoots(1,2,3)
		0
		
		>>> numRealRoots(2,4,2)
		1
		
		>>> numRealRoots(1,3,2)
		2
	"""
	return sign(discriminant(a,b,c)) + 1

def intify(float_num):
	"""converts numbers of type float with integer values to numbers of type integer, otherwise returns input unaltered.

	Tests
		>>> intify(5.0)
		5

		>>> intify(5.5)
		5.5
	"""
	if type(float_num) == float and int(float_num) == float_num: float_num = int(float_num) #remove unecessary decimal
	return float_num

def quadSolver(a,b,c):
	"""takes numeric inputs a, b, c -- representing coefficients of a quadratic equation in standard form -- and prints the roots, if any. Uses numRealRoots(a,b,c) as a helper function.

	Tests
		>>> quadSolver(1,2,3)
		no real roots
		
		>>> quadSolver(1,4,4)
		-2

		>>> quadSolver(1,-2,-15)
		-3 5
	"""
	if numRealRoots(a,b,c) == 0:
		output = "no real roots"
	elif numRealRoots(a,b,c) == 1:
		output = -b / 2. * a
		output = intify(output)
	else:
		r1, r2 = (-b - math.sqrt( discriminant(a,b,c) ) )/(2.*a), (-b + math.sqrt( discriminant(a,b,c) ) )/(2.*a)
		r1, r2 = intify(r1), intify(r2)
		output = str(r1) + " " + str(r2)
	print output

if __name__ == "__main__":
	import doctest
	doctest.testmod()