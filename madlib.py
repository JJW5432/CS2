# Jake Waksbaum
# IntroCS2 pd 2
# HW37 -- Fill in the Blanks
# 2014-04-28
## to run with tests execute 'test.py madlib.py'
## Mechanism for Madlibification:
## Peer-reviewed by Andy Tso
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Search for open and close brackets with tag word inside
## Replace string between those indices with a random element from the corresponding list

from random import choice
from string import lower, upper, capitalize
import pytest

nouns = ['student', 'sensei', 'monkey', 'grasshopper', 'tiger', 'bamboo', 'sushi', 'tank', 'rocket ship', 'moon']
adjectives = ['stinky', 'funny', 'pink', 'hairy', 'serendipitous', 'supersillious', 'discombobulated', 'absurd']
adverbs = ['gracefully', 'clumsily', 'fanatically', 'frantically', 'quickly', 'always', 'hapharzardly']
verbs = ['jumps', 'plays', 'runs', 'cries', 'laughs', 'lives', 'loves', 'dies', 'circumlocutes', 'disenfranchises']
numbers = map(str, range(1000)) + ['pi', 'phi', 'e', 'i']
places = ['the moon', '\'merica', 'new york city', 'hell', 'north korea', 'canada', 'the promised land', 'hawaii', 'alaska', 'ukraine']
family_members = ['mother', 'father', 'mama', 'papa', 'sister', 'brother', 'cousin', 'aunt', 'uncle', 'grandma', 'grandpa', 'second cousin twice removed']
animals = ['cat', 'dog', 'mouse', 'koala', 'kangaroo', 'llama', 'unicorn']
names = ['jake', 'clyde', 'james', 'phil', 'sherry', 'sarah']
body_parts = ['head', 'shoulders', 'knees', 'toes', 'belly', 'legs', 'fingers']
seasons = ['summer', 'fall', 'winter', 'spring']

def gerund(verb):
    if verb[-2:]=='es':
        verb = verb[:-2]
    elif verb[-1] == 's':
        verb = verb[:-1]
    return verb + 'ing'

tags = [        'NOUN', 'ADJECTIVE', 'ADVERB', 'VERB', 'VERBING', 'NUMBER', 'PLACE', 'FAMILY MEMBER', 'ANIMAL', 'NAME', 'BODY PART', 'SEASON']
dictionary = [   nouns,  adjectives,  adverbs,  verbs, map(gerund, verbs), numbers, places, family_members, animals, names, body_parts, seasons]

def find_tag(s):
    """finds a tag in the form <TAG> and returns [start, end, TAG]"""
    start = s.find('<')
    end = s.find('>')
    if end < start:
        return False
    elif s[start+1:end].upper() in tags:
        return [start, end+1, s[start+1:end]]
    else:
        return False

def is_capitalize(w):
    return w.capitalize() == w

def is_upper(w):
    return w.upper() == w

def is_lower(w):
    return w.lower() == w

def get_func(w):
    out_funcs = [capitalize, upper, lower]
    test_funcs = [is_capitalize, is_upper, is_lower]
    for i in range(len(test_funcs)):
        if test_funcs[i](w):
            return out_funcs[i]

def indexReplace(indices, new, s):
    """replaces slice specified in indices of string s with string new"""
    return s[:indices[0]] + new + s[indices[1]:]

def madlibs(story):
    while find_tag(story):
        # pytest.set_trace()
        start, end, tag = find_tag(story)
        word_list = dictionary[tags.index(tag.upper())]
        word = choice(word_list)
        func = get_func(tag)
        word = func(word)
        story = indexReplace([start, end], word, story)
    return story

print madlibs("This <season> vacation I went to <place> with my <family member>, <family member>, and <family member>. We were there for <number> days, <verbing> <adverb>. We also explored <place> nearby, and we saw some <adjective> <animal>s. Unfortunately, when I was <verbing>, I hurt my <body part> with a <noun>.")




def test_indexReplace():
    assert "i want to go"[3:5] == "an"
    assert indexReplace([3,5], 'jake', "i want to go") == "i wjaket to go"

def test_find_tags():
    assert find_tag("<NOUN>") == [0, 6, 'NOUN']
    s = "hello my <NOUN>"
    assert find_tag(s) == [9, 15, 'NOUN']
    assert s[find_tag(s)[0] : find_tag(s)[1]] == "<NOUN>"
    assert find_tag("helllo my <FACE>") == False

def test_fillBlanks():
    assert madlibs("<NOUN>") in map(upper, nouns)
    assert madlibs("<Noun>")in map(capitalize, nouns)
    assert madlibs("<noun>")in map(lower, nouns)

def test_string_checks():
    assert is_capitalize("Hello")
    assert not is_capitalize("hello")
    assert is_upper("HELLO")
    assert not is_upper("hello")
    assert is_lower("hello")
    assert not is_lower("Hello")
    assert get_func("Hello") == capitalize
    assert get_func("HELLO") == upper
    assert get_func("hello") == lower
    assert gerund('plays') == 'playing'
    assert gerund('makes') == 'making'
