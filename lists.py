print [1] + [2]
x = [1,2]
y = [3,4]
print x + y
print x
print [1,2] + [2,3]

def minPos(l):
    """
    >>> minPos([1,2,3,-72])
    3
    """
    index = 0
    lowest = 0
    while index < len(l):
        if l[index] < l[lowest]:
            lowest = index
    return index

if __name__ == "__main__":
    import doctest
    doctest.testmod()
