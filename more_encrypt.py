# Flying Koalas
# IntroCS2 1
# HW25 - Furhter Explorations in Toy Encryption
# 2014-03-27

import string

def rotn(n, s):
    """
    >>> rotn(2, 'a')
    'c'

    >>> rotn(6, 'b')
    'h'

    >>> rotn(2, 'z')
    'b'
    """
    if s in string.ascii_lowercase:
        base = string.ascii_lowercase
    elif s in string.ascii_uppercase:
        base = string.ascii_uppercase
    index = base.find(s)
    return base[( index + n ) % len(base)]

def rotnWrd(n, s):
    """
    >>> rotnWrd(2, 'abc')
    'cde'
    """
    count = 0
    output = ''
    while count < len(s):
        output += rotn(n, s[count])
        count += 1
    return output

def rotTest(limit, s):
    while limit > 0:
        print str(limit) + ": " + rotnWrd(limit, s)
        limit -= 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
