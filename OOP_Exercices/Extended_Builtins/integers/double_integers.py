class Double(int):
    def __new__(cls, *args, **kwargs):
        self = int.__new__(cls, *args, **kwargs)
        return self * 2



print(Double(5))