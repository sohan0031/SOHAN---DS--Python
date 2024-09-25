class Node:
    def __init__(self, cust_id, cust_name, service):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.service = service
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None 

    def Enqueue(self, cust_id, cust_name, service):
        new_entry = Node(cust_id, cust_name, service)
        if self.rear is None:
            self.front = self.rear = new_entry
        else:
            self.rear.next = new_entry
            self.rear = new_entry

    def Dequeue(self):
        if self.front is None:
            print("No Customer in Queue")
            return None 
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None  
            return temp
        
    def total_req(self):
        count = 0 
        current = self.front 
        while current is not None:
            count += 1
            current = current.next 
        print(count)

    def req_in_process(self):
        return f"ID: {self.front.cust_id}, Name: {self.front.cust_name}, Service: {self.front.service}"

    def print_queue(self):
        current = self.front
        if current is None:
            print("The queue is empty.")
            return
        while current is not None:
            print(f"ID: {current.cust_id}, Name: {current.cust_name}, Service: {current.service}")
            current = current.next

def menu():
    queue = Queue()
    while True:
        print("\nMenu:")
        print("1. Add Customer Request ")
        print("2. Delete Customer Request ")
        print("3. Print Requests Queue")
        print("4. Total Requests")
        print("5. Request in Process")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            cust_id = input("Enter Customer ID: ")
            cust_name = input("Enter Customer Name: ")
            service = input("Enter Service: ")
            queue.Enqueue(cust_id, cust_name, service)
            print(f"Customer {cust_name} added to the queue.")

        elif choice == '2':
            customer = queue.Dequeue()
            if customer:
                print(f"Customer {customer.cust_name} has been served.")

        elif choice == '3':
            print("Current Queue:")
            queue.print_queue()

        elif choice == '4':
            print("Total Pending Requests:",end="")
            queue.total_req()

        elif choice =="5":
            pass

        elif choice == '6':
            print("Exiting..........")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
