# Team #9 -- Dante Secada-Oz, Jake Waksbaum, Lydia Chen
# IntroCS2 pd 1
# HW #26 - Anslatingtray Englishway intoway Igpay Atinlay  
# 2014-3-31

#Pig Latin Rules:
    #1. For words begining with consonants, shift all letters comprising the first sound to the end of word and add the suffix "ay"
    #2. If the word begins with a vowel, add the suffix "way"
    #3. If the given word begins with a capitalized letter, capitalize the first letter of the translated word
    
#Summary of Approach:
    #translate one word 
        #get the starting sound, which will be nothing for a word starting with a vowel
        #take off the starting sound from the beginning, add it to the end, and add 'ay'
        #	except if there is no starting sound (becasue it starts with a vowel) add 'w' where you would add the starting sound
        #if the original word was capitalized, capitalize the output

    #translate a phrase
    	## recursive approach: while there is still phrase left to translate
	    	# look for a word
		    	# pass on everything before the word as is
		    	# pass translated the word
		    	# chop off everything up until the end of the word
		    # if there are no words left pass everything you've got left and you're done


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
	return "abcdefghijklmnopqrstuvwxyz".find(char.lower()) != -1


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
	if word[0].lower() == 'y':
		return 'y'
	elif word[0:2].lower() == 'qu':
		return 'qu'
	index = 0
	while not is_vowel(word[index]):
		index += 1
		#print index
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

			>>> pigWord("Jake's")
			"Ake'sjay"

			>>> pigWord("can't")
			"an'tcay"

			>>> pigWord("she'")
			"eshay'"
	"""
	if word[-1] == "'": 	# since single quote can be an apostrophe, it get's passed to this function
		close_quote = "'"	# if it's at the end it's a close quote so stick on the end
		word = word[:-1]
	else:
		close_quote = ''
	if starting_sound(word) == '':
		sound = 'w'
	else:
		sound = starting_sound(word)
	output = word[len(starting_sound(word)):] + sound + 'ay' + close_quote
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

			>>> findWordStart("'")
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

			>>> findWordEnd("can't")
			5

			>>> findWordEnd("she'") # since single quote can be apostrophe or close quote, we leave it on and is handled by pigWord
			4
	"""
	index = findWordStart(phrase)
	if index == -1:  # no words to begin with
		return -1
	while index < len(phrase) and (is_letter(phrase[index]) or phrase[index] == "'"): #apostrophe doesn't end a word for contractions
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

<<<<<<< HEAD
			>>> translate('school-work')
			'oolschay-orkway'
=======
			>>> translate("You can't do that!!")
			"Ouyay an'tcay oday atthay!!"

			>>> translate("But then she said to me, 'I've had enough.'")
			"Utbay enthay eshay aidsay otay emay, 'I'veway adhay enoughway.'"
>>>>>>> updates
	"""
	output = ''
	while len(phrase) > 0:
		start, end = findWordStart(phrase), findWordEnd(phrase)		# so we don't call function many times
		if start != -1:								# there are words left
			output += phrase[:start]  				# get everything before the word
			output += pigWord(phrase[start:end])  	# get the translated word
			phrase = phrase[end:]  					# slice off what we got
		else: # no words left
			output += phrase						# stick on whats left
			phrase = ''								# empty phrase to get out of the loop
	return output

if __name__ == "__main__":
	import doctest
	doctest.testmod()
