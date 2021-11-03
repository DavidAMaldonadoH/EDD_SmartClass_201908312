from TDAs.AVLNode import AVLNode
from TDAs.DoubleList import DoubleList

class Estudiante(AVLNode):
    def __init__(self, data, carnet, DPI, nombre, carrera, correo, password, creditos, edad):
        super().__init__(data)
        self.carnet = carnet
        self.DPI = DPI
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.listaA = DoubleList()

    def getCarnet(self):
        return self.carnet

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getDPI(self):
        return self.DPI

    def setDPI(self, DPI):
        self.DPI = DPI

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCorreo(self):
        return self.correo

    def setCorreo(self, correo):
        self.correo = correo

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getCreditos(self):
        return self.creditos

    def setCreditos(self, creditos):
        self.creditos = creditos

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getListaA(self):
        return self.listaA

    def setListaA(self, listaA):
        self.listaA = listaA
    
    def addYear(self, year):
        self.listaA.add(year)