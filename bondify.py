# Jake Waksbaum
# IntroCS2 pd 1
# HW#20
# 2014-03-18

def bondify(name):
    """takes a name written in First Last format, and returns the sassy version

    Tests
        >>> bondify("James Bond")
        'Bond, James Bond'

        >>> bondify("Jake Waksbaum")
        'Waksbaum, Jake Waksbaum'
    """
    index = 0 #counter
    first, last = '', '' #storage

    while name[index] != ' ':
        first += name[index] #letter by letter assemble first name
        index += 1
    
    index += 1 #get past the space
   
    while index < len(name):
        last += name[index] #letter by letter assmeble last name
        index += 1

    return last + ", " + first + " " + last

if __name__ == "__main__":
    import doctest
    doctest.testmod()
