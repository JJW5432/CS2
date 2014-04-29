# Jake Waksbaum
# IntroCS2 Pd1
# HW34 -- Stats 2
# 2014-04-23

#algorithm: loop through all items in L, comparing occurances against occurances of current reigning champ, and dethroning him if necessary
def modeListA(L):
    """returns the mode, as a single number, of the set of numeric elements in list nums
    Tests:
    >>> modeListA( [0,5,7,3,2,3] )
    3

    >>> modeListA( [0,5,7,3,7,3] )
    7
    """
    champ = L[0]
    for x in L:
        if L.count(x) > L.count(champ):
            champ = x
    return champ

#algorithm:
#   generate a unique verison of L so that each element only gets one shot
#       loop throuch indices of L, and only include the element at that index if that is the first occurance of that element
#   loop through unique list, comparing occurances of each element IN ORIGINAL LIST to those of any of current reigning champs, dethroning everyone or joining their ranks if necessary
def modeListB(L):
    """returns a list of the modes of a list
    Tests:
    >>> modeListB( [0,5,7,3,2,3] )
    [3]

    >>> modeListB( [0,5,7,3,7,3] )
    [3, 7]
    """
    # uniq = [ L[x] for x in range(len(L)) if L.index(L[x]) == x]
    uniq, index = [], 0                 # uniq has one of every element in L
    while index < len(L):
        if L.index(L[index]) == index:  # if the index of the element at index L is the first occurance of said element
            uniq.append(L[index])       # ^^ matches only once per element, specifically the first occurance
        index += 1
    champ = [ L[0] ]
    for x in uniq:
        if L.count(x) > L.count(champ[0]):
            champ = [x]
        elif L.count(x) == L.count(champ[0]):
            champ.append(x)
    return sorted(champ)                # for deterministicness


#algorithm:
#   build output string row by row
#   only those with the highest values get a star, but then get reduced by one, slowly leveling playing field
#       if no star spaces to position other stars
#   as the highest value gets lower, more indices qualify and therefore are reduced
#   eventually every element is 0 and you're done with stars
#   print x-axis by looping over elements in list and incrementing a counter
def vBarGraphify(nums):
    """
    Tests:
    >>> x = [0,1,2,3]
    >>> vBarGraphify(x)
          *
        * *
      * * *
    0 1 2 3

    >>> x = [1,0,3,2]
    >>> vBarGraphify(x)
        *
        * *
    *   * *
    0 1 2 3
    """
    output = ''
    while max(nums) > 0:                        # while there are still stars to print
        cutoff = max(nums)
        for x in nums:
            if x == cutoff:                     # if x is one of the highest
                output += '* '                  # that index gets a star in this row
                nums[nums.index(x)] = x - 1     # take one star out of the bank
            else:                               # x is too low to get a star
                output += '  '                  # add spaces to position other stars
        output = output[:-1]                    # remove trailings space
        output += '\n'
    else:                                       # after all stars are printed, print x-axis
        count = 0
        for x in nums:
            output += str(count) + ' '
            count += 1
        output = output[:-1]
    print output

import doctest
doctest.testmod()
#print "tested"
