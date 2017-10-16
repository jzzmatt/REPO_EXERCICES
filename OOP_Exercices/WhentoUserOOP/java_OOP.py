'''
ON Java, they suppose that any attributes can't be accessed directly
You should use a proxy fct to access attribute as setter ang getter method (Encapsulation)
the value are prefixed with '_' to indicate that they are private


We can use in Python , Property decorator, to make look method like attribute
'''

class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name


    def set_name(self, name):
        self._name = name



    def get_name(self):
        return self._name





c = Color("#ff0000", "bright red")
print(c.get_name())
c.set_name("red")
print(c.get_name())


