# Team Sticky Fingers -- Jake Waksbaum and Abndy Tso
# IntroCS2 pd 1
# HW#32 -- Removal
# 2014-04-10

"""
POP:
syntax: array.pop(index)
behavior: removes the element at index from array and returns it. if no index is specified, assumes -1

REMOVE:
syntax: array.remove(element)
behavior: removes first occurance of element from array

DEL:
syntax: del var
behavior: removes the value of var. If var is a slice of a list, removes that slice

We chose remove for use in rmNegatives2() because we know the element we want to remove, we don't know the index, and we only want to remove a single element
"""

def rmNegatives1(L):
    """removes the negative numbers from list L, assumed to contain only numeric elements. (Modifies L; does not create a new list.)
    Tests:
    >>> L = [5, 4,3,2,1]
    >>> rmNegatives1(L)
    >>> L
    [5, 4, 3, 2, 1]
    
    >>> L = [5,-4,3,-2,1]
    >>> rmNegatives1(L)
    >>> L
    [5, 3, 1]
    """ 
    index = 0
    while index < len(L):
        if L[index] < 0:
            L[index:] = L[index+1:]
        else:
            index += 1

def rmNegatives2(L):
    """removes the negative numbers from list L, assumed to contain only numeric elements. (Modifies L; does not create a new list.)
    Tests:
    >>> L = [5, 4,3,2,1]
    >>> rmNegatives2(L)
    >>> L
    [5, 4, 3, 2, 1]
    
    >>> L = [5,-4,3,-2,1]
    >>> rmNegatives2(L)
    >>> L
    [5, 3, 1]
    """
    for n in L:
        if n < 0:
            L.remove(n)


if __name__ == "__main__": #runs tests in correct context
    import doctest
    doctest.testmod()
    print "tested"
