from note import Note
from .db import NotesDB

class NotesDAL:
    def __init__(self):
        self._db = NotesDB()

    def insert(self, msg: str) -> Note:
        id = self._db._insert(msg)
        row = self._db._getNoteID(id)
        return(Note(row[0], row[1]))

    def getNoteID(self, id: int) -> Note:
        row = self._db._getNoteID(id)
        if row is not None:
             return(Note(row[0], row[1]))
        else:
            return(None)

    def getNotes(self):
        notes = []
        rows = self._db._getAll()
        for i in rows:
            notes.append(Note(i[0], i[1]))
        return(notes)

    def deleteNote(self, noteId: int) -> Note:
        row = self._db._deleteID(noteId)
        
        if row is not None:
            return(Note(row[0], row[1]))
        else:
            return(None)

    def editNote(self, noteId: int, newMsg: str) -> Note:
        row = self._db._editID(noteId, newMsg)
        
        if row is not None:
            return(Note(row[0], row[1]))
        else:
            return(None)
            