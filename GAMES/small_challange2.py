import random
'''
Randomly Selects a Word from a List of at Least 10

Prompts the User to Enter a Letter:
 - if the letter is in the Random Word, add that letter to a correct_lettes
 _ if the letter is no in the Random Word, add that letter to incorrect letters
 - if the letter has been guess already print a message informing the user
 - Do not append the errant letter
 - Display to the usr the list of correct and incorrect letter they have chosen
'''


class Check(object):
    good_guesses = []
    bad_guesses  = []

    def __init__(self, userinput, guessletter):
        self.userinput = userinput
        self.guessletter = guessletter


    def isin_randomword(self):
        return self.userinput in self.guessletter


    def isalready_guess(self):
        return self.userinput in self.good_guesses

    def update_goodlist(self):
        if not self.userinput in self.good_guesses:
            self.good_guesses.insert(self.guessletter.index(self.userinput), userinput)

        else:
            self.good_guesses.append(self.userinput)


    def update_badlist(self):
        self.bad_guesses.append(self.userinput)


    def is_winer(self, word_random):
        return (''.join(self.good_guesses) == word_random)





class GuessLetter(Check):


    @classmethod
    def get_goodguesses(cls):
        return cls.good_guesses

    @classmethod
    def get_badguesses(cls):
        return cls.bad_guesses


    def isalready_guess(self):
        print("Your Letter are already guesses")
        super().isalready_guess()


    def getstatus(self):
        if self.isin_randomword():
            self.get_goodguesses().append(self.userinput)

        else:
            self.get_badguesses().append(self.userinput)


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


def get_word(userinput, randomword):
    convertword = list(randomword)
    neworld = []

    if userinput in randomword:
        neworld.insert(randomword.index(userinput), userinput)

    return neworld



while True:
    print("GOOD GUESSES : {} ".format(''.join(GuessLetter.get_goodguesses())))
    print("BAD GUESSES : {}".format(''.join(GuessLetter.get_badguesses())))

    print("---- GUESSES LETTER ----")
    userinput = input("Please Enter your guesses\n: ")
    guessletter = GuessLetter(userinput, random_word)

    if guessletter.is_winer(random_word):
        print("You WIN!!!!")
        break

    if not guessletter.isalready_guess() and guessletter.isin_randomword():
        guessletter.update_goodlist()

    else:
        guessletter.update_badlist()









