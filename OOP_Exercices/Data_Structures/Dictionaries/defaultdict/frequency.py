'''
CASE 1 using SETDEFAULT
'''

def letter_frequency(sentence):
    '''
    Everytime we access the dictionnary we need to check that if has a value already
    and if not , set it to zero
    :param sentence: 
    :return: 
    '''
    frequencies = {}

    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1

    return frequencies



'''
CASE 2 USING DEFAULTDICT
'''

from collections import defaultdict
def letter_frequency2(sentence):
    frequencies = defaultdict(int)  #call int wihtout any parameter , return 0

    for letter in sentence:
        frequencies[letter] += 1

    return frequencies

'''
CASE 3 USING our OWN fct
'''
num_items = 0

def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])  #return a num for each item and a list of this same items


d = defaultdict(tuple_counter)
d['a'][1].append('hello')
d['b'][1].append('world')

print(d)


