class CQueue:
    def __init__(self, size):
        self.size = size
        self.list = [None] * size 
        self.front = -1
        self.rear = -1

    def enque(self, num):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.list[self.rear] = num

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        
        temp =  self.list[self.front]
        self.list[self.front] = -1
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else :
            self.front = (self.front + 1) % self.size
            return temp 
        
    def printQ(self):
        if self.front == -1:
            print("Queue is empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.list[i])


Q = CQueue(10)
Q.enque(10)
Q.enque(20)
Q.enque(30)
Q.enque(40)
Q.enque(50)
Q.dequeue()

Q.printQ()
