tags = ['NOUN', 'ADJECTIVE', 'ADVERB', 'VERB']

def find_tag(s):
    """finds a tag in the form <TAG> and returns [start, end, TAG]
    Tests:
    >>> find_tag("hello my <NOUN>")
    [9, 14, 'NOUN']

    >>> find_tag("helllo my <FACE>")
    False

    >>> find_tag("hello my /<NOUN/>")
    False
    """
    start = s.find('<')
    end = s.find('>')
    if end < start \
       or s[start-1] == '/' \
       or s[end-1] == '/':
        return False
    elif s[start+1:end].upper() in tags:
        return [start, end, s[start+1:end].upper()]
    else:
        return False

import doctest
doctest.testmod()
