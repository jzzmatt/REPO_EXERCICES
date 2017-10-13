'''
Encapsulation , the first Pillar of an OOP
Encapsulation Permit to store Data on a Class
by using a getter & Setter
getter: for get the Data Value
Setter: for set the Data value
'''

class Myclass(object):
    def set_val(self, val):
        '''
        a Setter is characterised by a (self, val)
        self = instance
        
        :param val: the value of the Data
        :return:  and return the new value of the self object
        '''
        self.value = val



    def get_val(self):
        '''
        a Getter is characterised by a way to retreive a Value or Data
        :return: a Value
        '''
        return self.value



a = Myclass()  #Create instance Object
b = Myclass()


a.set_val(10)   #Using a Setter for set the value of the Object
b.set_val(100)

print(a.get_val()) #Using a Getter for retreive the value
print(b.get_val())