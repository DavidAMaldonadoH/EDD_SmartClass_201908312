from TDAs.DoubleNode import DoubleNode
from TDAs.Matrix import Matrix

class Mes(DoubleNode):
    def __init__(self, data):
        super().__init__(data)
        self.tareas = Matrix()

    def getTareas(self):
        return self.tareas
    
    def setTareas(self, tareas):
        self.tareas = tareas