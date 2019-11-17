#!/usr/bin/env python3

import argparse

from db.dal import NotesDAL
from note import Note

def createNote():
    """
        Prompt user to input a message for their note
        Enters the message into the database via DAL

        Output: Show outpt with id attached
    """
    print("---- Creating Note ----")
    dal = NotesDAL()

    msg = input("Enter your note: \n")

    # Enter note into database
    #   Get Note obj back
    note = dal.insert(msg)
    print("\nNote #{} Inserted succesfully".format(note._id))

def viewNotes():
    print("---- View Notes ----")

    # Query database via DAL
    dal = NotesDAL()
    allNotes = dal.getNotes()

    # Output all notes in nice format
    for note in allNotes:
        note.printMsg()

def deleteNote(noteId: int):
    """
        Remove a note database given the note id

        Output: Show deleted message upon deletion
    """
    print("---- Deleting Note #{} ----".format(noteId))

    # Make deletion call to DB
    dal = NotesDAL()
    delNote = dal.deleteNote(noteId)

    # Output deleted note
    if delNote is not None:
        print("Deleted...\n")
        delNote.printMsg()
    else:
        print("Note #{} does not exist".format(noteId))

def editNote(noteId: int):
    """
        Change message of note given the note id

        Output: Show original message -> Show edited message
    """
    print("---- Edit Note #{} ----".format(noteId))

    dal = NotesDAL()

    # Query DB to get original note
    oldNote = dal.getNoteID(noteId)
    if oldNote is not None:
        # Query DB to change note
        newMsg = input("Change message to: ")
        editNote = dal.editNote(noteId, newMsg)

        if editNote is not None:
            # Show user changes made to the note
            print("\nOld:")
            oldNote.printMsg()
            print("\nNew:")
            editNote.printMsg()
        else:
            print("Failed to change message...")
    else:
        print("Note #{} does not exist".format(noteId))

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
