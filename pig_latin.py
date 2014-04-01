# Team #9 -- Dante Secada-Oz, Jake Waksbaum, Lydia Chen
# IntroCS2 pd 1
# HW #26 - Anslatingtray Englishway intoway Igpay Atinlay  
# 2014-3-31

#Pig Latin Rules:
    #1. For words begining with consonants, shift all letters before the first vowel to the end of word and add the suffix "ay"
    #2. If the word begins with a vowel, add the suffix "way"
    #3. If the given word begins with a capitolized letter, capitolized the first letter of the translated word
    
#Summary of Approach:

#PseudoCode
    #translation function
        #word in phrase
         #begins with a consonant
           #append all constants before the first vowel
           #add suffix "ay"
         #begins with a vowel
             #append "way"
         #if first letter is capitolized
             #uppercase the first letter of the newer string


def is_vowel(char):
	"""checks if one character string char is a vowel
	Tests:
			>>> is_vowel('a')
			True

			>>> is_vowel('A')
			True

			>>> is_vowel('b')
			False

			>>> is_vowel('y')
			True
	"""
	return "aeioiuy".find(char.lower()) != -1


def is_letter(char):
	"""checks if one character string char is a letter
	Tests:
			>>> is_letter('a')
			True

			>>> is_letter('!')
			False

			>>> is_letter(' ')
			False
	"""
	return 'abcdefghijklmnopqrstuvwxyz'.find(char.lower()) != -1


def is_capitalized(word):
	"""checks if word is capitalized
	Tests:
			>>> is_capitalized('hello')
			False

			>>> is_capitalized('Hello')
			True

			>>> is_capitalized('HELLO')
			True
	"""
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(word[0]) != -1


def starting_sound(word):
	"""returns the beginning consonant sound of a word
	Tests:
			>>> starting_sound('hello')
			'h'

			>>> starting_sound('school')
			'sch'

			>>> starting_sound('apple')
			''

			>>> starting_sound('yonder')
			'y'

			>>> starting_sound('crystal')
			'cr'

			>>> starting_sound('quiet')
			'qu'
	"""
	if word[0] == 'y':
		return 'y'
	elif word[0:2] == 'qu':
		return 'qu'
	index = 0
	while not is_vowel(word[index]):
		index += 1
	return word[:index]


def pigWord(word):
	"""translates a single word into piglatin
	Tests:
			>>> pigWord('hello')
			'ellohay'

			>>> pigWord('Hello')
			'Ellohay'

			>>> pigWord('school')
			'oolschay'

			>>> pigWord('apple')
			'appleway'

			>>> pigWord('Apple')
			'Appleway'

			>>> pigWord('yonder')
			'onderyay'

			>>> pigWord('crystal')
			'ystalcray'
	"""
	if starting_sound(word) == '':
		sound = 'w'
	else:
		sound = starting_sound(word)
	output = word[len(starting_sound(word)):] + sound + 'ay'
	if is_capitalized(word):
		output = output.capitalize()
	return output


def findWordStart(phrase):
	"""returns the index of the first character of the first word of a phrase
	so that phrase[findWordStart:findWordEnd] is the first word
	Tests:

			>>> findWordStart('hello')
			0

			>>> findWordStart('hello how are you')
			0

			>>> findWordStart(' hello how are you')
			1

			>>> findWordStart('!!!!!, adf%&#(@')
			7

			>>> findWordStart('!!!!')
			-1
	"""
	index = 0
	while index < len(phrase) and not is_letter(phrase[index]):
		index += 1
	if index == len(phrase):  # got to end and there are no letters
		return -1
	return index


def findWordEnd(phrase):
	"""returns the one more than the index of the last character of the first word of a phrase
	so that phrase[findWordStart:findWordEnd] is the first word
	Tests:
			>>> findWordEnd('hello')
			5

			>>> findWordEnd('hello how are you')
			5

			>>> findWordEnd(' hello how are you')
			6

			>>> findWordEnd('!!!!!, adf%&#(@')
			10

			>>> findWordEnd('!!!!!!')
			-1
	"""
	index = findWordStart(phrase)
	if index == -1:  # no words to begin with
		return -1
	while index < len(phrase) and is_letter(phrase[index]):
		index += 1
	return index


def translate(phrase):
	"""returns Pig Latin equivalent of the string phrase
	Tests:
			>>> translate("the pope rocks red kicks")
			'ethay opepay ocksray edray ickskay'

			>>> translate("!!!!!!!!!Hello!!!!!!!!!")
			'!!!!!!!!!Ellohay!!!!!!!!!'

			>>> translate("!!!")
			'!!!'

			>>> translate('But soft! What light through yonder window breaks? It is the east, and Juliet is the sun.')
			'Utbay oftsay! Atwhay ightlay oughthray onderyay indowway eaksbray? Itway isway ethay eastway, andway Ulietjay isway ethay unsay.'
			>>> translate('quiet')
			'ietquay'

			>>> translate('pyramid')
			'yramidpay'

			>>> translate('school-work')
			'oolschay-orkway'
	"""
	output = ''
	while len(phrase) > 0:
		# print phrase
		start, end = findWordStart(phrase), findWordEnd(phrase)		# so we don't call function many times
		if start == -1:			# there are no words left
			output += phrase	# stick on whats left
			phrase = ''			# empty phrase to get out of the loop
		else:
			# print str(start) + " " + str(end)
			# print phrase[start:end]
			output += phrase[:start]  									# get everything before the word
			output += pigWord(phrase[start:end])  						# get the translated word
			phrase = phrase[end:]  										# slice off what we got
			# print output
			# print "\n"
	return output


if __name__ == "__main__":
	import doctest
	doctest.testmod()
