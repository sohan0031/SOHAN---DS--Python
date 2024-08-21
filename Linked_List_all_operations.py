class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def insert_at_front(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_index(head, index, data):
    new_node = Node(data)
    if index == 0:
        return insert_at_front(head, data)

    current = head
    count = 0
    while current is not None and count < index - 1:
        current = current.next
        count += 1
    
    if current is None:
        print("Index out of bounds")
        return head

    new_node.next = current.next
    current.next = new_node
    return head

def remove_at_index(head, index):
    if head is None:
        print("The list is empty")
        return head

    if index == 0:
        # Remove the head node
        return head.next

    current = head
    count = 0
    while current is not None and count < index - 1:
        current = current.next
        count += 1
    
    if current is None or current.next is None:
        print("Index out of bounds")
        return head

    current.next = current.next.next
    return head

def print_list(head):
    current = head
    while current is not None:
        print(f" {current.data}", end="")
        current = current.next
    print()

def create_linked_list_from_input():
    n = int(input("Enter the number of nodes in the linked list: "))
    if n == 0:
        return None

    data = int(input("Enter the data for node 1: "))
    head = Node(data)
    current = head

    for i in range(1, n):
        data = int(input(f"Enter the data for node {i + 1}: "))
        current.next = Node(data)
        current = current.next

    return head

if __name__ == "__main__":
    head = create_linked_list_from_input()
    
    print("Original Linked List:", end="")
    print_list(head)

    while True:
        print("\nChoose an operation:")
        print("1. Insert at end")
        print("2. Insert at front")
        print("3. Insert at index")
        print("4. Remove at index")
        print("5. Print list")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the data for the new node: "))
            head = insert_at_end(head, data)
        elif choice == 2:
            data = int(input("Enter the data for the new node: "))
            head = insert_at_front(head, data)
        elif choice == 3:
            index = int(input("Enter the index where you want to insert the new node: "))
            data = int(input("Enter the data for the new node: "))
            head = insert_at_index(head, index, data)
        elif choice == 4:
            index = int(input("Enter the index of the node you want to remove: "))
            head = remove_at_index(head, index)
        elif choice == 5:
            print("Linked List:", end="")
            print_list(head)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
