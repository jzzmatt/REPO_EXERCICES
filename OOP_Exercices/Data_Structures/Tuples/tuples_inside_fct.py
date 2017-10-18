import datetime

def middle(stock, date):
    symbol, current, high, low = stock  #We unpacking or decompress all the value inside stock
    return (((high + low) /2), date)    #into 4 various value (symbol,current,high,low)



mid_value, date = middle(("GOOG", 613.30, 625.86, 610.50), datetime.date(2010, 1, 6))


print(mid_value)
print(date)