class Mynumber(object):
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)

    def __gt__(self, other):
        return int(self) > other

    def __add__(self, other):
        return int(self) + other


    def __radd__(self, other):
        return int(self) + other



mynum = Mynumber(input("Enter your num: "))

print(mynum + 100)
print(20 + mynum)

if mynum > 10 :
    print("the convertion have happened")

else:
    print("Can't be greated")
