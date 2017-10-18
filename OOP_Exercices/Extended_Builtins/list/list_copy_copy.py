import copy

class Filledlist(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()  #forward nothing to the super list, so we obtain a new list

        for _ in range(count):
            self.append(copy.copy(value))





fl1 = Filledlist(9, 2)  #i want a 9 time a copy of 2
fl2 = Filledlist(2, [1,2,3])


print(len(fl1))
print(fl1)

print(len(fl2))
print(fl2)