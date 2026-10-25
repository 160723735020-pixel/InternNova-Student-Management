from student import Student
from student_manager import StudentManager


def get_non_empty_input(prompt):
    """Ask until the user enters a non-empty value."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_integer_input(prompt, minimum, maximum):
    """Read an integer within the specified range."""

    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_marks_input(prompt):
    """Read marks between 0 and 100."""

    while True:
        try:
            marks = float(input(prompt))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def add_student(manager):
    """Collect information and register a student."""

    print("\n--- Add Student ---")

    student_id = get_non_empty_input("Enter student ID: ")
    name = get_non_empty_input("Enter student name: ")
    age = get_integer_input("Enter age: ", 1, 120)
    course = get_non_empty_input("Enter course: ")
    marks = get_marks_input("Enter marks (0-100): ")

    student = Student(student_id, name, age, course, marks)
    manager.add_student(student)


def view_students(manager):
    """Display all registered students."""

    print("\n--- All Students ---")
    manager.view_students()


def search_student(manager):
    """Search for a student by ID."""

    print("\n--- Search Student ---")

    student_id = get_non_empty_input("Enter student ID: ")
    manager.search_student(student_id)


def update_student(manager):
    """Collect new details for an existing student."""

    print("\n--- Update Student ---")

    student_id = get_non_empty_input("Enter student ID to update: ")

    if manager.find_student(student_id) is None:
        print("Student not found.")
        return

    name = get_non_empty_input("Enter new name: ")
    age = get_integer_input("Enter new age: ", 1, 120)
    course = get_non_empty_input("Enter new course: ")
    marks = get_marks_input("Enter new marks (0-100): ")

    manager.update_student(student_id, name, age, course, marks)


def delete_student(manager):
    """Delete a student after confirmation."""

    print("\n--- Delete Student ---")

    student_id = get_non_empty_input("Enter student ID to delete: ")

    if manager.find_student(student_id) is None:
        print("Student not found.")
        return

    confirmation = input(
        f"Delete student {student_id}? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        manager.delete_student(student_id)
    else:
        print("Deletion cancelled.")


def show_grade(manager):
    """Display a student's percentage and grade."""

    print("\n--- Calculate Grade ---")

    student_id = get_non_empty_input("Enter student ID: ")
    student = manager.find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    percentage = student.marks

    print(f"Student Name: {student.name}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {student.calculate_grade()}")


def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 42)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Grade")
    print("7. Exit")
    print("=" * 42)


def main():
    """Run the application."""

    manager = StudentManager()

    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
        "6": show_grade,
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Thank you for using Student Management System!")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid choice. Please select a number from 1 to 7.")
            continue

        try:
            action(manager)
        except (EOFError, KeyboardInterrupt):
            print("\nOperation interrupted.")
            break

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nApplication closed.")