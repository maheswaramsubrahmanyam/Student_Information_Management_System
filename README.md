# Student Management System

This project is a Python-based Student Management System that allows users to perform various operations such as adding student details, finding students by different parameters, updating their information, and more. It provides a simple interface to manage student data efficiently.

## Features

1. Add student details (First Name, Last Name, Roll Number, CGPA, Course IDs).
2. Find students by:
   - Roll Number
   - First Name
   - Course ID
3. Display the total number of students.
4. Delete a student's details using their Roll Number.
5. Update student details such as name, roll number, CGPA, or courses.

## Technologies Used

- Python 3

## How to Run the Project

1. Clone the repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Run the script using the command:

   ```bash
   python Student_Information_Management_System.py
   ```

4. Follow the menu options to perform desired operations.

## Sample Inputs and Outputs

### Sample Input 1: Add Student
```
Add the Student Details
-------------------------
Enter the first name of student: Maheswaram
Enter the last name of student: Subrahmanyam
Enter the Roll Number: 101
Enter the CGPA you obtained: 9.5
Enter the course IDs (5 courses):
101
102
103
104
105
```

### Sample Output 1:
```
Student added successfully!
```

### Sample Input 2: Find by Roll Number
```
Enter the Roll Number of the student: 101
```

### Sample Output 2:
```
The Student Details are:
First Name: Maheswaram
Last Name: Subrahmanyam
CGPA: 9.5
Course IDs: 101, 102, 103, 104, 105
```

### Sample Input 3: Find by First Name
```
Enter the First Name of the student: Maheswaram
```

### Sample Output 3:
```
The Student Details are:
First Name: Maheswaram
Last Name: Subrahmanyam
Roll Number: 101
CGPA: 9.5
Course IDs: 101, 102, 103, 104, 105
```

### Sample Input 4: Find by Course ID
```
Enter the Course ID: 102
```

### Sample Output 4:
```
The Student Details are:
First Name: Maheswaram
Last Name: Subrahmanyam
Roll Number: 101
CGPA: 9.5
```

### Sample Input 5: Update Student
```
Enter the Roll Number to update: 101
What do you want to update?
1. First Name
2. Last Name
3. Roll Number
4. CGPA
5. Courses
Enter your choice: 4
Enter the new CGPA: 9.8
```

### Sample Output 5:
```
Student updated successfully!
```

### Sample Input 6: Delete Student
```
Enter the Roll Number to delete: 101
```

### Sample Output 6:
```
Student deleted successfully, if present.
```

## Future Enhancements

1. Implement a database for persistent storage.
2. Add a graphical user interface (GUI).
3. Provide user authentication for secure access.

## Author

**Maheswaram M V Subrahmanyam**

## License

This project is open-source and available under the MIT License.
