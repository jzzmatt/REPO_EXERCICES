stocks = {
    'GOOG' : (613.30, 625.86, 610.50),
    'MSFT' : (30.25, 30.70, 30.19)

}


print(stocks["GOOG"])

''' --get-- method on dic
the get method accepts a key as the first parameter and and optional value if the key doesnt' exist
'''

print(stocks.get("RIM"))  #as RIM doesnt' exit, we will receive a NONE key
                          #we can handle this error as second parameter of get


print(stocks.get("RIM", "NOT FOUND"))

'''
setdefault method
this method will only sets a value in the Dictionnary only if that value has not previously been set
Ohterwise, it return the previous setting key
Basically set a default key to a key
'''

print(stocks.setdefault("GOOG", "Invalid"))

print(stocks.setdefault("RIM", (67.38, 68.48, 67.28)))

print(stocks["RIM"])


for stock, value in stocks.items():
    print ("{} las value is {}".format(stock, value[0]))

