'''
We cab also accept arbitrary Keyword arguements
these arrive into the functions as a dictionnary
This tool is commonly used in configuration setups

the __getitem__ method simply allow us to use the new class index syntax
'''

class Options:
    default_options = {
        'port' : 21,
        'host' : 'localhost',
        'username' : None,
        'password' : None,
        'debug' : False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options) #Instead of using the class var, we copy it , so that
        self.options.update(kwargs)                  #each instance , will have it own copy of the class dict



    def __getitem__(self, key):
        return self.options[key]




options = Options(username = "dusty", password = 'drowssap', debug= True)

print(options['debug'])

print(options['port'])


print(options['username'])