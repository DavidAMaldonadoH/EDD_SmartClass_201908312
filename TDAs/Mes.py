from TDAs.DoubleNode import DoubleNode

class Mes(DoubleNode):
    def __init__(self, data):
        super().__init__(data)
        self.tareas = None

    def getTareas(self):
        return self.tareas
    
    def setTareas(self, tareas):
        self.tareas = tareas