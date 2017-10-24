'''
PART1
Prompt the User to enter a number 1-10
Remember to convert the response to an int

write a for loop that prints an(X) for each number the user entered

eg.
user input 5 => (X)(X)(X)(X)(X)
user input 2 => (x) (X) 


PART2
Randomly Select a Word from a list of 15 possible choices

Have the program print a blank space for each character in the word as , was shown in the example

On the next line,  have the program print out the word , but check for letter that are common to you first name

if the letter is in your name print the proper letter in place of the blank

if the letter is not in your name, print only a blank space

'''

import random


class Traduce_by_x(object):
    def __init__(self, yourinteger):
        self.yourinteger = int(yourinteger)

    @property
    def get_x(self):
        tile = 'X'
        if self.yourinteger <= 10:
            return (tile * self.yourinteger)
        else:
            raise Exception ("Your Integer can't be > 10 ")



    def display(self):
        for l in self.get_x:
            print ("({})".format(l), end=' ')

'''

while True:
    print (" TRANSLATE INTEGER BY 'X' ")
    print("---------------------------")
    userinput= input("Enter a Number between 1-10\n:")
    traduce = Traduce_by_x(userinput)
    traduce.display()
    print("\n\n")

    bottom_menu = input("Press <Enter> to Continue, Q to <Quit> ").upper()
    if bottom_menu == "Q" : break
    
    '''


RANDOMWORD = ['lion',
              'tigre',
              'elephant',
              'eagle',
              'shark',
              'snake',
              'monkey',
              'leopard',
              'chita',
              'rabbit',
              ]


random.shuffle(RANDOMWORD)
random_word = RANDOMWORD.pop()



class Word(object):
    def __init__(self, yourword):
        self.yourword = yourword

    def cover(self):
        new_word = ''

        for l in self.yourword:
            if l != '-':
                l = '-'
                new_word += l
        return new_word


class Uncover(Word):
    def __init__(self, yourword):
        super().__init__(yourword)

    def uncover(self, userinput):
        old_str = self.cover()
        uncoverstr = ''

        if userinput in self.yourword:
            idx = self.yourword.index(userinput)
            uncoverstr += old_str[:idx+1] + userinput + old_str[idx+1:]


        return uncoverstr





'''

word2 = Uncover("stone")

print(word2.cover())
print(word2.uncover("e"))
'''
word3 = Uncover("stone")
newwword=''
while True:

    display = word3.uncover(newwword)
    print(display)

    userinput = input(">: ")

    newwword+= userinput









'''
def get_coverlist(yourlist):
    coverlist = []  # ['-', '-']

    for i in yourlist:
        i = '- '
        coverlist.append(i)

    return coverlist


def get_uncoverlist(guessword, yourword):
    new_word = ''
    for i in guessword:
        if i in yourword:
            new_word += i+' '

        else:
            new_word += '- '
    return new_word


guessesword =''

while True:

    print(random_word)
    coverlist = get_coverlist(random_word)
    print('{}\n{}'.format(''.join(coverlist), guessesword))

    user_input = input("> ")
    uncover = get_uncoverlist(random_word, user_input)
    guessesword += uncover

    menu_bottom = input("Press <Enter> to Continue, Q <Quit>").upper()

    if menu_bottom == 'Q' : break
    
'''




