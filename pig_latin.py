def is_vowel(char):
	"""checks if one character string char is a vowel
	Tests:
		>>> is_vowel(a)
		True
		
		>>> is_vowel(A)
		True
		
		>>> is_vowel(b)
		False
		
		>>> is_vowel(y)
		False
	"""
	return "aeioiu".find(char) != -1

if __name__ == "__main__":
	import doctest
	doctest.testmod()