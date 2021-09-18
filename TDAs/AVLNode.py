class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left
    
    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right
    
    def getHeight(self):
        return self.height
    
    def setHeight(self, height):
        self.height = height