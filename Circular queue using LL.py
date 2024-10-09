class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None

class Circular_Que :
    def __init__(self) :
        self.front = None
        self.rear = None

    def Enque(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def Deque(self):
        if self.front is None:
            print("Queue is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def printQ(self):
        if self.front is None:
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.data, end='\n')
            current = current.next
            if current  == self.front:
                break

Q = Circular_Que()
Q.Enque(10)
Q.Enque(20)
Q.Enque(30)
Q.Enque(40)
Q.Enque(50)
Q.Deque()

Q.printQ()
