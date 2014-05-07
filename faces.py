#!/usr/bin/python
print "Content-Type: text/html\n"
print ''
print "<!doctype html><html><pre>"
#Team Flying Fish

hair = ['^^^^^', '-----','=====', 'wwwww', '~~~~~', '*****', '#####', 'mmmmm', '((|))', '{[^]}']
eyes = [' 0 0 ', ' @ @ ', '-   -', ' x x ', ' / \ ', ' * * ', ' ^ ^ ', '(` `)', '-O-O-']
nose = ['  v  ', '  -  ', '  U  ', '  V  ', ' ( ) ', ' |_| ', '  ~  ', '  W  ']
mouth = [' ___ ', '_____', ' !@% ', '  O  ', ' *** ', ' --- ', '(---)']

from random import randrange

def choose(L):
    return L[randrange(len(L))]

def face():
    for part in [hair, eyes, nose, mouth]:
        print choose(part)

face()
print "</pre></html>"
