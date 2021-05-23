class queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.queue = [None] * self.capacity
    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False
    def isFull(self):
        if (self.rear+1) % self.capacity == self.front:
            return True
        return False
    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full")
        self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] =  data
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        self.front = (self.front+1) % self.capacity
        temp = self.queue[self.front]
        self.queue[self.front] = None
        return temp

q = queue(8)
q.enqueue(10)
q.enqueue(56)
q.enqueue(23)
q.enqueue(9)
q.enqueue(30)
q.enqueue(17)
print(q.queue)
print(q.isFull())
print(q.dequeue())
print(q.queue)