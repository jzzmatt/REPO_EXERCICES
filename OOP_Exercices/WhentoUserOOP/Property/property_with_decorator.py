'''
Property Decorators
'''

class Silly:

    @property          #first we Decorate the foo method as getter
    def silly(self):
        "This is a silly property "
        print("You are getting silly")
        return self._silly


    @silly.setter         #Then, we decorate a new method wich exactly the same name with setter
    def silly(self, value):
        self._silly = value



    @silly.deleter
    def silly(self):
        print("Whoa, you killed silly !")
        del self._silly






