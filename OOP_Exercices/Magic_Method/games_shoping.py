class Games:
    def __init__(self):
        self.gamelist = []


    def add(self, item, *args):
        self.gamelist.append(item)

        for item in args:
            self.gamelist.append(item)


    def __contains__(self, item):
        return item in self.gamelist


    def __iter__(self):
        for item in self.gamelist:
            yield  item

    def __repr__(self):
        return Games.__class__.__name__ + ' ' + type(self.gamelist)


    def __str__(self):
        return ','.join(self.gamelist)




shopgame = Games()

shopgame.add('nintendo', 'playstation', 'sega')

print ('sega' in shopgame)

for item in shopgame:
    print (item)
