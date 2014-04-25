# NAME
# IntroCS2 pd 1
# HW#21 -- Clever Problem Solving
# 2014-03-19

import math

##PROBLEM 1 - Multiples of 3 and 5
##algorithm:
##  add by 3 and add to answer until 1000
##  add by 5 and add to answer until 1000
##    but don't forget to skip multiples of 5 that are also multiples of 3 you already added

some = 0
mult = 0
while mult < 1000:
    # print "some:" + str(some)
    # print "mult:" + str(mult)
    some += mult
    mult += 3
mult = 0
while mult < 1000:
    # print "some:" + str(some)
    # print "mult:" + str(mult)
    if mult%3 != 0:
        some += mult
    mult += 5


##PROBLEM 2 - Even Fibonacci numbers
##algorithm:
##  generate fibonacci numbers, check if even, and add to total
total = 0
fib, fib_prev= 1, 1
while fib < 4*10**6:
    fib, fib_prev = fib + fib_prev, fib
    # print fib
    if fib%2 == 0:
        total += fib


##PROBLEM 3 - Largest prime factor
##algorithm:
##  find a factor pair by brute force and then find prime factors of factors recursively
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

##PROBLEM 5 - smallest multiple
##algorithm:
##  
#x = 1
#total = 1
#while x <= 20:


##PROBLEM 6 - sum square difference
##algorithm:
##  iterate over numbers and add their squares and themselves to different totals, then square the one that received the numbers and difference
squares, some, x = 0, 0, 1
while x <= 100:
    squares += x**2
    some += x
    x += 1
some **= 2
difference = some - squares

    
 if True: #runs tests in correct context
        import doctest
        doctest.testmod()
        print 'hey'
