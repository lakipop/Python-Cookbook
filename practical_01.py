# %%
"""
Practical 01: Introduction to Python Programming
"""

# %%
"""
Task 1: Hello World Program
Write a Python program to print Hello, World! on the screen.
"""
# Teaching Note: The `print()` function outputs text to the console. Strings must be enclosed in quotes.
print('Hello, World!')

# %%
"""
Task 2: Using Indentation and Loops
Write a program to print numbers from 1 to 9.
"""
# Teaching Note: Python uses indentation (spaces/tabs) to define blocks of code (like loops or functions). 
# A `while` loop repeatedly executes its block as long as the condition remains True.
i = 1
max_val = 10
while i < max_val:
    print(i)
    i = i + 1

# %%
"""
Task 3: Creating and Updating Variables
"""
# Teaching Note: Variables store data. Python is dynamically typed, so you don't declare the type.
# You can update the value of a variable by reassigning it.
message = 'Hello, World!'
print(message)
message = 'Good Bye!'
print(message)

# %%
"""
Numeric Data Types and Operations
"""
# Teaching Note: Python supports basic arithmetic: + (add), - (sub), * (mul), / (div), ** (exponent).
# Integers are whole numbers, and floats are decimal numbers.
print("Integers:")
print(20 + 10)
print(20 - 10)
print(20 * 10)
print(20 / 10)
print(3 ** 3)

print("\nFloats:")
print(0.5 + 0.5)
print(0.5 * 0.5)
print(0.1 + 0.2)

# %%
"""
Task 4: Creating Strings
"""
# Teaching Note: Strings can be created with single quotes (' '), double quotes (" "), 
# or triple quotes (''' ''') for strings that span multiple lines.
s1 = 'This is a string'
s2 = "Another string"
s3 = '''This string
spans multiple lines'''
print(s1)
print(s2)
print(s3)

# %%
"""
Task 5: String Concatenation, Accessing, and Slicing Strings
"""
# Teaching Note:
# + joins strings together (concatenation).
# Indexing (e.g., text[0]) gets a single character (0-based). Negative index gets from the end.
# Slicing (e.g., text[0:6]) extracts a substring from start to end (exclusive).
# len() returns the string length.
greeting = 'Good '
time = 'Morning'
print(greeting + time)

text = "Python String"
print(text[0])
print(text[-1])
print(text[0:6])
print(len(text))

# %%
"""
Exercise 1: Write a Python program to calculate the area of a rectangle.
"""
# Teaching Note: Assign length and width to variables, then multiply to get the area.
length = 5
width = 10
area = length * width
print(f"Area of rectangle: {area}")

# %%
"""
Exercise 2: Write a program to swap two numbers.
"""
# Teaching Note: To swap values using a temporary variable, assign the first to temp, 
# second to first, and temp to second.
a = 15
b = 25
print(f"Before: a={a}, b={b}")
temp = a
a = b
b = temp
print(f"After: a={a}, b={b}")

# %%
"""
Exercise 3: Create a string and display its first, middle, and last characters.
"""
# Teaching Note: Use standard indexing. For the middle, use integer division `//` on length.
my_string = "Programming"
first_char = my_string[0]
last_char = my_string[-1]
middle_char = my_string[len(my_string) // 2]
print(f"First: {first_char}, Middle: {middle_char}, Last: {last_char}")

# %%
"""
Exercise 4: Write a program to display your name using a multi-line string.
"""
# Teaching Note: Triple quotes maintain formatting and line breaks exactly as written.
my_name = """
L
A
K
I
N
"""
print(my_name)

# %%
"""
Exercise 5: Write a Python program that stores two numbers in variables and prints their sum, difference, product, and division.
"""
# Teaching Note: Using f-strings (f"...") makes it easy to embed variables directly into strings.
num1 = 20
num2 = 5
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")

# %%
"""
Exercise 6: Convert a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32
"""
# Teaching Note: Python follows standard math order of operations (PEMDAS).
celsius = 30
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

# %%
"""
Exercise 7: Write a program to calculate the area and perimeter of a square.
"""
# Teaching Note: Area = side², Perimeter = 4 * side.
side = 4
area = side ** 2
perimeter = 4 * side
print(f"Square Area: {area}, Perimeter: {perimeter}")

# %%
"""
Exercise 8: Given a string, print first character, last character, and length.
"""
# Teaching Note: Reuse indexing and the len() function to gather metadata.
sample_text = "Analysis"
print("First:", sample_text[0])
print("Last:", sample_text[-1])
print("Length:", len(sample_text))

# %%
"""
Exercise 9: Extract the word "Python" from the string "Learning Python Programming".
"""
# Teaching Note: String slicing extracts segments. Format is string[start:stop]. 
# The characters at index 9 through 14 form "Python" (stop index is 15, exclusive).
phrase = "Learning Python Programming"
word = phrase[9:15]
print("Extracted word:", word)

# %%
"""
Exercise 10: Store a full name and print the initials.
"""
# Teaching Note: Using split() breaks a string into a list of words, which we can unpack.
full_name = "Lakindu Shehan"
first, last = full_name.split()
initials = f"{first[0]}.{last[0]}."
print("Initials:", initials)

# %%
"""
Exercise 11: Swap Two Numbers (Without Using a Temporary Variable)
"""
# Teaching Note: Python supports multiple assignment on the same line. 
# x, y = y, x evaluates the right side as a tuple and unpacks to the left side variables.
x = 10
y = 20
print(f"Before: x={x}, y={y}")
x, y = y, x
print(f"After: x={x}, y={y}")

# %%
"""
Exercise 12: Store a large number using underscores and print it.
"""
# Teaching Note: Python 3 allows underscores (_) in numeric literals to improve readability.
large_number = 1_000_000_000
print("Large number:", large_number)

# %%
"""
Exercise 13: Change the first letter of a string "Python" to "Jython".
"""
# Teaching Note: Strings in Python are immutable (cannot be changed in place). 
# You must construct a new string using concatenation.
original = "Python"
modified = "J" + original[1:]
print("Modified string:", modified)

# %%
"""
Exercise 14: Display the following information using a multi-line string: Name, Degree Program, University.
"""
# Teaching Note: Triple quotes are perfect for multi-line text blocks.
info = """
Name: Lakindu
Degree Program: BSc in IT
University: University of Ruhuna
"""
print(info)

# %%
"""
Exercise 15: Write a Python program to calculate the volume of a cube.
"""
# Teaching Note: Volume = side³. Use the exponent operator (**).
cube_side = 5
volume = cube_side ** 3
print(f"Volume of the cube: {volume}")

# %%
"""
Exercise 16: Write a program to count the number of characters in a string (excluding spaces).
"""
# Teaching Note: The replace() method allows replacing spaces with empty strings.
text_with_spaces = "Hello World Python"
text_no_spaces = text_with_spaces.replace(" ", "")
count = len(text_no_spaces)
print(f"Character count (excluding spaces): {count}")

# %%
"""
Exercise 17: Create a string and print every second character.
"""
# Teaching Note: The third parameter in a slice is the 'step' (start:stop:step).
# A step of 2 means every alternating character.
string_sequence = "abcdefghij"
every_second = string_sequence[0::2]
print("Every second character (starting from the first):", every_second)

# %%
"""
Exercise 18: Store your NIC number or student ID as a string and print its length.
"""
# Teaching Note: Identifiers like NIC often behave better as strings if they have trailing letters (e.g., 'V') or leading zeros.
nic = "200012345678"
print(f"NIC Length: {len(nic)}")

# %%
"""
Exercise 19: Write a program to join two strings with a space in between.
"""
# Teaching Note: Standard concatenation (+). You can hardcode a space (" ") string between variables.
str1 = "Artificial"
str2 = "Intelligence"
joined = str1 + " " + str2
print("Joined String:", joined)
