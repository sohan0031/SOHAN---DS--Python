class Patient:
    def __init__(self, patient_id, name, age, patient_problem):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.patient_problem = patient_problem
        self.next = None

class Patient_List:
    def __init__(self):
        self.head = None  

    def add_patient(self, patient_id, name, age, patient_problem):
        new_patient = Patient(patient_id, name, age, patient_problem)
        if self.head is None:
            self.head = new_patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_patient
        print(f"Patient {name} added successfully.")

    def search(self, patient_id):
        current = self.head
        while current:
            if current.patient_id == patient_id:
                print(f"Patient found with name {current.name}.")
                return
            current = current.next
        print("Patient not found.")

    def remove_patient(self, patient_id):
        current = self.head
        prev = None
        while current and current.patient_id != patient_id:
            prev = current
            current = current.next
        if current is None:
            print("No patient found with that ID.")
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Patient with ID {patient_id} has been removed.")

    def schedule_to_front(self, patient_id):
        if self.head is None or self.head.patient_id == patient_id:
            print(f"Patient with ID {patient_id} is already at the front.")
            return
        current = self.head
        prev = None
        while current and current.patient_id != patient_id:
            prev = current
            current = current.next
        if current is None:
            print("Patient not found.")
            return
        prev.next = current.next
        current.next = self.head
        self.head = current
        print(f"Patient with ID {patient_id} moved to the front.")

    def display_queue(self):
        current = self.head
        if self.head is None:
            print("No patients in the queue.")
            return
        print("Current Patient Queue:")
        while current is not None:
            print(f"Patient ID: {current.patient_id}, Name: {current.name}, Age: {current.age}, Problem: {current.patient_problem}")
            current = current.next

def main():
    queue = Patient_List()
    
    while True:
        command = input("Enter command (add, remove, search, view, move, exit): ").strip().lower()
        
        if command == "add":
            try:
                patient_id = int(input("Enter patient's ID: "))
                name = input("Enter patient's name: ")
                age = int(input("Enter patient's age: "))
                patient_problem = input("Enter patient's problem: ")
                queue.add_patient(patient_id, name, age, patient_problem)
            except ValueError:
                print("Invalid input. Please enter numeric values for ID and age.")
        elif command == "remove":
            try:
                patient_id = int(input("Enter patient's ID to remove: "))
                queue.remove_patient(patient_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif command == "search":
            try:
                patient_id = int(input("Enter patient's ID: "))
                queue.search(patient_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif command == "view":
            queue.display_queue()
        elif command == "move":
            try:
                patient_id = int(input("Enter patient's ID to move to front: "))
                queue.schedule_to_front(patient_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif command == "exit":
            print("Exiting the patient management system.")
            break
        else:
            print("Invalid command. Please enter add, remove, search, view, move, or exit.")

if __name__ == "__main__":
    main()
