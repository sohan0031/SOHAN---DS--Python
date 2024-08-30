class Patient:
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition
        self.next = None

class Patient_List:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def is_empty(self):
        return self.head is None

    def add_patient(self, name, condition):
        new_patient = Patient(name, condition)
        if self.is_empty():
            self.head = self.tail = new_patient
        else:
            self.tail.next = new_patient
            self.tail = new_patient
        print(f"Patient {name} added to the queue.")

    def remove_patient(self, name):
        if self.is_empty():
            print("No patients to remove.")
            return None
        
        current = self.head
        previous = None

       
        if current is not None and current.name == name:
            self.head = current.next
            if self.head is None:
                self.tail = None
            print(f"Patient {current.name} removed from the queue.")
            return current

        while current is not None and current.name != name:
            previous = current
            current = current.next

        if current is None:
            print(f"Patient {name} not found in the queue.")
            return None

     
        previous.next = current.next
        if current == self.tail:
            self.tail = previous
        print(f"Patient {current.name} removed from the queue.")
        return current

    def display_queue(self):
        current = self.head
        if self.is_empty():
            print("No patients in the queue.")
            return
        print("Current Patient Queue:")
        while current is not None:
            print(f"Name: {current.name}, Condition: {current.condition}")
            current = current.next

    def search_patient(self, name):
        current = self.head
        while current is not None:
            if current.name == name:
                print(f"Patient found: Name: {current.name}, Condition: {current.condition}")
                return current
            current = current.next
        print(f"Patient {name} not found in the queue.")
        return None

    def update_patient_info(self, name, condition=None):
        patient = self.search_patient(name)
        if patient:
            if condition is not None:
                patient.condition = condition
            print(f"Updated patient info: Name: {patient.name}, Condition: {patient.condition}")

def main():
    queue = Patient_List()
    
    while True:
        command = input("Enter command (add, remove, search, view, exit): ").strip().lower()
        
        match command:
            case "add":
                name = input("Enter patient's name: ")
                condition = input("Enter patient's condition: ")
                queue.add_patient(name, condition)
            case "remove":
                name = input("Enter patient's name to remove: ")
                queue.remove_patient(name)
            case "search":
                name = input("Enter patient's name to search: ")
                queue.search_patient(name)
            case "view":
                queue.display_queue()
            case "exit":
                print("Exiting the patient management system.")
                break
            case _:
                print("Invalid command. Please enter add, remove, search, view, or exit.")

if __name__ == "__main__":
    main()
