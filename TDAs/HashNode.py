from TDAs.SimpleList import SimpleList


class HashNode:
    def __init__(self, data) -> None:
        self.data = data
        self.notes = SimpleList()

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNotes(self):
        return self.notes

    def setNotes(self, notes):
        self.notes = notes

    def addNote(self, nodo):
        self.notes.add(nodo)
