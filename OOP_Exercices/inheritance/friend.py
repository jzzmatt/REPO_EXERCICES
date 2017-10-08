'''
OVERIDDING & SUPER

overidding is altering or replacing a method of the superclass

'''
from contact import Contact

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)   #Super can be call at any point in the method, maybe we
        self.phone = phone     # want to manipulate the incoming paramter before forwarding them the superclass







