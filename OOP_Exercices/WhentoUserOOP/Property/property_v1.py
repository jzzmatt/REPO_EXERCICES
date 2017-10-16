'''
If we Originally wrote our code to use Directo member Access
We can later add methods to get and set  'name attribute' witout changing the interface
'''

class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name


    def _set_name(self, name):
        if not name:
            raise Exception ("Invalid Name")
        self._name = name


    def _get_name(self):
        return self._name


    name = property(_get_name, _set_name)   #we give the attribute name property, and bind this property to a _set and _get method


#the Property magic method, creates a new attribute on the Color Class named 'name'
#Which now replaces the previous name attribute
#Its sets this attribute to be a property , which calls the 2 methods


c = Color("##0000ff", "bright=red")
print(c.name)
c.name = "red"
print(c.name)
c.name = ''










