class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)





a = AverageList([1, 2, 3, 4])
print(a.average)