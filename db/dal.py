from note import Note
from .db import NotesDB

class NotesDAL:
    def __init__(self):
        self._db = NotesDB()

    def insert(self, msg: str) -> Note:
        print("DAL Insert")
        note = self._db._insert(msg)
        return(note)

    def getNotes(self):
        notes = []
        rows = self._db._getAll()
        for i in rows:
            notes.append(Note(i[0], i[1]))
        return(notes)

    def deleteNote(self, noteId: int) -> Note:
        print("DAL Delete")

    def editNote(self, noteId: int, newMsg: str) -> Note:
        print("DAL View")
