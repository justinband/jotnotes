import argparse

from note import Note

def createNote():
    print("---- Creating Note ----")

def viewNotes():
    print("---- View Notes ----")

def deleteNote(noteId: int):
    print("---- Deleting Note #{} ----".format(noteId))

def editNote(noteId: int):
    print("---- Edit Note #{} ----".format(noteId))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--view", help="View all notes", action="store_true") # Shows user all the notes
    parser.add_argument("-c", "--create", help="Create a note", action="store_true") # Will allow user to type until ENTER pressed
    parser.add_argument("-d", "--delete", help="Delete a note by id") # Delete a note
    parser.add_argument("-e", "--edit", help="Edit a note by id") # Edit a note, give an id!
    args = parser.parse_args()
   
    if args.view:
        viewNotes()
    if args.create:
        createNote()
    if args.delete:
        deleteNote(args.delete)
    if args.edit:
        editNote(args.edit)
