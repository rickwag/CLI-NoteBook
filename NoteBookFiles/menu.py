import sys
from NoteBook import Notebook

class Menu:
    '''Displays a menu and responds to choices
    when run'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1" : self.show_notes,
            "2" : self.search_notes,
            "3" : self.add_note,
            "4" : self.modify_note,
            "5" : self.delete_note,
            "6" : self.quit
        }

    def display_menu(self):
        print("""
        NoteBook Menu
        
        1. Show all Notes
        2. Search all NOtes
        3. Add Note
        4. Modify Note
        5. Delete Note
        6. Quit
        """)

    def run(self):
        '''
        display the menu and respond to choices
        '''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self,notes = None):
        if notes is None:
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id,note.tag,note.memo
            ))

    def search_notes(self):
        filter = input("search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tag = input("Enter a tag: ")
        self.notebook.new_note(memo,tag)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter note id: ")
        memo = input("Enter memo: ")
        tag = input("Enter tag: ")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tag:
            self.notebook.modify_tags(id,tag)

    def delete_note(self):
        note_id = input("Enter note id: ")
        self.notebook.delete_note(note_id)
        print("Note {} deleted!".format(note_id))

    def quit(self):
        print("Thank you for using your notebook"
              " today.")
        self.update_file()
        sys.exit(0)

    def update_file(self):
        with open("notebook", "w") as file:
            for value in self.notebook.notes:
                file.write(value.tag + "|" + value.memo + "|" + value.creation_date + "\n")


if __name__ == "__main__":
    Menu().run()

