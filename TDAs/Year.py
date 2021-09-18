from TDAs.DoubleNode import DoubleNode

class Year(DoubleNode):
    def __init__(self, data):
        super().__init__(data)
        self.semestres = None
        self.meses = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getSemestres(self):
        return self.semestres

    def setSemestres(self, semestres):
        self.semestres = semestres
    
