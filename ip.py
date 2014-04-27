# Jake Waksbaum
# IntroCS2 pd 1
# HW36 -- Ayn Paul Range
# 2014-04-27


# algorithm:
#   append the smaller of the first elements of the two lists, removing them from the lists until one list is empty
#   then add the rest of the elements from on the end
def merge(L1, L2):
    """ Returns a new list containing the elements of both lists, in sorted (ascending) order. Assumes each input list is sorted. (Therefore, you may not use any sorting functions as helpers.) The length of the output list should equal the sum of the lengths of the input lists.
    >>> a = [0, 2, 4, 6, 8]
    >>> b = [1, 3, 5, 7]
    >>> merge(a,b)
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    out = []
    while len(L1) > 0 and len(L2) > 0:
        #print L1
        #print L2
        if L1[0] < L2[0]:
            out.append(L1[0])
            L1=L1[1:]
        else:
            out.append(L2[0])
            L2=L2[1:]
    out.extend(L1)
    out.extend(L2)
    return out

# algorithm:
#   iterate over numbers 0 through n-1, each time appending a random number between 0 and 255 inclusive
import random
def randList(n):
    out = []
    for x in range(n):
        out.append(random.randrange(256))
    return out

# algorithm:
#   concatenate 4 random numbers between 0 and 255, with periods seperating
def randIP():
    out = ""
    for x in randList(4):
        out += str(x) + "."
    return out[:-1]

print randIP()
print randIP()
print randIP()

#if __name__ == "__main__":
import doctest
doctest.testmod()
