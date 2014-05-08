file = open('./story.txt', 'r')
text = file.read()
file.close()
print text

from string import ascii_letters

def is_letter(char):
    return char in ascii_letters

def strip_punctuation(word):
    for i in range(len(word)):
        char = word[i]
        if not is_letter(char):
            word = word[:i] + word[1+i:]
    return word


def word_count(text):
    words = text.split(' ').strip()
    
