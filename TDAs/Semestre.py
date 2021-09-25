from TDAs.SimpleNode import SimpleNode

class Semestre(SimpleNode):
    def __init__(self, data):
        super().__init__(data)
        self.cursos = None
    
    def getCursos(self):
        return self.cursos
    
    def setCursos(self, cursos):
        self.cursos = cursos
