# Jake Waksbaum
# IntroCS2 pd 2
# HW35 -- Bucket List
# 2014-04-24


# modeList algorithm:
#   bucket
#       initialize bucket list of length highest element + 1, with all zeroes
#       for each element, increment element in bucket list at that index
#   return all indexes of max of bucket list
#       reigning champ using while loop to get at indices
def indexOfMax(L):
    """returns a list of the indices of the largest element
    Tests:
        >>> indexOfMax([1,5,4,3])
        [1]

        >>> indexOfMax([1,5,3,5,5,4,5])
        [1, 3, 4, 6]
    """
    champ, index = [0], 0
    while index < len(L):
        if L[index] == L[champ[0]]:
            champ.append(index)
        elif L[index] > L[champ[0]]:
            champ = [index]
        index += 1
    return sorted(champ)


def modeList(L):
    """returns the mode, as a single number, of the set of numeric elements
    in list nums. Uses the 'labeled buckets' algorithm discussed in class.
    Tets:
        >>> modeList( [0,5,7,3,2,3] )
        [3]

        >>> modeList( [0,5,7,3,7,3] )
        [3, 7]
    """
    buckets = (max(L)+1) * [0]
    for x in L:
        buckets[x] += 1
    return indexOfMax(buckets)

# vBarGraphify algorithm:
#   build output string row by row
#   only those with the highest values get a star, but then get reduced by one
#       if no star spaces to position other stars
#   as the highest value gets lower, more indices qualify and are reduced
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
