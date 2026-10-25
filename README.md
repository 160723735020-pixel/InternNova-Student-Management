# Student Management System

## Project Description

The Student Management System is a menu-driven Python application developed for the InternNova Week 6 internship assignment.

It allows users to manage student records, including personal details, course information, and academic marks. Student information is stored in a JSON file and remains available between application sessions.

## Features

* Add new student records.
* View all registered students.
* Search for students by ID.
* Update existing student information.
* Delete student records with confirmation.
* Calculate student grades.
* Save and load records using JSON.
* Validate user input.
* Prevent duplicate student IDs.
* Handle common input and file errors.

## Technologies Used

* Python 3
* JSON
* Git
* GitHub

## Python Concepts Used

* Variables and data types
* Input and output
* Operators and type conversion
* Conditional statements
* Loops
* Functions and methods
* Dictionaries and lists
* Classes and objects
* Constructors
* Encapsulation
* File handling
* Exception handling
* JSON serialization and deserialization
* Modules and imports

## Project Structure

```text
InternNova-Student-Management/
|-- main.py
|-- student.py
|-- student_manager.py
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- data/
|   |-- students.json
|-- screenshots/
|-- documentation/
```

## Requirements

* Python 3.10 or later.
* Git, if you want to clone and contribute to the repository.

The application uses Python's standard library and does not require external packages.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/160723735020-pixel/InternNova-Student-Management.git
```

### 2. Navigate to the project directory

```bash
cd InternNova-Student-Management
```

### 3. Run the application

```bash
python main.py
```

No additional package installation is required.

## How to Use

When the application starts, a menu appears with these options:

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Grade
7. Exit

Enter the corresponding number and follow the prompts.

Student records are saved automatically in `data/students.json`.

## Grade Calculation

| Marks          | Grade |
| -------------- | ----- |
| 90 to 100      | A+    |
| 80 to below 90 | A     |
| 70 to below 80 | B     |
| 60 to below 70 | C     |
| 50 to below 60 | D     |
| Below 50       | F     |

## Screenshots

Application screenshots will be included in the `screenshots/` directory.

## Challenges Faced

* Organizing the application into separate Python modules.
* Maintaining student records between executions.
* Validating user input.
* Preventing duplicate student IDs.
* Managing JSON file operations and common file errors.

## Future Improvements

* Introduce a graphical user interface.
* Add database integration using SQLite or MySQL.
* Generate academic performance reports.
* Support multiple subjects and examination records.
* Add user authentication and role-based access.
* Export student records to CSV or PDF.

## Conclusion

The Student Management System demonstrates the practical application of Python programming concepts through a simple student-record management solution.

It provides student record management, input validation, grade calculation, and persistent storage using JSON.

## Internship Information

* Organization: InternNova
* Assignment: Week 6 - Git, GitHub and Final Project
* Project: Student Management System
* Language: Python
