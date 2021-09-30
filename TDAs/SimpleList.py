class SimpleList():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def getSize(self):
        return self.size
    
    def add(self, nodo):
        if self.head == None:
            self.head = nodo
            self.size+=1
        else:
            if self.find(nodo.getData()) is None:
                if (nodo.getData() < self.head.getData()):  # Si el nuevo nodo es menor a la head
                    nodo.setNext(self.head)
                    self.head = nodo
                else:
                    nodo_aux = self.head
                    while nodo_aux.getNext() is not None:
                        if (nodo.getData() < nodo_aux.getNext().getData()):  # Si el valor del nuevo nodo es menor al siguiente del actual
                            nodo.setNext(nodo_aux.getNext())  # El siguiente del nuevo va a ser el siguiente del actual
                            nodo_aux.setNext(nodo)  # el siguiente del actual va a ser el nuevo
                            break
                        nodo_aux = nodo_aux.getNext()
                    if (nodo_aux.getNext() is None):  # Si el siguiente del actual es None es porque nuevo va a ser el ultimo
                        nodo_aux.setNext(nodo)
                self.size += 1
    
    def get(self, i):
        index = 0
        nodo_aux = self.head
        if i > self.size | i < 0:
            return None
        while nodo_aux is not None:
            if index == i:
                return nodo_aux
            nodo_aux = nodo_aux.getNext()
            index+=1
        return None

    
    def find(self, value):
        for i in range(self.size):
            if (self.get(i).getData() == value):
                return self.get(i)
        return None

    def delete(self, value):
        nodo_aux = self.find(value)
        if nodo_aux is not None:
            if nodo_aux is self.head:
                if self.size != 1:
                    tmp = nodo_aux.getNext()
                    self.head = tmp
                else:
                    self.head = None
            else:
                tmp = self.head
                while tmp.getNext().getData() != value:
                    tmp = tmp.getNext()
                tmp.setNext(nodo_aux.getNext())
                nodo_aux.setNext(None)
            self.size-=1
            del nodo_aux
        else:
            print('El nodo no existe')

    def imprimir(self):
        for i in range(self.size):
            print(self.get(i).getData())