class Document:
    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''


    def insert(self, character):
        self.characters.insert(self.cursor, character)
        self.cursor += 1


    def delete(self):
        del self.characters[self.cursor]




    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()



    def forward(self):
        self.cursor += 1


    def back(self):
        self.cursor -= 1


doc = Document()
doc.filename = 'test_documentpython'
doc.insert('h')
doc.insert('e')
doc.insert('l')
doc.insert('l')
doc.insert('o')
print(doc.characters)
print(''.join(doc.characters))
doc.back()
doc.delete()
doc.insert('p')
print(doc.characters)
print(''.join(doc.characters))




