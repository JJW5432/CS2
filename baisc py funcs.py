# Jake Waksbaum
# IntroCS2 pd 1
# HW12
# 2014-03-05

import math
#1. cartDist(x1,y1,x2,y2)
print "1. cartDist(x1,y1,x2,y2)\n"
def cartDist(x1,y1,x2,y2):
    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

print cartDist(0,0,0,0)
print "should be 0\n"

print cartDist(4,4,4,4)
print "should be 0\n"

print cartDist(0,0,3,4)
print "should be 5\n"

print "\n\n"


def pythTriple (a, b, c):
    return (a ** 2 + b ** 2 == c ** 2) or (
        b**2 == a**2 + c**2 ) or (a**2 == b**2 + c**2)
print pythTriple (0,0,0)
