'''
---init---  'Constructor'
'''
import random

class Thief:
    sneaky = True

    def __init__(self, name, sneaky = True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)   #this will set the attribute like this
                                        # self.key = value


    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))



junior = Thief("junior", scars=None, favorite_weapon="Wit")

print (junior.sneaky)
print (junior.favorite_weapon)
print(junior.scars)
