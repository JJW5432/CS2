file = open('./story.txt', 'r')
ptext = file.read()
file.close()
#print text

from string import punctuation

#def jake_strip(word, chars):
#    while word[0] in chars or word[-1] in chars:
#        if word[0] in chars:
#            word = word[1:]
#        elif word[-1] in chars:
#            word = word[:-1]
#    return word


def word_count(text):
    words = text.split(' ')
    buckets = {}
    for word in words:
        #preprocess
        word = word.strip(punctuation).lower()
        if word in buckets.keys():
            buckets[word] += 1
        else:
            buckets[word] = 1
    return buckets
