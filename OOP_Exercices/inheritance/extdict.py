'''
EXTEND A DICTIONNARIES
This class, will show the longestKey character
'''

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key

        return longest

'''
TESTING


longkeys = LongNameDict()

longkeys['hello'] = 1
longkeys['longest key'] = 5
longkeys['hello2'] = 'world'


print(longkeys.longest_key())

'''

