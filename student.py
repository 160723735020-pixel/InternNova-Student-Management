class Student:
    """Represents a student and their academic information."""

    def __init__(self, student_id, name, age, course, marks):
        self._student_id = str(student_id)
        self._name = name
        self._age = int(age)
        self._course = course
        self._marks = float(marks)

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def course(self):
        return self._course

    @property
    def marks(self):
        return self._marks

    def calculate_grade(self):
        """Calculate the student's grade based on marks."""

        if self._marks >= 90:
            return "A+"
        elif self._marks >= 80:
            return "A"
        elif self._marks >= 70:
            return "B"
        elif self._marks >= 60:
            return "C"
        elif self._marks >= 50:
            return "D"
        else:
            return "F"

    def to_dict(self):
        """Convert the student object into a dictionary."""

        return {
            "student_id": self._student_id,
            "name": self._name,
            "age": self._age,
            "course": self._course,
            "marks": self._marks,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a student object from a dictionary."""

        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            marks=data["marks"],
        )

    def display(self):
        """Display the student's information."""

        print("-" * 45)
        print(f"Student ID : {self._student_id}")
        print(f"Name       : {self._name}")
        print(f"Age        : {self._age}")
        print(f"Course     : {self._course}")
        print(f"Marks      : {self._marks:.2f}")
        print(f"Grade      : {self.calculate_grade()}")
        print("-" * 45)