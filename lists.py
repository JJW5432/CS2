# Jake Waksbaum
# IntroCS2 pd 1
# HW#28 -- The Reigning Champion
# 2014-04-03

def minPos(l):
    """takes a list L containing only numeric elements, and returns the position (index) of the least value
    Tests:
    >>> minPos([1,2,3,-72])
    3

    >>> minPos( [3] )
    0
	
    >>> minPos( [5,4,3,2,1] )
    4
    """
    index = 0
    lowest = 0
    while index < len(l):
        if l[index] < l[lowest]:
            lowest = index
        index += 1
    return lowest

def listSum(L):
    """takes a list L containing only numbers, and returns the sum of elements
    Tests:
    >>> listSum( [0,1,2,3] )
    6
    """
    index = 0
    total = 0
    while index < len(L):
        total += L[index]
        index += 1
    return total

def doublify(L):
    """modifies list L by doubling each of its elements. Assumes L contains only numeric elements.
    Tests:
    >>> x = [1,2,3,4,5]
    >>> doublify(x)
    >>> x
    [2, 4, 6, 8, 10]
    """
    index = 0
    while index < len(L):
        L[index] *= 2
        index += 1


import doctest
doctest.testmod()
