class BPage():
    def __init__(self, parent):
        self.parent = parent
        self.leaf = True
        self.degree = 5
        self.keys = []
        self.branches = []
        for i in range(self.degree+1):
            self.branches.insert(i, None)

    def isLeaf(self):
        return self.leaf
    
    def getParent(self):
        return self.parent

    def getCenter(self):
        return self.keys[int(self.degree/2)]
    
    def getSizeKeys(self):
        return len(self.keys)

    def isFull(self):
        return len(self.keys) == self.degree
    
    def fullBranches(self):
        return all([b is not None for b in self.branches])
    
    def addKey(self, nodo):
        self.keys.append(nodo)
        self.keys.sort(key=lambda x: x.getData())
    
    def getKey(self, i):
        return self.keys[i]

    def addBranch(self, pos, nodo):
        self.branches[pos] = nodo

    def getBranch(self, i):
        return self.branches[i]
    
    def toCadena(self):
        label = ''
        for i in range(len(self.keys)):
            if i != len(self.keys)-1:
                label+=f'{self.keys[i].getData():03}\\n{self.keys[i].getNombre()}| |'
            else:
                label+=f'{self.keys[i].getData():03}\\n{self.keys[i].getNombre()}'
        return label
    
    def toID(self):
        label = ''
        for i in range(len(self.keys)):
            label+=f'{self.keys[i].getData():03}'
        return label
    