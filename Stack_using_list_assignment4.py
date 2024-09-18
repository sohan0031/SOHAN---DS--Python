class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority 

    def __repr__(self):
        return f"Task(description='{self.description}', priority='{self.priority}')"
    
class PriorityStack:
    def __init__(self):
        self.stack = []
        self.priority_map = {'High': [], 'Medium': [], 'Low': []}
    
    def push(self, task):
        self.stack.append(task)
        if task.priority in self.priority_map:
            self.priority_map[task.priority].append(task)

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from an empty stack")
        task = self.stack.pop()
        self.priority_map[task.priority].remove(task)
        return task 

    def display(self):
        for priority in self.priority_map:
            if self.priority_map[priority]:  
                print(f"Priority: {priority}")
                for task in self.priority_map[priority]:
                    print(task)
                  
def main():
    todo_list = PriorityStack()
    todo_list.push(Task("Complete project model", "High"))
    todo_list.push(Task("Schedule team meeting", "Medium"))
    todo_list.push(Task("Review draft presentation", "Low"))
    todo_list.push(Task("Prepare weekly report", "High"))
    todo_list.push(Task("Respond to client emails", "Medium"))

    print("Tasks by Priority:")
    todo_list.display()

    removed_task = todo_list.pop()
    print(f"\nRemoved task: {removed_task}")

    print("\nTasks by Priority after removal:")
    todo_list.display()

if __name__ == "__main__": 
    main()
