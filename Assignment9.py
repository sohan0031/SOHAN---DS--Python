class Node :
    def __init__(self,order_id,cust_name,items) :
        self.order_id = order_id
        self.cust_name = cust_name
        self.items = items
        self.next = None

class Fast_Food:
    def __init__(self) :
        self.front = None
        self.rear = None

    def take_order(self,order_id,cust_name,items):
        new_order = Node(order_id,cust_name,items)
        if self.rear is None:
            self.front = self.rear = new_order
            self.rear.next = self.front
        else:
            self.rear.next = new_order
            self.rear = new_order
            self.rear.next = self.front

    def Process_order(self):
        if self.front is None:
            print("Order Queue is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = self.front.next
            self.rear.next = self.front
            return temp.order_id 

    def printQ(self):
        if self.front is None:
            print(" Order Queue is empty")
            return
        current = self.front
        while current:
            print(f"Order ID : {current.order_id}\nCustomer Name:{current.cust_name}\nItems Order:{current.items}")
            print("")
            current = current.next
            if current  == self.front:
                break
            
F = Fast_Food()

while True :
    print("Menu :")
    print("1.Place Order ")
    print("2.Process Order ")
    print("3.Display Orders ")
    print("4.Exit ")
    print("")
    
    choice = int(input("Enter Your Choice :"))
    if choice == 1 :
        order_id= int(input("Enter Order Id :"))
        cust_name  = input("Enter Customer Name :")
        items = (input("Enter Items To order :"))
        F.take_order(order_id,cust_name,items)
        print("Order Added Succesfully..........")
        print("")
    
    elif choice == 2 :
        a = F.Process_order()
        print(f"Order with ID {a} Comleted Succesfully...............")
        print("")
        
    elif choice ==3   :
        print("\nOrders in Queue : ")
        F.printQ()
        print("")
        
    elif choice == 4 :
        print("Exiting ..............")
        break
    
    else :
        print("Enter Valid Choice......................")
        
    
