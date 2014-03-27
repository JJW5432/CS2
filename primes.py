import math
def is_prime(x):
    """tests if x is prime
    Tests:
        >>> is_prime(1)
        False

        >>> is_prime(2)
        True

        >>> is_prime(9)
        False

        >>> is_prime(15)
        False

        >>> is_prime(39)
        False

        >>> is_prime(53)
        True
    """
    if x ==1:
        return False
    factor = 2
    while factor <= math.sqrt(x):
        if x%factor == 0:
            return False
        factor += 1
    return True

def findfactor(x):
    """finds first factor pair of x
    Tests:
        >>> findfactor(15)
        [3, 5]

        >>> findfactor(20)
        [2, 10]

        >>> findfactor(5)
        [1, 5]
    """
    factor = 2
    while factor <= math.sqrt(x):
        if x%factor == 0:
            return [factor, x / factor]
        factor += 1
    return [1, x]

def primefactor(x):
    """returns all prime factors of x in a list

    Tests:
        >>> primefactor(1)
        [1]

        >>> primefactor(2)
        [2]

        >>> primefactor(6)
        [2, 3]

        >>> primefactor(36)
        [2, 2, 3, 3]

        >>> primefactor(1575)
        [3, 3, 5, 5, 7]
    """
    if x == 1:
        return [1]
    if x==2:
        return [2]
    factor_list = []
    for factor in findfactor(x):
        if is_prime(factor):
            factor_list.append(factor)
        else:
            factor_list += primefactor(factor)
    return sorted(factor_list)

def nthPrime(n):
    """returns a list of the first n primes
    Tests:
        >>> nthPrime(1)
        [2]

        >>> nthPrime(4)
        [2, 3, 5, 7]

        >>> nthPrime(6)
        [2, 3, 5, 7, 11, 13]
    """
    primes = [2, 3]
    if n == 1:
        return [2]
    while len(primes) < n:
        x = primes[-1] + 2
        while not is_prime(x):
            x += 2
        else:
            primes.append(x)
    return primes

if __name__ == "__main__": #runs tests in correct context
    import doctest
    doctest.testmod()