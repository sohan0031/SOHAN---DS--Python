class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_index(head, index, data):
    new_node = Node(data)
    if index == 0:
        # Insert at the head
        new_node.next = head
        return new_node

    current = head
    count = 0
    while current is not None and count < index - 1:
        current = current.next
        count += 1
    
    if current is None:
        # Index is out of bounds
        print("Index out of bounds")
        return head

    new_node.next = current.next
    current.next = new_node
    return head

def print_list(head):
    current = head
    while current is not None:
        print(f" {current.data}", end="")
        current = current.next
    print()

if __name__ == "__main__":
    # Create the linked list
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
    data = 100
    index = 2
    print(f"After inserting Node at index {index} :", end="")
    
    head = insert_at_index(head, index, data)  # Insert at the specified index
    print_list(head)
