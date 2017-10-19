'''
len  ; __len__
reversed ; __reversed__()


'''
normal_list = [1, 2, 3, 4, 5]
class CustomSequence():
    def __len__(self):
        return 5


    def __getitem__(self, item):  #this will get , each key on dict, on list, will get any element
        return "x{0}".format(item)  #=> return x1stelement, x2element



class FunkyBackwards(CustomSequence):
    def __reversed__(self):
        return "BACKWARDS! "



for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("\n{}: ".format(seq.__class__.__name__), end='' )

    for item in reversed(seq):
        print(item, end=", ")