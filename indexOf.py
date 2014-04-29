def indexOf(s, x):
    index = 0
    while index < len(s) and s[index] != x:
        index += 1
    else:
        if index == len(s):
            return -1
        else:
            return index
