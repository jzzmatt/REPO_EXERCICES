class YourList(list):
    def __init__(self):
        super().__init__()

    def append(self, item):
        new_item = ''
        for l in item:
            if l in 'aieo':
                l = 'X'
                new_item += l
            else:
                new_item += l

        super().append(new_item)

mylist = YourList()

mylist.append("lion")

print(mylist)