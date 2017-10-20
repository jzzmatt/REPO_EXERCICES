import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog ' \
        'donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole ' \
        'monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino ' \
        'salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey weasle ' \
        'whale wolf wombat zebra'.split()



class RandomWord(object):
    def __init__(self, wordlist):
        self.wordlist = wordlist

    @property
    def getWord(self):
        '''
        
        :return: Return a Random word from the list
        '''
        _idx_word= random.randint(0, len(self.wordlist) -1)
        return words[_idx_word]



class HangMan(object):
    def __init__(self, randomword, userguesses):
        self._randomword = randomword
        self._userguesses = userguesses
        self._missedLetter = ''
        self._correctLetter = ''


    def is_matching(self):
        if self._userguesses not in self._randomword:
            self._missedLetter += self._userguesses


        else:
            self._correctLetter += self._userguesses
            return True

        return False


    def is_winner(self):
        return self._correctLetter == self._userguesses




    







#getword = RandomWord(words).getWord
#print(getword)
