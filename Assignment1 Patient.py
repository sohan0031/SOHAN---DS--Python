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

    def remove_patient(self):
        if self.is_empty():
            print("No patients to remove.")
            return None
        removed_patient = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        print(f"Patient {removed_patient.name} removed from the queue.")
        return removed_patient


    def display_queue(self):
        current = self.head
        if self.is_empty():
            print("No patients in the queue.")
            return
        print("Current Patient Queue:")
        while current is not None:
            print(f"Name: {current.name}, Condition: {current.condition}, Priority: {current.priority}")
            current = current.next

    def search_patient(self, name):
        current = self.head
        while current is not None:
            if current.name == name:
                print(f"Patient found: Name: {current.name}, Condition: {current.condition}, Priority: {current.priority}")
                return current
            current = current.next
        print(f"Patient {name} not found in the queue.")
        return None

    def update_patient_info(self, name, condition=None, priority=None):
        patient = self.search_patient(name)
        if patient:
            if condition is not None:
                patient.condition = condition
            if priority is not None:
                patient.priority = priority
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
                queue.remove_patient()
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
