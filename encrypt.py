# Jake Waksbaum
# IntroCS2 pd 1
# HW34 -- Cereal-Grade Encyrption
# 2014-03-25

import string

def rot(s):
    """ takes a single-letter string input and returns its rot13 equivalent.
    Tests:
    >>> rot('B')
    'O'

    >>> rot('b')
    'o'

    >>> rot('s')
    'f'
    """
    if s in string.ascii_uppercase:
        base = string.ascii_uppercase
    elif s in string.ascii_lowercase:
        base = string.ascii_lowercase
    index = (base.find(s) + 13) % len(base)
    return base[index]
        
def printEmAll():
    """prints all letters of the alphabet along with the rot13 equivelant of each
    Tests:
    """
    count = 0
    base = string.ascii_uppercase + string.ascii_lowercase
    while count < len(base):
        print base[count] + " <-> " + rot(base[count])
        count += 1

def rot13Wrd(word):
    """takes a string input (all caps, no spaces) and returns its rot13 encoding.
    Tests:
    >>> rot13Wrd('JABBERWOCKY')
    'WNOOREJBPXL'
    """
    count = 0
    output = ''
    while count < len(word):
        output += rot(word[count])
        count += 1
    return output

def encryptable(chr):
    """checks if char is encryptable
    Tests:
    >>> encryptable('A')
    True

    >>> encryptable('x')
    True

    >>> encryptable('?')
    False

    >>> encryptable(' ')
    False

    >>> encryptable('4')
    False
    """
    return (ord(chr) >= ord('A') and ord(chr) <= ord('Z')) or (ord(chr) >= ord('a') and ord(chr) <= ord('z')) 
    
def rot13(phrase):
    """encrypts a string with spaces and punctuation
    Tests:
    >>> rot13('Justin Bieber')
    'Whfgva Ovrore'

    >>> rot13("Justin Bieber? Like, OMG!!! He's my hero!")
    "Whfgva Ovrore? Yvxr, BZT!!! Ur'f zl ureb!"
    """
    index = 0
    output = ''
    while index < len(phrase):
        if encryptable(phrase[index]):
            output += rot(phrase[index])
        else:
            output += phrase[index]
        index += 1
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
