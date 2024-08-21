class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_front(head,data):
   new_node = Node(data)
   new_node.next = head
   return new_node

def print_list(head):
    current = head
    while current is not None:
        print(f" {current.data}", end="-->")
        current = current.next
    print()
 
if __name__ == "__main__":

    N1 = Node(10) 
    N2 = Node(20) 
    N3 = Node(30) 
    N4 = Node(40) 

    N1.next = N2
    N2.next = N3
    N3.next = N4
    head = N1

    print("Original Linked List:", end="")
    print_list(head)
    print("After inserting Nodes at the front :", end="")
    
    head = insert_at_front(head, 50)
    
    print_list(head)
