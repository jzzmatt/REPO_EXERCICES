#!/usr/bin/python
'''
An Abstract class is a kind of 'Model|template|blue print' for other classes to be defined
It's not designed to construct instances, but can be subclassed by regular classes
An abstract classes can define an Interface, or methods that must be implemented by its subclasses
'''


import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def set_val(self, input):
        '''Set a value in the instance'''
        return


    @abc.abstractmethod
    def get_val(self):
        '''Get and return a value from instance'''
        return




class Myclass(GetterSetter):
    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val



x = Myclass()
print(x)