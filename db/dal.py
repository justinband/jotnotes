from typing import List

from note import Note
from .db import NotesDB

class NotesDAL:
    def __init__(self):
        self._db = NotesDB()

    def insert(self, msg: str) -> Note:
        print("DAL Insert")
        note = self._db._insert("notes", msg)
        return(note)

    def viewNotes(self) -> List:
        print("DAL View")
        rows = self._db._getAll()
        print(rows)

    def deleteNote(self, noteId: int) -> Note:
        print("DAL Delete")

    def editNote(self, noteId: int, newMsg: str) -> Note:
        print("DAL View")
