# Jake Waksbaum
# IntroCS2 pd 1
# HW12
# 2014-03-05

import math

#1. areaCirc(r)
print "1. areaCirc(r)\n"
def areaCirc(r):
    """takes numeric input r and returns the area of a circle of radius r."""
    return r**2 * math.pi

print areaCirc(1)
print "...should be 3.14159265359\n"


print areaCirc(3)
print "...should be 28.2743338823\n"

print areaCirc(5)
print "...should be 78.5398163397\n"

print "\n\n"

#2. areaWasher(radInner, radOuter)
print "2. areaWasher(radInner, radOuter)\n"
def areaWasher(radInner, radOuter):
    """takes numeric inputs radOuter, radInner and returns the area of a washer with inner radius radInner and outer radius radOuter."""
    return areaCirc(radOuter) - areaCirc(radInner)

print areaWasher(0, 2)
print "...should be 12.5663706144\n"

print areaWasher(3, 5)
print "...should be 50.2654824574\n"

print areaWasher(6, 10)
print "...should be 201.06192983\n"

print "\n\n"

#3. sumOfSquares(a,b)
print "3. sumOfSquares(a,b)\n"
def sumOfSquares(a,b):
    """takes numeric inputs a, b and returns the sum of their squares"""
    return a**2 + b**2

print sumOfSquares(0,0)
print "...should be 0\n"

print sumOfSquares(1,2)
print "...should be 5\n"

print sumOfSquares(4,5)
print "...should be 41\n"

print "\n\n"
