import psycopg2

class NotesDB:
    def __init__(self):
        self._db = psycopg2.connect(dbname="jotnotes", host="localhost", user="postgres", password="postgres")
        self._cur = self._db.cursor()

    def _execute(self, query: str, params=None):
        self._cur.execute(query, params)
        self._db.commit() # Update database


    def _insert(self, msg: str):
        '''
            Insert a message into the db
        '''

        query = """
            INSERT INTO notes (note) VALUES (%(msg)s);
        """
        params = {
            'msg': msg
        }
        self._execute(query, params)
        row = self._getNoteRecent()

        return(row)

    def _getAll(self):
        '''
            Get ALL notes!
        '''
        
        query = """
            SELECT * FROM notes;
        """
        self._execute(query)
        rows = self._cur.fetchall()
        return(rows)

    def _getNoteRecent(self):
        '''
            Get most recent note
            Used right after inserting (_insert) to return the row
        '''

        query = """
            SELECT * FROM notes WHERE id=(
                SELECT MAX(id) FROM notes
            );
        """
        self._execute(query)
        row = self._cur.fetchone()
        return(row)

    def _getNoteID(self, id: int):
        query = """
            SELECT * FROM notes WHERE id=%(id)s;
        """
        params = {
            'id': id
        }
        self._execute(query, params)
        row = self._cur.fetchone()
        return(row)
        