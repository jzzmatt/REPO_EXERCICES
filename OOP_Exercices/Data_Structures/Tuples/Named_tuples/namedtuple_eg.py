'''
NamedTuple are Object without behavior

named tuples is a 2 process:
first use Collections.namedtuple to create a class
then crate instances of that class
'''

from collections import namedtuple
'''
The namedtuple constructor accepst 2 args
first is and identifier for the the named tuple
the second arg, represent an attribute followed by a space for enter a third arg and so one
'''
Stock = namedtuple("Stock", "symbol current high low") #This Class can be called just like normal Class
                                                    # Here construct the class with 4 attributes
'''
The Constructor , must have exactly the right number of arg
'''

stock = Stock("GOOG", 613.30, high= 625.86, low= 610.50)

print(stock.high)

'''
Unpack this Object 'stock'
'''
symbol, current, high, low = stock

print(symbol)
print(current)
print(high)

