def min_max_indexes(seq):
    minimum = min(enumerate(seq), key= lambda s: s[1])
    maximum = max(enumerate(seq), key= lambda s: s[1])
    return minimum[0], maximum[0]




mylist = [5, 0, 1, 4, 6, 3]

print(min_max_indexes(mylist))

print(mylist[1], mylist[4])