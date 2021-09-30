from TDAs.SimpleNode import SimpleNode

class Curso(SimpleNode):

    def __init__(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        super().__init__(codigo)
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio

    def getCodigo(self):
        return self.codigo
    
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCreditos(self):
        return self.creditos
    
    def setCreditos(self, creditos):
        self.creditos = creditos

    def getPreRequisitos(self):
        return self.prerequisitos
    
    def setPreRequisitos(self, prerequisitos):
        self.prerequisitos = prerequisitos
    
    def getObligatorio(self):
        return self.obligatorio
    
    def setObligatorio(self, obligatorio):
        self.obligatorio = obligatorio