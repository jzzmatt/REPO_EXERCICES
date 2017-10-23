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



while True:
    print (" TRANSLATE INTEGER BY 'X' ")
    print("---------------------------")
    userinput= input("Enter a Number between 1-10\n:")
    traduce = Traduce_by_x(userinput)
    traduce.display()
    print("\n\n")

    bottom_menu = input("Press <Enter> to Continue, Q to <Quit> ").upper()
    if bottom_menu == "Q" : break
