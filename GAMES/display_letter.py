guesses = []  #first we create an Empty list

word = "PIANO"


def get_letter():
    '''

    :return: This function permit a user to enter a character
             this character are checked
             for valueError(No more than 1 char and must be a alpha
             Then return this letter
    '''
    userinput = input("Enter> ")

    if len(userinput) > 1 or userinput == '':
        raise ValueError ("Can't Enter more than 1  or Empty character")

    elif userinput.isnumeric():
        raise ValueError("Your letter can't be an integer")

    else:
        return userinput


def check_duplicate(yourletter, guessword):
    if yourletter in guessword:
        return True
    return False


def is_matching(userguess, randomword):
    return userguess in randomword



while True:  #this loop, while display the guesses list and get eache user letter
    print("ENTER YOUR  GUESSES LETTER: ")
    print("---------------------------")
    for l in guesses:
        print(l, end= ' ') #displaying each list letter with a ' '

    print("\n{}".format('- ' * len(guesses)))


    letter = get_letter().upper()

    if check_duplicate(letter, guesses) or not is_matching(letter, word):
        print ("either you have already guess this letter\nor "
               "your guesses doesn't match the secret word !!!")
        continue


    else:
        guesses.append(letter)

    userinput= input("\n\nPress <ENTER> to Continue, <Q> to Quit").upper()

    if userinput == "Q":
        print("Quitting...")
        break




