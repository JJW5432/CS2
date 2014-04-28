from madlib import *
import pytest

def test_indexReplace():
    assert "i want to go"[3:5] == "an"
    assert indexReplace([3,5], 'jake', "i want to go") == "i wjaket to go"

def test_find_tags():
    assert find_tag("<NOUN>") == [0, 6, 'NOUN']
    s = "hello my <NOUN>"
    assert find_tag(s) == [9, 15, 'NOUN']
    assert s[find_tag(s)[0] : find_tag(s)[1]] == "<NOUN>"
    assert find_tag("helllo my <FACE>") == False
    assert find_tag("hello my /<NOUN/>") == False

def test_fillBlanks():
    assert fillBlanks("<NOUN>") in nouns
    print fillBlanks("The <ADJECTIVE> <NOUN> <VERB> <ADVERB> upside down.")
