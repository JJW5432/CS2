# Jake Waksbaum
# IntroCS2 pd 1
# HW#23 -- Title/Topic
# 2014-03-24

def closerNum(target, num1, num2):
    """ operates on 3 numeric parameters, returning a string stating which of the 2nd and 3rd arguments is closer to the first.
    Tests:
    >>> closerNum(8, 20, 10)
    '8 is closer to 10'

    >>> closerNum(8, 20, 2)
    '8 is closer to 2'

    >>> closerNum(8, -2, 30)
    '8 is closer to -2'

    >>> closerNum( 8, 9, 7)
    '8 is equally close to 9 and 7'
    """
    dist1, dist2 = abs(target - num1), abs(target - num2)
    if dist1 > dist2: #num1 is farther away than num2
        return str(target) + " is closer to " + str(num2)
    elif dist1 < dist2: #num1 is closer than num2
        return str(target) + " is closer to " + str(num1)
    else:
        return str(target) + " is equally close to " + str(num1) + " and " + str(num2)
