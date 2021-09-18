class MatrixNode:
    def __init__(self, row, column, tareas):
        self.row = row
        self.column = column
        self.tareas = tareas
        self.next = None
        self.prev = None
        self.top = None
        self.bottom = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def setTop(self, top):
        self.top = top

    def getTop(self):
        return self.top

    def setBottom(self, bottom):
        self.bottom = bottom

    def getBottom(self):
        return self.bottom

    def setTareas(self, tareas):
        self.tareas = tareas

    def getTareas(self):
        return self.tareas
    
    def getColumn(self):
        return self.column
    
    def getRow(self):
        return self.row