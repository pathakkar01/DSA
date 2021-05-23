class minHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*(self.maxsize+1)
        self.heap[0] = float("-inf")
    def parent(self, pos):
        return pos // 2
    def leftChild(self, pos):
        return 2*pos
    def rightChild(self, pos):
        return 2*pos +1
    def isLeaf(self, pos):
        if pos > (self.size//2) and pos <= self.size:
            return True
        return False
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def insert(self, ele):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = ele

        curr = self.size

        while self.heap[curr] < self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
    def heapify(self, pos):
        
        if not self.isLeaf(pos):
            print(self.heap , "k")
            if self.heap[pos] > self.heap[self.leftChild(pos)] or  self.heap[pos] > self.heap[self.rightChild(pos)]:
                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                    print(0)
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                else:
                    print(1)
                    self.swap(pos,self.rightChild(pos))
                    self.heapify(self.rightChild(pos))
    def delete(self):
        delEle = self.heap[1]
        self.heap[1] = self.heap[self.size]
        
        self.heap[self.size] = float("inf")
        self.size -=1
        self.heapify(1)
        print(self.heap)
        return delEle
    def sort(self):
        s = []
        for i in range(self.size):
            #print(self.heap)
            s.append(MH.delete())
        return s

MH = minHeap(15)
MH.insert(51)
MH.insert(31)
MH.insert(27)
MH.insert(19)
MH.insert(15)
MH.insert(11)
MH.insert(8)
MH.insert(0)
print(MH.heap, "d")
print(MH.delete(), MH.heap)
print(MH.delete())

print(MH.heap)
print(MH.sort())


