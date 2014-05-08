# Team Da Bomb - Jake Waksbaum and Andy Tso
# IntroCS2 pd 1
# HW43 -- Four de Toid Thyme
# 2014-05-07

def modeList(nums):
    """returns the mode of the set of numeric elements in list nums. Uses a dictionary to implement the "labeled buckets" algorithm.
    >>> modeList( [0,5,7,3,2,3] )
    3
    >>> modeList( [0,5,7,3,7,3] )
    3
    """
    buckets = {}
    for x in nums:
        if x in buckets.keys():
            buckets[x] += 1
        else:
            buckets[x] = 1
    #print buckets
    champ = buckets.keys()[0]
    for x in buckets:
        if buckets[x] > buckets[champ]:
            champ = x
    return champ

import doctest
doctest.testmod()
