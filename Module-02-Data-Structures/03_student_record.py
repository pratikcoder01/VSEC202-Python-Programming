"""
Student record system using a dictionary.
Key   : roll number
Value : another dictionary with name and marks
"""

students = {}

while True:
    print("\n=== Student Record System ===")
    print("1. Add / Update student")
    print("2. View all students")
    print("3. Search by roll number")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Record saved.")
    elif choice == "2":
        if not students:
            print("No student records available.")
        else:
            for roll, info in students.items():
                print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
    elif choice == "3":
        roll = input("Enter roll number to search: ")
        if roll in students:
            info = students[roll]
            print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
        else:
            print("Student not found.")
    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        if roll in students:
            del students[roll]
            print("Record deleted.")
        else:
            print("Student not found.")
    elif choice == "5":
        print("Exiting Student Record System.")
        break
    else:
        print("Invalid choice. Please try again.")
