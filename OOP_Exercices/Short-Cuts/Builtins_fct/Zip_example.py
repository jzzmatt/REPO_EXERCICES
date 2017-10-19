'''
The Zip function takes 2 or more sequences and creates a new seq of tuples
Each tuple contains one element from each list
'''

list_one = ['a','b', 'c']
list_two = [1, 2, 3]

zipped = zip(list_one, list_two)  #build the Object ZIP

zipped = list(zipped) #Convert the Object to a list
print(zipped)

unzipped = zip(*zipped)
print(unzipped)

print(list(unzipped))