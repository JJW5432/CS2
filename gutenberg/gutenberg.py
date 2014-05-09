FILE = './story.txt'

def main(file):
    file = open(file, 'r')
    ptext = file.read()
    file.close()
#print text

from string import punctuation

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

def cutoff(dict, cutoff):
    new_dict = {}
    while len(new_dict) < cutoff:
        highest = max(dict.values())
        current_len = len(new_dict)
        index = 0
        while len(new_dict) == current_len and index < len(dict):
            key = dict.keys()[index]
            if dict[key] == highest:
                new_dict[key] == highest
                
