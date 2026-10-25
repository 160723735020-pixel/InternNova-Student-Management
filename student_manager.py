import json
from pathlib import Path

from student import Student


class StudentManager:
    """Manages student records and JSON file storage."""

    def __init__(self):
        self._students = {}
        self._data_file = (
            Path(__file__).resolve().parent
            / "data"
            / "students.json"
        )
        self.load_students()

    def load_students(self):
        """Load student records from the JSON file."""

        if not self._data_file.exists():
            self._data_file.parent.mkdir(parents=True, exist_ok=True)
            self.save_students()
            return

        try:
            with self._data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                print("Warning: Student data must be a JSON list.")
                return

            loaded_students = {}

            for record in data:
                try:
                    if not isinstance(record, dict):
                        continue

                    student = Student.from_dict(record)

                    if not student.student_id.strip():
                        continue

                    if (
                        not student.name.strip()
                        or not student.course.strip()
                        or not 1 <= student.age <= 120
                        or not 0 <= student.marks <= 100
                    ):
                        continue

                    student_id = student.student_id.strip()

                    if student_id in loaded_students:
                        continue

                    loaded_students[student_id] = student

                except (KeyError, TypeError, ValueError):
                    continue

            self._students = loaded_students
            print(f"Loaded {len(self._students)} student record(s).")

        except json.JSONDecodeError:
            print("Error: The student data file contains invalid JSON.")
        except OSError as error:
            print(f"Error reading student data: {error}")

    def save_students(self):
        """Save all student records to the JSON file."""

        try:
            self._data_file.parent.mkdir(parents=True, exist_ok=True)

            data = [
                student.to_dict()
                for student in self._students.values()
            ]

            with self._data_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return True

        except (OSError, TypeError, ValueError) as error:
            print(f"Error saving student data: {error}")
            return False

    def add_student(self, student):
        """Add a new student if the ID is unique."""

        student_id = student.student_id.strip()

        if not student_id:
            print("Error: Student ID cannot be empty.")
            return False

        if student_id in self._students:
            print("Error: A student with this ID already exists.")
            return False

        self._students[student_id] = student

        if not self.save_students():
            del self._students[student_id]
            return False

        print("Student added successfully!")
        return True

    def view_students(self):
        """Display all registered students."""

        if not self._students:
            print("No student records found.")
            return

        print(f"\nTotal Students: {len(self._students)}")

        for student in self._students.values():
            student.display()

    def find_student(self, student_id):
        """Find a student by ID."""

        return self._students.get(student_id.strip())

    def search_student(self, student_id):
        """Search for and display a student."""

        student = self.find_student(student_id)

        if student is None:
            print("Student not found.")
            return None

        student.display()
        return student

    def update_student(self, student_id, name, age, course, marks):
        """Update an existing student's information."""

        student_id = student_id.strip()
        existing_student = self.find_student(student_id)

        if existing_student is None:
            print("Student not found.")
            return False

        updated_student = Student(
            student_id=student_id,
            name=name,
            age=age,
            course=course,
            marks=marks,
        )

        self._students[student_id] = updated_student

        if not self.save_students():
            self._students[student_id] = existing_student
            return False

        print("Student updated successfully!")
        return True

    def delete_student(self, student_id):
        """Delete a student by ID."""

        student_id = student_id.strip()
        student = self._students.get(student_id)

        if student is None:
            print("Student not found.")
            return False

        del self._students[student_id]

        if not self.save_students():
            self._students[student_id] = student
            return False

        print("Student deleted successfully!")
        return True

    def get_student_count(self):
        """Return the number of registered students."""

        return len(self._students)