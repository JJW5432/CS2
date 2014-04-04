# Jake Waksbaum
# IntroCS2 pd 1
# HW#28 -- The Reigning Champion
# 2014-04-03

#print [1] + [2]
#x = [1,2]
#y = [3,4]
#print x + y
#print x
#print [1,2] + [2,3]

def minPos(l):
    """takes a list L containing only numeric elements, and returns the position (index) of the least value
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()