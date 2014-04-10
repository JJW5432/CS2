# Team Sticky Fingeres -- Jake Waksbaum and Andy Tso
# IntroCS2 pd 1
# HW#31 -- Come Together
# 2014-04-09

def rmNegatives(L):
    """removes the negative numbers from list L, assumed to contain only numeric elements. (Modifies L; does not create a new list.)
    Tests:
    >>> L = [5, 4,3,2,1]
    >>> rmNegatives(L)
    >>> L
    [5, 4, 3, 2, 1]
    
    >>> L = [5,-4,3,-2,1]
    >>> rmNegatives(L)
    >>> L
    [5, 3, 1]
    """ 
    index = 0
    while index < len(L):
        if L[index] < 0:
            L[index:] = L[index+1:]
        else:
            index += 1

def listOFib(n):
    """returns a list of the first n Fibonacci numbers, starting with 0 as the 0th term, 1 as the 1st term, 1 as the 2nd term, and so on.
    
    >>> listOFib(1)
    [0]
    
    >>> listOFib(2)
    [0, 1]
    
    >>> listOFib(3)
    [0, 1, 1]
    
    >>> listOFib(4)
    [0, 1, 1, 2]

    >>> listOFib(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    output = [0]
    if n > 1:
        output.append(1) 
    while len(output) < n:
        output.append(sum(output[-2:]) )
    return output

def sentify(L):
    """returns a string comprised of list L’s elements, in order, with spaces between. Assumes L contains only string elements.
    >>> sentify( ["this", "is", "how", "we", "do"] )
    'this is how we do'
    """
    output = ''
    for word in L:
        output += word + " "
    return output[:-1]

if __name__ == "__main__": #runs tests in correct context
    import doctest
    doctest.testmod()
