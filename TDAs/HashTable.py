from TDAs.HashNode import HashNode


class HashTable:
    def __init__(self, m=7, max=50):
        self.keys = list()
        self.m = m
        self.max = max
        self.size = 0
        for i in range(self.m):
            self.keys.insert(i, HashNode(-1))

    def division(self, k: int):
        return k % self.m

    def quadratic(self, k: int, i: int):
        return (k + i*i) % self.m

    def insert(self, node: HashNode):
        k = self.division(node.getData())
        if self.keys[k].getData() != -1:
            for i in range(self.m):
                k = self.quadratic(k, i)
                if self.keys[k].getData() == -1:
                    break
        self.keys[k] = node
        self.size += 1
        self.rehashing()

    def rehashing(self):
        if ((self.size * 100) / self.m) >= self.max:
            tmp = self.keys[:]
            mprev = self.m
            self.m = self.getNextPrime(mprev)
            self.keys.clear()
            self.size = 0
            for i in range(self.m):
                self.keys.insert(i, HashNode(-1))
            for i in range(mprev):
                if tmp[i].getData() != -1:
                    self.insert(tmp[i])

    def getNextPrime(self, number: int) -> int:
        x = number + 1
        while not self.isPrime(x):
            x += 1
        return x

    def find(self, data) -> HashNode:
        k = self.division(data)
        if self.keys[k].getData() != data:
            for i in range(self.m):
                k = self.quadratic(k, i)
                if self.keys[k].getData() == data:
                    break
        return self.keys[k]

    def isPrime(self, number: int) -> bool:
        for i in range(2, number):
            if number % i == 0:
                return False
        return number > 1

    def imprimir(self):
        for i in range(self.m):
            print(f"{i+1}. {self.keys[i].getData()}")
