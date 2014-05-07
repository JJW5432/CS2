# Team Flying Fish -- Jake, Andy, and Eric
# IntroCS2 pd 1
# HW41 -- ASCIIng About Your Face
# 2014-05-05

def common(L1, L2):
    """takes 2 lists as input and returns a new list containing values common to both. Assumes no repeated values in either list.
    >>> common( [1,5,4,3,2] , [4,5,10,15] )
    [4, 5]"""
    shared = []
    for a in L1:
        if a in L2:
            shared.append(a)
    return sorted(shared)

# algorith:
#   split the list on commas
#   merge every other element
#   sort resulting list
def alphabetize(names):
    """takes a string of names, assumed to be in Last-First pairings, separated by commas, and returns an alphabetized list of names with line breaks in string form
    >>> alphabetize( "Wayne,Bruce,Kent,Clark,Parker,Peter" )
    'Kent Clark\\nParker Peter\\nWayne Bruce'
    """
    names = names.split(',')
    merged = []
    for index in range(len(names)/2):                               # loop over every element in each of the half-lists
        merged.append(names[::2][index] + ' ' + names[1::2][index]) # combine corresponding names (those with same index in half-lists)
    merged = alpha_sort(merged)
    return "\n".join(merged)

def alpha_sort(L):
    output = []
    while len(L) >= 1:
        output.append(min(L))
        L.remove(min(L))
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()
