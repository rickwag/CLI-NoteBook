#to add date to notes
from datetime import datetime

#store the next available id for new note
last_id = 0

class Note:
    ''' Represents a note in the notebook,
    match it to a string during searching
    can be tagged'''

    def __init__(self,memo,tag="",date=None):
        '''initialises a note with a memo and an
        optional tag, it automatically sets the
        creation date and a unique id '''

        self.memo = memo
        self.tag = tag
        self.creation_date = date
        global last_id
        last_id += 1
        self.id = last_id

    def match(self,filter):
        '''returns true if text in filter matches
        the note memo or tag, otherwise returns
        false. (it is case sensitive)'''

        return filter in self.memo or filter in self.tag

class Notebook:
    '''Represents a collection of notes that can
    be tagged, modified and searched'''

    def __init__(self):
        '''initialises a notebook with an empty
        list '''
        self.notes = []
        self.load_file()

    def load_file(self):
        with open("notebook","r") as file:
            for line in file.readlines():
                clean_line = line.strip("\n")
                tag,memo,date = clean_line.split("|")
                self.new_note(memo,tag,date)


    def new_note(self,memo,tag='',date=str(datetime.today().date())):
        '''create a new note and add it to the list'''
        self.notes.append(Note(memo,tag,date))

    def _find_note(self,note_id):
        '''underscore before indicates its for
        internal use only'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self,note_id,memo):
        '''find the note with the given id and
        modify its memo'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def delete_note(self,note_id):
        note = self._find_note(note_id)
        if note is not None:
            self.notes.remove(note)

    def modify_tags(self,note_id,tag):
        '''find the note with the given id and
        modify its tag'''
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.tag = tag
        note = self._find_note(note_id)
        if note:
            note.tag = tag

    def search(self,filter):
        '''find all notes that match the given
        filter string'''

        return [note for note in self.notes if note.match(filter)]
