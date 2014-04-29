# Jake Waksbaum
# IntroCS2 pd 1
# HW#30 -- The Same But Different
# 2014-04-08

def listSum(L):
    """takes a list L containing only numbers, and returns the sum of it's elements
    Tests:
    >>> listSum( [0,1,2,3] )
    6
    """
    total = 0
    for item in L:
        total += item
    return total

def minVal(L):
    """takes a list L containing only numeric elements, and returns the least value.
    Tests:
    >>> minVal( [3] )
    3
    >>> minVal( [5,4,3,2,1] )
    1
    """
    lowest = L[0]
    for item in L:
        if item < lowest:
            lowest = item
    return lowest

def doublify(L):
    """returns a doublified version of L. Assumes L contains only numeric elements.
    Tests:
    >>> doublify( [3] )
    [6]
    
    >>> doublify( [3,6,9] )
    [6, 12, 18]
    
    >>> doublify( [2,0,4,8] )
    [4, 0, 8, 16]
    """
    output = []
    for item in L:
        output += [item*2] 
    return output
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print
