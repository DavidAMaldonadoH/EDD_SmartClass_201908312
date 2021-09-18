from TDAs.SimpleNode import SimpleNode

class Tarea(SimpleNode):
    def __init__(self, id, carnet, nombre, descripcion, materia, fecha, hora, estado):
        super().__init__(id)
        self.id = id
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
    
    def getCarnet(self):
        return self.carnet

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def getMateria(self):
        return self.materia
    
    def setMateria(self, materia):
        self.materia = materia
    
    def getFecha(self):
        return self.fecha
     
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def getHora(self):
        return self.hora
    
    def setHora(self, hora):
        self.hora = hora

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado