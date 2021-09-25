class AVLTree():
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None

    def add(self, nodo):
        self.root = self._add(nodo, self.root)

    def _add(self, nodo, tmp):    
        if tmp is None:
            return nodo
        elif nodo.getData() > tmp.getData():
            tmp.setRight(self._add(nodo, tmp.getRight()))
            if (self.height(tmp.getRight())-self.height(tmp.getLeft()))==2:
                if nodo.getData() > tmp.getRight().getData():
                    tmp = self.rsd(tmp)
                else:
                    tmp = self.rdd(tmp)    
        elif nodo.getData() < tmp.getData():
            tmp.setLeft(self._add(nodo, tmp.getLeft()))
            if (self.height(tmp.getRight())-self.height(tmp.getLeft()))==(-2):
                if nodo.getData() < tmp.getLeft().getData():
                    tmp = self.rsi(tmp)
                else:
                    tmp = self.rdi(tmp)
        else:
            print(f'> Ya se encuentra registrado un Estudiante con el Carnet: {nodo.getData()}')
        heightR = self.height(tmp.getRight())
        heightL = self.height(tmp.getLeft())
        tmp.setHeight(max(heightR, heightL)+1)
        return tmp
    
    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.getHeight()

    def rsi(self, n):
        n1 = n.getLeft()
        n.setLeft(n1.getRight())
        n1.setRight(n)
        n.setHeight(max(self.height(n.getLeft()), self.height(n.getRight()))+1)
        n1.setHeight(max(self.height(n1.getLeft()), n.getHeight())+1)
        return n1

    def rsd(self, n):
        n1 = n.getRight()
        n.setRight(n1.getLeft())
        n1.setLeft(n)
        n.setHeight(max(self.height(n.getLeft()), self.height(n.getRight()))+1)
        n1.setHeight(max(self.height(n1.getLeft()), n.getHeight())+1)
        return n1

    def rdi(self, tmp):
        tmp.setLeft(self.rsd(tmp.getLeft()))
        return self.rsi(tmp)

    def rdd(self, tmp):
        tmp.setRight(self.rsi(tmp.getRight()))
        return self.rsd(tmp)
    
    def get(self, value):
        return self._get(value, self.root)
    
    def _get(self, value, tmp):
        if tmp:
            if tmp.getData() == value:
                return tmp
            elif value > tmp.getData():
                return self._get(value, tmp.getRight())
            else:
                return self._get(value, tmp.getLeft())
        return None

    def delete(self, value):
        self._delete(value, self.root)

    def _delete(self, value, tmp):
        if not tmp:
            return tmp
        elif value > tmp.getData():
            tmp.setRight(self._delete(value, tmp.getRight()))
            if (self.height(tmp.getRight())-self.height(tmp.getLeft()))==2:
                if value > tmp.getRight().getData():
                    tmp = self.rsd(tmp)
                else:
                    tmp = self.rdd(tmp)
        elif value < tmp.getData():
            tmp.setLeft(self._delete(value, tmp.getLeft()))
            if (self.height(tmp.getRight())-self.height(tmp.getLeft()))==(-2):
                if value < tmp.getLeft().getData():
                    tmp = self.rsi(tmp)
                else:
                    tmp = self.rdi(tmp) 
        else:
            if (tmp.getRight() is None):
                tmp2 = tmp.getRight()
                tmp = None  
                return tmp2
            elif (tmp.getLeft() is None):
                tmp2 = tmp.getLeft()
                tmp = None  
                return tmp2
            else:
                tmp2 = self.getLR(tmp.getLeft())
                tmp.setData(tmp2.getData())
                tmp.setCarnet(tmp2.getCarnet())
                tmp.setDPI(tmp2.getDPI())
                tmp.setNombre(tmp2.getNombre())
                tmp.setCarrera(tmp2.getCarrera())
                tmp.setCorreo(tmp2.getCorreo())
                tmp.setPassword(tmp2.getPassword())
                tmp.setCreditos(tmp2.getCreditos())
                tmp.setEdad(tmp2.getEdad())
                tmp.setListaA(tmp2.getListaA())
                tmp.setLeft(self._delete(tmp2.getData(), tmp.getLeft()))
                if (self.height(tmp.getRight())-self.height(tmp.getLeft()))==(-2):
                    if value < tmp.getLeft().getData():
                        tmp = self.rsi(tmp)
                    else:
                        tmp = self.rdi(tmp) 
        if tmp is None:
            return tmp
        heightR = self.height(tmp.getRight())
        heightL = self.height(tmp.getLeft())
        tmp.setHeight(max(heightR, heightL)+1)
        return tmp
    
    def getLR(self, tmp):
        if tmp is None or tmp.getRight() is None:
            return tmp 
        return self.getLR(tmp.getRight())

    def postOrder(self):
        self._postOrder(self.root)

    def _postOrder(self, root):
        if root:
            self._postOrder(root.getLeft())
            self._postOrder(root.getRight())
            print(str(root.getData()) + ' - ', end="")

    def preOrder(self):
        self._preOrder(self.root)
    
    def _preOrder(self, root):
        if root:
            print(str(root.getData()) + ' - ', end="")
            self._preOrder(root.getLeft())
            self._preOrder(root.getRight())
    
    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, root):
        if root:
            self._inOrder(root.getLeft())
            print(str(root.getData()) + ' - ', end="")
            self._inOrder(root.getRight())
    
    def toGviz(self, cadenas):
        self._toGviz(self.root, cadenas)

    def _toGviz(self, tmp, cadenas):
        if tmp:
            cadenas.append(f'\nnodo{tmp.getData()} [label="IZQ* | {tmp.getData()} | DER*"]')
            if tmp.getLeft() is not None:
                cadenas.append(f'\nnodo{tmp.getData()} -> nodo{tmp.getLeft().getData()};')
            if tmp.getRight() is not None:
                cadenas.append(f'\nnodo{tmp.getData()} -> nodo{tmp.getRight().getData()};')
            self._toGviz(tmp.getLeft(), cadenas)
            self._toGviz(tmp.getRight(), cadenas)