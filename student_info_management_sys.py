import sys

# Class to store student information
class Student:
    def __init__(self, fname, lname, roll, cgpa, cid):
        self.fname = fname
        self.lname = lname
        self.roll = roll
        self.cgpa = cgpa
        self.cid = cid

# List to store all students
students = []

# Function to add a student
def add_student():
    print("Add the Student Details")
    print("-------------------------")
    fname = input("Enter the first name of student: ")
    lname = input("Enter the last name of student: ")
    roll = int(input("Enter the Roll Number: "))
    cgpa = float(input("Enter the CGPA you obtained: "))
    cid = []
    print("Enter the course IDs (5 courses):")
    for _ in range(5):
        cid.append(int(input()))
    students.append(Student(fname, lname, roll, cgpa, cid))
    print("Student added successfully!\n")

# Function to find student by roll number
def find_by_roll():
    roll = int(input("Enter the Roll Number of the student: "))
    for student in students:
        if student.roll == roll:
            print("The Student Details are:")
            print(f"First Name: {student.fname}")
            print(f"Last Name: {student.lname}")
            print(f"CGPA: {student.cgpa}")
            print(f"Course IDs: {', '.join(map(str, student.cid))}\n")
            return
    print("Student with the given Roll Number not found.\n")

# Function to find student by first name
def find_by_first_name():
    fname = input("Enter the First Name of the student: ")
    found = False
    for student in students:
        if student.fname.lower() == fname.lower():
            print("The Student Details are:")
            print(f"First Name: {student.fname}")
            print(f"Last Name: {student.lname}")
            print(f"Roll Number: {student.roll}")
            print(f"CGPA: {student.cgpa}")
            print(f"Course IDs: {', '.join(map(str, student.cid))}\n")
            found = True
    if not found:
        print("No student found with the given First Name.\n")

# Function to find students enrolled in a particular course
def find_by_course():
    course_id = int(input("Enter the Course ID: "))
    found = False
    for student in students:
        if course_id in student.cid:
            print("The Student Details are:")
            print(f"First Name: {student.fname}")
            print(f"Last Name: {student.lname}")
            print(f"Roll Number: {student.roll}")
            print(f"CGPA: {student.cgpa}")
            found = True
    if not found:
        print("No students found enrolled in the given Course ID.\n")

# Function to print the total number of students
def total_students():
    print(f"The total number of students is {len(students)}.")
    print(f"You can add up to {50 - len(students)} more students.\n")

# Function to delete a student by roll number
def delete_student():
    roll = int(input("Enter the Roll Number to delete: "))
    global students
    students = [student for student in students if student.roll != roll]
    print("Student deleted successfully, if present.\n")

# Function to update a student's data
def update_student():
    roll = int(input("Enter the Roll Number to update: "))
    for student in students:
        if student.roll == roll:
            print("What do you want to update?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Roll Number")
            print("4. CGPA")
            print("5. Courses")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                student.fname = input("Enter the new First Name: ")
            elif choice == 2:
                student.lname = input("Enter the new Last Name: ")
            elif choice == 3:
                student.roll = int(input("Enter the new Roll Number: "))
            elif choice == 4:
                student.cgpa = float(input("Enter the new CGPA: "))
            elif choice == 5:
                print("Enter the new Course IDs (5 courses):")
                student.cid = [int(input()) for _ in range(5)]
            print("Student updated successfully!\n")
            return
    print("Student with the given Roll Number not found.\n")

# Driver code
def main():
    while True:
        print("The Task that you want to perform:")
        print("1. Add the Student Details")
        print("2. Find the Student Details by Roll Number")
        print("3. Find the Student Details by First Name")
        print("4. Find the Student Details by Course ID")
        print("5. Find the Total Number of Students")
        print("6. Delete the Student Details by Roll Number")
        print("7. Update the Student Details by Roll Number")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            find_by_roll()
        elif choice == 3:
            find_by_first_name()
        elif choice == 4:
            find_by_course()
        elif choice == 5:
            total_students()
        elif choice == 6:
            delete_student()
        elif choice == 7:
            update_student()
        elif choice == 8:
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
