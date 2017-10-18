class ReversedStr(str):
    def __new__( *args, **kwargs):
        obj = str.__new__(*args, **kwargs) #forward the an element to the str class
        obj  = obj[::-1]  #reverse this  str return
        return obj



reverstr = ReversedStr('junior')

print(reverstr)