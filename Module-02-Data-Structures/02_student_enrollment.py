"""
Student enrollment manager using a list of tuples.
Each student: (roll_number, name)
"""

students = []

while True:
    print("\n=== Student Enrollment Manager ===")
    print("1. Enroll student")
    print("2. View students")
    print("3. Remove student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        students.append((roll, name))
        print("Student enrolled.")
    elif choice == "2":
        if not students:
            print("No students enrolled.")
        else:
            print("Enrolled students:")
            for roll, name in students:
                print(f"Roll: {roll} | Name: {name}")
    elif choice == "3":
        roll = input("Enter roll number to remove: ")
        for s in students:
            if s[0] == roll:
                students.remove(s)
                print("Student removed.")
                break
        else:
            print("Student not found.")
    elif choice == "4":
        print("Exiting Student Enrollment Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
