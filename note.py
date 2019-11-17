
class Note:
    # Default Constructor
    def __init__(self, msg=None, msgId=None):
        self._msg = msg
        self._id = msgId

    def printMsg(self):
        print("{}. {}".format(self._id, self._msg))
        