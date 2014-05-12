#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html>"
print "<html>"
print """
<head>
<title>
# title goes here
</title>
</head>
"""
print "<body>"
##################################
import wc


FILE = './story.txt'
#import pytest

f = open(FILE, 'r')
text = f.read()
print wc.dict_html(wc.word_count(text), 30)
f.close()
##################################
print """
</body>
</html>
"""

### Credit to Team Rando: Joseph Han, Alonzo Ding, Vincent Tang