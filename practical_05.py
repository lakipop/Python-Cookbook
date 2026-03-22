# %%
"""
Practical 05: File Handling, Modules, Exceptions & OOP
"""

# %%
"""
PART 1: File Handling
Step 1: Opening and Reading a File
Task 1.1 & 1.2
"""
# Teaching Note: Open files using open("filename", "mode"). Always close() them to free system memory.
with open("sample.txt", "w") as file:
    file.write("Python is powerful.\nFile handling is important.\nWe are learning Practical 05.\n")

file = open("sample.txt", "r")
content = file.read()
print("--- Task 1.2 Content ---")
print(content)
file.close()

# %%
"""
Step 2: Using with Statement
"""
# Teaching Note: The `with` statement guarantees the file is automatically closed when the block ends.
with open("sample.txt", "r") as file:
    content = file.read()
    print("--- Step 2 Content ---")
    print(content)

# %%
"""
Step 3: File Methods Practice
"""
# Teaching Note:
# .read(n) reads n characters.
# .tell() returns current cursor position.
# .seek(n) moves cursor to position n.
with open("sample.txt", "r") as file:
    print(file.read(10)) 
    print("Pointer position:", file.tell())
    file.seek(0)
    print("After seek:", file.tell())
    print("First line:", file.readline().strip()) # .strip() removes trailing newline for cleaner print
    print("All other lines:", file.readlines())

# %%
"""
Step 4: Writing and Appending
"""
# Teaching Note: "w" overwrites everything. "a" appends without deleting.
with open("newfile.txt", "w") as file:
    file.write("This is a new file.\n")
    file.write("Python File I/O example.\n")

with open("newfile.txt", "a") as file:
    file.write("Appending new content.\n")

# Check what was written
with open("newfile.txt", "r") as f:
    print(f.read())

# %%
"""
PART 2: Exception Handling
Step 5: Basic Exception Example
"""
# Teaching Note: Wraps risky code in `try`. Catch specific errors cleanly in `except` blocks.
try:
    num = int(input("\nEnter a number (try 0 to see the error): "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")
finally:
    print("Program completed. This finally block always runs.")

# %%
"""
Step 6: Custom Exception
"""
# Teaching Note: Custom exceptions are built by inheriting from the base `Exception` class.
class NegativeNumberException(Exception):
    pass

try:
    number = int(input("\nEnter a positive number (try a negative to trigger custom error): "))
    if number < 0:
        raise NegativeNumberException("Negative numbers not allowed!")
    print(f"You entered {number}")
except NegativeNumberException as e:
    print("Error:", e)

# %%
"""
PART 3: Modules
Step 7: Create Your Own Module (mymath.py)
"""
# Teaching Note: Modules allow you to separate code into clean files and import them.
# The file mymath.py must exist in the same directory.
import mymath
from mymath import add

print("\nFrom import mymath:", mymath.add(10, 5))
print("From import mymath:", mymath.subtract(10, 5))
print("From direct import add:", add(20, 10))

# %%
"""
PART 4: Object-Oriented Programming (OOP)
Step 8: Creating a Class and Object
"""
# Teaching Note: Classes act as blueprints. `__init__` is the constructor. `self` binds attributes to the instance.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)

s1 = Student("Nimal", 21)
s1.display()

# %%
"""
Step 9: Inheritance
"""
# Teaching Note: Inheritance allows a child class (Student) to inherit attributes and methods from a parent (Person).
class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("Hello,", self.name)

class StudentInherited(Person):
    def study(self):
        print(self.name, "is studying.")

stu = StudentInherited("Kamal")
stu.greet()
stu.study()

# %%
"""
Step 10: Encapsulation
"""
# Teaching Note: Prefixing an attribute with `__` makes it private, preventing direct outside modification.
class BankAccount:
    def __init__(self):
        self.__balance = 0 
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(5000)
# account.__balance = 10000 -> This would fail/create a new useless variable!
print("\nBalance:", account.get_balance())

# %%
"""
Step 11: Polymorphism
"""
# Teaching Note: Child classes overriding a parent method with their own unique behavior is Polymorphism.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for a in animals:
    a.speak()

# %%
"""
PART 5: Mini Integrated Task (Student Record Management System)
"""
# Teaching Note: Combining OOP, List Comprehensions, and File I/O.
class StudentRecord:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        return sum(self.marks) / len(self.marks)

# Data Entry
with open("records.txt", "a") as file:
    name = input("\nEnter name for Mini Task: ")
    marks = [int(input(f"Enter mark {i+1}: ")) for i in range(3)]
    student = StudentRecord(name, marks)
    file.write(f"{student.name},{student.marks[0]},{student.marks[1]},{student.marks[2]},{student.average():.2f}\n")

print("\n--- Current Records ---")
with open("records.txt", "r") as file:
    print(file.read())

# %%
"""
Question 1 - Basic File Reading
"""
# Teaching Note: Auto-generating country.txt for the test.
with open("country.txt", "w") as f:
    f.write("Sri Lanka\nIndia\nJapan\nAustralia\n")

with open("country.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n" + content)
    
with open("country.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

# %%
"""
Question 2 - Writing & Appending
"""
# Teaching Note: Mixing "w" to start fresh, and "a" to append sequentially.
with open("students.txt", "w") as file:
    file.write("Alice\nBob\nCharlie\n")

with open("students.txt", "a") as file:
    file.write("Diana\nEdward\n")

with open("students.txt", "r") as file:
    print("\n" + file.read())

# %%
"""
Question 3 - File Methods Practice
"""
# Teaching Note: pointer manipulation again to show cursor locations.
with open("data.txt", "w") as f:
    f.write("This is a random paragraph filled with information.\nIt has a second line too.\nAnd a third.")

with open("data.txt", "r") as file:
    print("\nFirst 20 chars:", file.read(20))
    print("Pointer at:", file.tell())
    file.seek(0)
    print("Line 1:", file.readline().strip())
    print("All Lines List:", file.readlines())

# %%
"""
Question 4 - Mini File Project (marks.txt)
"""
# Teaching Note: Another integration of lists and files.
name = input("\nEnter student name for Question 4: ")
scores = [int(input(f"Enter mark {i+1}: ")) for i in range(3)]

with open("marks.txt", "a") as file:
    file.write(f"{name},{scores[0]},{scores[1]},{scores[2]}\n")

print("\n--- Marks Report ---")
with open("marks.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        s_name = data[0]
        s_marks = [int(m) for m in data[1:]]
        s_total = sum(s_marks)
        s_avg = s_total / len(s_marks)
        print(f"Name: {s_name} | Total: {s_total} | Average: {s_avg:.2f}")

# %%
"""
Question 5 - Create Your Own Module (calculator.py)
"""
# Teaching Note: Ensure calculator.py exists in the same folder.
import calculator

try:
    print("\nAdd: 10 + 5 =", calculator.add(10, 5))
    print("Subtract: 10 - 5 =", calculator.subtract(10, 5))
    print("Multiply: 10 * 5 =", calculator.multiply(10, 5))
    print("Divide: 10 / 0 =", calculator.divide(10, 0))
except ZeroDivisionError as e:
    print("Caught Exception:", e)

# %%
"""
Question 6 - Input Validation Program
"""
# Teaching Note: `while True` loop is perfect for continually trapping the user until valid input passes the `try` block safely.
while True:
    try:
        val = int(input("\nEnter an integer: "))
        print("Valid integer entered:", val)
        break # Escape loop if previous line succeeds
    except ValueError:
        print("Error: That was not an integer. Try again!")

# %%
"""
Question 7 - Multiple Exceptions
"""
# Teaching Note: Catching multiple specified errors ensures the exact problem is communicated clearly.
try:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    print("Division Result:", num1 / num2)
except ValueError:
    print("ValueError: You must enter valid numeric values!")
except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide by zero!")
except Exception as e:
    print("A general exception occurred:", e)

# %%
"""
Question 8 - Class & Object
"""
# Teaching Note: Straightforward class encapsulation defining identity properties.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_details(self):
        print(f"'{self.title}' by {self.author} - ${self.price:.2f}")

print("")
b1 = Book("1984", "George Orwell", 15.99)
b2 = Book("Brave New World", "Aldous Huxley", 12.50)
b1.display_details()
b2.display_details()

# %%
"""
Question 9 - Inheritance
"""
# Teaching Note: `super().__init__()` passes initialization logic up to the parent component, so you don't repeat self.name = name.
class PersonBase:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Person: {self.name}, Age: {self.age}")

class StudentDerived(PersonBase):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
        
    def display_student(self):
        self.display()
        print(f"ID: {self.student_id}, Grade: {self.grade}")

print("")
s_obj = StudentDerived("Lakindu", 22, "S1001", "A")
s_obj.display_student()

# %%
"""
Question 10 - Encapsulation (BankAccount)
"""
# Teaching Note: Secure mutators prevent negative deposits natively.
class BankAccountSecure:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount!")
            
    def get_balance(self):
        return self.__balance

ba = BankAccountSecure()
ba.deposit(100)
ba.withdraw(40)
print(f"\nFinal Bank Balance: ${ba.get_balance()}")

# %%
"""
Question 11 - Polymorphism
"""
# Teaching Note: Shared interface signatures (like `area()`) mapping differently dynamically based on object type.
import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * (self.r ** 2)

shapes = [Rectangle(5, 10), Circle(7)]
print("")
for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")

# %%
"""
Project Task - Mini Student Management System
"""
# Teaching Note: Combines File Handling, Functions, Loops and Classes.
import os

class MainStudent:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def to_csv(self):
        return f"{self.name},{self.age},{self.course}\n"

def display_menu():
    print("\n--- Mini Student Management System ---")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

def add_student():
    try:
        name = input("Student Name: ")
        age = int(input("Student Age: "))
        course = input("Student Course: ")
        student = MainStudent(name, age, course)
        
        with open("system_students.txt", "a") as file:
            file.write(student.to_csv())
        print("Student added successfully!")
    except ValueError:
        print("Error: Age must be a number.")

def view_students():
    if not os.path.exists("system_students.txt"):
        print("No student records found!")
        return
        
    print("\nName\t\tAge\tCourse")
    print("-" * 40)
    with open("system_students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 3:
                print(f"{data[0]}\t\t{data[1]}\t{data[2]}")

# Note: Blocked by __name__ checking to prevent looping when hitting 'Run All' in a notebook.
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter 1, 2, or 3.")
