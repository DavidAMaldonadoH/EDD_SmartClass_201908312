from TDAs.DoubleList import DoubleList
from TDAs.MatrixNode import MatrixNode
from TDAs.HeaderNode import HeaderNode

class Matrix():
    def __init__(self):
        self.horas = DoubleList() #filas
        self.dias = DoubleList()  #columnas
    
    def add(self, row, column, tareas):
        nuevo = MatrixNode(row, column, tareas)
        #incersion por filas
        eHora = self.horas.find(row)
        if eHora is None:
            eHora = HeaderNode(row)
            eHora.setAccessNode(nuevo)
            self.horas.add(eHora)
        else:
            if nuevo.getColumn() < eHora.getAccessNode().getColumn():
                nuevo.setNext(eHora.getAccessNode())
                eHora.getAccessNode().setPrev(nuevo)
                eHora.setAccessNode(nuevo)
            else:
                actual = eHora.getAccessNode()
                while actual.getNext() is not None:
                    if nuevo.getColumn() < actual.getNext().getColumn():
                        nuevo.setNext(actual.getNext())
                        actual.getNext().setPrev(nuevo)
                        nuevo.setPrev(actual)
                        actual.setNext(nuevo)
                        break
                    actual = actual.getNext()
                if actual.getNext() is None:
                    actual.setNext(nuevo)
                    nuevo.setPrev(actual)
        #incersion por columnas
        eDia = self.dias.find(column)
        if eDia is None:
            eDia = HeaderNode(column)
            eDia.setAccessNode(nuevo)
            self.dias.add(eDia)
        else:
            if nuevo.getRow() < eDia.getAccessNode().getRow():
                nuevo.setBottom(eDia.getAccessNode())
                eDia.getAccessNode().setTop(nuevo)
                eDia.setAccessNode(nuevo)
            else:
                actual = eDia.getAccessNode()
                while actual.getBottom() is not None:
                    if nuevo.getRow() < actual.getBottom().getRow():
                        nuevo.setBottom(actual.getBottom())
                        actual.getBottom().setTop(nuevo)
                        nuevo.setTop(actual)
                        actual.setBottom(nuevo)
                        break
                    actual = actual.getBottom()
                if actual.getBottom() is None:
                    actual.setBottom(nuevo)
                    nuevo.setTop(actual)
    
    def get(self, row, column):
        hora = self.horas.find(row)
        if hora:
            actual = hora.getAccessNode()
            while actual is not None:
                if actual.getColumn() == column:
                    return actual
                actual = actual.getNext()
        return None

    def printMatrix(self):
        print("   ", end=" | ")
        for j in range(self.dias.getSize()):
            print(f"{self.dias.get(j).getData():03}", end=" | ")
        print()
        for i in range(self.horas.getSize()):
            hora = self.horas.get(i).getData()
            print(f"{hora:03}", end=" | ")
            for j in range(self.dias.getSize()):
                dia = self.dias.get(j).getData()
                if self.get(hora, dia) is None:
                    print('   ', end=" | ")
                else:
                    print(f"{self.get(hora, dia).getTareas():03}", end=" | ")
            print()