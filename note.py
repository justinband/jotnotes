
class Note:
    # Default Constructor
    def __init__(self, msgId=None, msg=None):
        self._id = msgId
        self._msg = msg

    def printMsg(self):
        print("{}. {}".format(self._id, self._msg))
