myword = 'balloon'




def convert_caracter(yourword, userinput):
    _list = ['- ' for x in range(len(list(yourword)))]
    goodguesses = []

    if userinput in yourword:
        goodguesses.append(userinput)


    for idx, item in enumerate(yourword):
        if item in goodguesses:
            _list[idx] = item

    return (''.join(_list))





while True:
    yourlist = ''

    print('- ' * len(myword))
    print(yourlist)

    userinput = input("Enter your letter: ")

    yourlist += convert_caracter(myword, userinput)




