class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head,data):
   current = head
   new_node = Node(data)
   while current.next is not None :
      current = current.next
   current.next = new_node 
   return head 

def print_list(head):
    current = head
    while current is not None:
        print(f" {current.data}", end="")
        current = current.next
    print("")
 


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
    print("After inserting Nodes at the end:", end="")
    data = 100
    insert_at_end(head, data)
    print_list(head)
