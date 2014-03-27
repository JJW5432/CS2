"""Jake Waksbaum
IntroCS2 pd 1
HW#16
2014-03-12
"""

def sleep_in(weekday, vacation):
	"""The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 
	
	Tests
		>>> sleep_in(False, False)
		True
		
		>>> sleep_in(True, False)
		False
		
		>>> sleep_in(False, True)
		True
		
		>>> sleep_in(True, True)
		True
	"""
	return (not weekday) or vacation

def diff21(n):
	"""Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
	Tests
		>>> diff21(19)
		2
		
		>>> diff21(10)
		11
		
		>>> diff21(21)
		0
		
		>>> diff21(22)
		2
		
		>>> diff21(25)
		8
		
		>>> diff21(30)
		18
		
		>>> diff21(0)
		21
		
		>>> diff21(1)
		20
		
		>>> diff21(2)
		19
		
		>>> diff21(-1)
		22
		
		>>> diff21(-2)
		23
		
		>>> diff21(50)
		58

	"""
	if n>21:
		return 2*(n-21)
	else:
		return 21-n

def near_hundred(n):
	"""Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number. 

	Tests
		>>> near_hundred(93)
		True
		
		>>> near_hundred(90)
		True
		
		>>> near_hundred(89)
		False
		
		>>> near_hundred(110)
		True
		
		>>> near_hundred(111)
		False
		
		>>> near_hundred(121)
		False
		
		>>> near_hundred(0)
		False
		
		>>> near_hundred(5)
		False
		
		>>> near_hundred(191)
		True
		
		>>> near_hundred(189)
		False
		
		>>> near_hundred(190)
		True
		
		>>> near_hundred(200)
		True
		
		>>> near_hundred(210)
		True
		
		>>> near_hundred(211)
		False
		
		>>> near_hundred(290)
		False
	"""
	return abs(n-100)<=10 or abs(n-200)<=10

def parrot_trouble(talking, hour):
	"""We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

	Tests
		>>> parrot_trouble(True, 6)
		True
		
		>>> parrot_trouble(True, 7)
		False
		
		>>> parrot_trouble(False, 6)
		False
		
		>>> parrot_trouble(True, 21)
		True
		
		>>> parrot_trouble(False, 21)
		False
		
		>>> parrot_trouble(False, 20)
		False
		
		>>> parrot_trouble(True, 23)
		True
		
		>>> parrot_trouble(False, 23)
		False
		
		>>> parrot_trouble(True, 20)
		False
		
		>>> parrot_trouble(False, 12)
		False
	"""
	return talking and (hour<7 or hour>20)

def pos_neg(a, b, negative):
	"""Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. 

	Tests
		>>> pos_neg(1, -1, False)
		True
	
		>>> pos_neg(-1, 1, False)
		True
		
		>>> pos_neg(-4, -5, True)
		True
		
		>>> pos_neg(-4, -5, False)
		False
		
		>>> pos_neg(-4, 5, False)
		True
		
		>>> pos_neg(-4, 5, True)
		False
		
		>>> pos_neg(1, 1, False)
		False
		
		>>> pos_neg(-1, -1, False)
		False
		
		>>> pos_neg(1, -1, True)
		False
		
		>>> pos_neg(-1, 1, True)
		False
		
		>>> pos_neg(1, 1, True)
		False
		
		>>> pos_neg(-1, -1, True)
		True
		
		>>> pos_neg(5, -5, False)
		True
		
		>>> pos_neg(-6, 6, False)
		True
		
		>>> pos_neg(-5, -6, False)
		False
		
		>>> pos_neg(-2, -1, False)
		False
		
		>>> pos_neg(1, 2, False)
		False
		
		>>> pos_neg(-5, 6, True)
		False
		
		>>> pos_neg(-5, -5, True)
		True
	"""
	if negative:
		return a<0 and b<0
	else:
		return (a<0 and b>0) or (a>0 and b<0)

if __name__ == "__main__":
	import doctest
	doctest.testmod()