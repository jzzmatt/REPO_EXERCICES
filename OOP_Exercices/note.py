import datetime

# Store the next available id for all new notes

last_id = 0  # this var are created outside the class, so it will be used as global arg in our class


class Note:
    '''
    Represent a note int the notebook. Match against a string in searches and store tages for each note
    '''

    def __init__(self, memo, tags=' '):
        '''
        Initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id  # we us the global arg
        last_id += 1
        self.id = last_id  # attribuate an arg for last_id

    def match(self, filter):
        '''
        Determine if this note matches the filter text
        Return True if it matches, false otherwise

        Search is case sensitive and matches both text and tags
        '''
        return filter in self.memo or filter in self.tags









        # TESTING  CLASS NOTE
        # n1 = Note("hello first")
        # n2 = Note("hello second")

        # print(n1.match('second'))