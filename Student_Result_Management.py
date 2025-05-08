# Student Result Management System – Python + SQLite
import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    subject1 INTEGER,
    subject2 INTEGER,
    subject3 INTEGER
)''')

def add_student(roll_no, name, s1, s2, s3):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (roll_no, name, s1, s2, s3))
    conn.commit()

def view_student(roll_no):
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    if student:
        total = student[2] + student[3] + student[4]
        avg = total / 3
        grade = 'A' if avg >= 75 else 'B' if avg >= 50 else 'C'
        return f"Name: {student[1]}, Total: {total}, Avg: {avg}, Grade: {grade}"
    return "Student not found"

# Example usage
add_student(1, "Alice", 80, 70, 90)
print(view_student(1))