class Node:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        self.next = None  

class StackLL:
    def __init__(self):
        self.head = None 

    def push(self, task, priority):
        new_node = Node(task, priority)
        new_node.next = self.head  
        self.head = new_node     
        print("Task Added to List")
        
    def pop(self):
        if self.head is None:
            print("Stack is empty.")
            return None
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None  
        print("task is Popped out ")
        return popped_node.task, popped_node.priority
    
    def peek(self):
        if self.head is None:
            print("Stack is empty.")
            return None
        
        print(f"Task at top is {self.head.task} having Priority {self.head.priority})")
        return self.head.task, self.head.priority

    def print_list(self):
        current = self.head
        if current is None:
            print("Stack is empty.")
        else:
            while current:
                print(f"{current.task} (Priority: {current.priority})", end="\n")
                current = current.next
            print("None")

stack = StackLL()
while True:
    action = input("Enter push , pop , peek , display or exit : ")
    
    if action == 'push':
        task = input("Enter Task: ")
        priority = input("Enter Priority: ")
        stack.push(task, priority)
    elif action == 'pop':
        stack.pop()
    elif action == 'peek' :
        stack.peek()
    elif action == 'display':
        stack.print_list()
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please try again.")
