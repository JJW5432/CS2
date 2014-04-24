# Jake Waksbaum
# IntroCS2 pd 1
# HW33 -- Statistic
# 2014-04-18

def intify(n):
    """takes a float and returns n as an int if it is an integer, and as a float if it is not
    Tests:
    >>> intify(5)
    5

    >>> intify(5.0)
    5

    >>> intify(5.5)
    5.5
    """
    if int(n) == n:
        return int(n)
    else:
        return n

def meanList(L):
    """returns the mean of a list
    Tests:
    >>> meanList([1,2,3,4,5])
    3

    >>> meanList([1,2,3,4,5,6])
    3.5
    """
    output = 0
    for n in L:
        output += n
    return intify(output / float(len(L)))

def medList(L):
    """returns the median of a list
    Tests:
    >>> medList([1,2,3,4,5])
    3

    >>> medList([1,2,3,4,5,6])
    3.5
    """
    while len(L) > 2:
        L.remove(myMax(L))
        L.remove(myMin(L))
    return meanList(L)

def barGraphify(nums):
    """takes a list of non-negative integers and prints a set of bars as shown
    Tests:
    >>> barGraphify([0,1,2,3])
    0:
    <BLANKLINE>
    1:=
    <BLANKLINE>
    2:==
    <BLANKLINE>
    3:===
    <BLANKLINE>

    >>> barGraphify([1,0,3,2])
    0:=
    <BLANKLINE>
    1:
    <BLANKLINE>
    2:===
    <BLANKLINE>
    3:==
    <BLANKLINE>
    """
    index = 0
    while index < len(nums):
        print str(index) + ":"  + nums[index] * "=" + "\n"
        index += 1

def myMin(L):
    """returns the smallest element of a list
    Tests:
    >>> myMin([1,3,2,-5])
    -5
    """
    lowest = L[0]
    for x in L:
        if x < lowest:
            lowest = x
    return lowest

def myMax(L):
    """returns a list sorted from lowest to highest
    Tests:
    >>> myMax([1,3,2,-5])
    3
    """
    highest = L[0]
    for x in L:
        if x > highest:
            highest = x
    return highest

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print "tested"
