class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev