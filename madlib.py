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

nouns = ['student', 'sensei', 'monkey', 'grasshopper', 'tiger', 'bamboo', 'sushi', 'tank', 'rocket ship', 'moon']
adjectives = ['stinky', 'funny', 'black', 'hairy', 'serendipitous', 'supersillious', 'discombobulated', 'absurd']
adverbs = ['gracefully', 'clumsily', 'fanatically', 'frantically', 'quickly', 'always', 'hapharzardly']
verbs = ['jumps', 'plays', 'runs', 'cries', 'laughs', 'lives', 'loves', 'dies', 'circumlocutes', 'disenfranchises']

tags = [        'NOUN', 'ADJECTIVE', 'ADVERB', 'VERB']
dictionary = [   nouns,  adjectives,  adverbs,  verbs]

def find_tag(s):
    """finds a tag in the form <TAG> and returns [start, end, TAG]"""
    start = s.find('<')
    end = s.find('>')
    if end < start \            # first > is before <
       or s[start-1] == '/' \   # commented out
       or s[end-1] == '/':
        return False
    elif s[start+1:end].upper() in tags:
        return [start, end+1, s[start+1:end].upper()]
    else:
        return False

def indexReplace(indices, new, s):
    """replaces slice specified in indices of string s with string new"""
    return s[:indices[0]] + new + s[indices[1]:]

def fillBlanks(story):
    while find_tag(story):
        tag = find_tag(story)
        word_list = dictionary[tags.index(tag[2])]
        word = choice(word_list)
        story = indexReplace(tag[:2], word, story)
    return story

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
    assert fillBlanks("/<NOUN>") == "/<NOUN>"
    print fillBlanks("The <ADJECTIVE> <NOUN> <VERB> <ADVERB> upside down.")
