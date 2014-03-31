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
	return "aeioiuy".find(char.lower()) != -1
	
def is_upper(word):
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(word[0]) != -1

def first_sound(word):
	if word[0] == 'y':
		return 'y'
	index = 0
	while not is_vowel(word[index]):
		index += 1
	return word[:index]

def pigWord(word):
	if first_sound(word) == '':
		sound = 'w'
	else:
		sound = first_sound(word)
	output = word[len(first_sound(word)):] + sound + 'ay'
	if is_upper(word):
		output = output.capitalize()
	return output

if __name__ == "__main__":
	import doctest
	doctest.testmod()