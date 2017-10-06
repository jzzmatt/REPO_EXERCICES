from note import Note


class Notebook:
    '''
    Represent a Collection of notes that can be tagged, modified and searched
    '''

    def __init__(self):
        '''
        Initialize a notebook with an empty list, which in future will hold the note
        '''
        self.notes = []


    def new_note(self, memo, tags= ''):
        '''
        
        :param memo: Create a new note and add it to the list
        :param tags: tags will still '' at this stage 
        we append instance or Obj of the Class Note
        '''
        self.notes.append(Note(memo, tags))


    def _find_note(self, note_id):
        '''
        Locate the note with the given id
        :param note_id: 
        :return:  the note
        '''
        for note in self.notes:
            if note.id == note_id:
                return note   #Return the object or instance
        return None   # if doesnt' find nothing return None


    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its memo to the given value
        '''
        #for note in self.notes:
         #   if note.id == note_id:  #we compare the note.id from the imported class Note
          #      note.memo = memo
           #     break
        self._find_note(note_id).memo = memo


    def modify_tags(self, note_id, tags):
        '''
        Find the note with the giveb id and change its tags to the given value
        :param note_id: 
        :param tags: 
        :return: 
        '''
        #for note in self.notes:
        #    if note.id == note_id:
        #        note.tags = tags
         #       break

        self._find_note(note_id).tags = tags



    def search(self, filter):
        '''
        Find all notes that match the given filter string 
        :param filter: 
        :return: the list of note, here , we look inside note method for match method 'note.match(filter)
        '''
        return [note for note in self.notes if note.match(filter)]









'''

#TESTING
n = Notebook()
n.new_note("yes i love it")
n.new_note("this is my second though")
n.new_note("Basket i love ")
n.modify_memo(1, "yes i love Python")  #Update the first note id
n.modify_memo(3, "Football also")


print(n.notes)

print(n.notes[0].memo)  #Access the list of note
print(n.notes[1].memo)
print(n.notes[2].memo)

print(n.search("second"))
print(n.search("Python"))
print(len(n.notes))
'''


