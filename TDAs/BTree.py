from TDAs.BPage import BPage

class BTree():
    def __init__(self, degree = 5):
        self.root = BPage(None)
        self.degree = degree

    def add(self, nodo):
        self.root = self._add(nodo, self.root)

    def _add(self, nodo, tmp):
        if tmp.isLeaf():
            tmp.addKey(nodo)
        else:
            found = False
            for i in range(tmp.getSizeKeys()):
                if nodo.getData() < tmp.getKey(i).getData():
                    found = True
                    self._add(nodo, tmp.getBranch(i))
                    break
            if not found:
                self._add(nodo, tmp.getBranch(tmp.getSizeKeys()))
        if tmp.isFull():
            if tmp.getParent() is None:
                r = tmp
                tmp = BPage(None)
                tmp.addKey(r.getCenter())
                tmp.addBranch(0, BPage(tmp))
                tmp.addBranch(1, BPage(tmp))
                tmp.getBranch(0).keys = r.keys[0:int((self.degree)/2)]
                tmp.getBranch(1).keys = r.keys[int((self.degree)/2)+1:]
                if r.fullBranches():
                    x=0
                    for i in range(int(self.degree/2)+1):
                        r.getBranch(i).parent = tmp.getBranch(0)
                        tmp.getBranch(0).addBranch(i, r.getBranch(i))
                    for i in range(int(self.degree/2)+1, self.degree+1):
                        r.getBranch(i).parent = tmp.getBranch(1)
                        tmp.getBranch(1).addBranch(x, r.getBranch(i))
                        x+=1
                    tmp.getBranch(0).leaf = False
                    tmp.getBranch(1).leaf = False
                tmp.leaf = False
            else:
                mkey = tmp.getCenter()
                tmp.getParent().addKey(mkey)
                index = 0
                for index in range(tmp.getParent().getSizeKeys()):
                    if tmp.getParent().getKey(index).getData() == mkey.getData():
                        break
                for i in range(tmp.getParent().getSizeKeys(), index+1, -1):
                    tmp.getParent().addBranch(i, tmp.getParent().getBranch(i-1))
                tmp.getParent().addBranch(index+1, BPage(tmp.getParent()))
                tmp.getParent().getBranch(index+1).keys = tmp.keys[int((self.degree)/2)+1:]
                aux = tmp
                tmp.getParent().addBranch(index, BPage(tmp.getParent()))
                tmp.getParent().getBranch(index).keys = aux.keys[0:int(self.degree/2)]
                if tmp.fullBranches():
                    x=0
                    for i in range(int(self.degree/2)+1):
                        tmp.getBranch(i).parent = tmp.getParent().getBranch(index)
                        tmp.getParent().getBranch(index).addBranch(i, tmp.getBranch(i))
                    for i in range(int(self.degree/2)+1, self.degree+1):
                        tmp.getBranch(i).parent = tmp.getParent().getBranch(index+1)
                        tmp.getParent().getBranch(index+1).addBranch(x, tmp.getBranch(i))
                        x+=1
                    tmp.getParent().getBranch(index).leaf = False
                    tmp.getParent().getBranch(index+1).leaf = False
        return tmp
    
    def get(self, value):
        return self._get(value, self.root)

    def _get(self, value, tmp):
        if tmp:
            found = False
            for i in range(tmp.getSizeKeys()):
                if value == tmp.getKey(i).getData():
                    return tmp.getKey(i)
                if value < tmp.getKey(i).getData():
                    found = True
                    return self._get(value, tmp.getBranch(i))
            if not found:
                return self._get(value, tmp.getBranch(tmp.getSizeKeys()))
        return None

    def show(self):
        self._show(self.root, 0)
    
    def _show(self, tmp, h):
        print(f'Level {h}: {tmp.toCadena()}')
        for i in range(self.degree+1):
            if tmp.getBranch(i) is not None:
                self._show(tmp.getBranch(i), h+1)
    
    def toGviz(self, cadenas):
        self._toGviz(self.root, cadenas)
    
    def _toGviz(self, tmp, cadenas):
        if tmp:
            cadenas.append(f'\nnodo{tmp.toID()} [label="{tmp.toCadena()}"]')
            for i in range(self.degree+1):
                if tmp.getBranch(i) is not None:
                    cadenas.append(f'\nnodo{tmp.toID()} -> nodo{tmp.getBranch(i).toID()}')
                    self._toGviz(tmp.getBranch(i), cadenas)