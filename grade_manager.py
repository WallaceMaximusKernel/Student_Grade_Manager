# Student Grade Manager

students = []


# Calculate Grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Add Student
def add_student():

    # Get student name
    while True:
        name = input("Enter student name: ")

        if name.strip() == "":
            print("Name cannot be blank. Try again.")
        else:
            break

    # Get student mark - I used float to allow decimal marks, but you can change it to int if you want whole numbers only
    while True:
        try:
            mark = float(input("Enter student mark: "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100. Try again.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    grade = get_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully!")


# Show Results
def show_results():

    if len(students) == 0:
        print("No student records available.")
        return

    print("\nName         Mark      Grade")

    for student in students:
        print(f"{student['name']:<13}{student['mark']:<10.2f}{student['grade']}")

    marks = [student['mark'] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print()
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


# Main Menu
while True:

    print("\n===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice. Please try again.")