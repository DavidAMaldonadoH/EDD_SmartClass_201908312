from TDAs.DoubleNode import DoubleNode
from TDAs.SimpleList import SimpleList
from TDAs.DoubleList import DoubleList

class Year(DoubleNode):
    def __init__(self, data):
        super().__init__(data)
        self.semestres = SimpleList()
        self.meses = DoubleList()

    def getMeses(self):
        return self.meses

    def setMeses(self, meses):
        self.meses = meses

    def getSemestres(self):
        return self.semestres

    def setSemestres(self, semestres):
        self.semestres = semestres
    
