# %%
"""
Practical 02: Booleans, Operators, Type Conversion, and Lists
"""

# %%
"""
Task 1: Boolean Variables and Comparisons
"""
# Teaching Note: Booleans represent True or False values. Comparison operators like >, < evaluate to booleans.
is_active = True
is_admin = False
print(type(is_active))
print(30 > 20)
print(30 < 20)

# %%
"""
Task 2: Boolean Evaluation using bool() Function
"""
# Teaching Note: The bool() function converts a value to a boolean. 
# Empty strings, 0, and None are considered 'falsy'. Everything else is 'truthy'.
print(bool('Hi'))
print(bool(''))
print(bool(100))
print(bool(0))

# %%
"""
Task 3: Creating and Using Constants
"""
# Teaching Note: Python doesn't have true constant types. By convention, variables named in ALL_CAPS 
# are treated as constants that shouldn't be changed. 
# The lab requested separating them into 'constant.py', but we define them here to keep the single notebook style.
PI = 3.14
GRAVITY = 9.8

# Normally this would be `import constant` and `print(constant.PI)`
print(PI)
print(GRAVITY)

# %%
"""
Task 4: Comments and Documentation (using a function)
"""
# Teaching Note: Docstrings ("""...""") immediately following a function definition serve as its official documentation.
def calculate_area(radius):
    """Calculate area of a circle"""
    return 3.14 * radius * radius

print(calculate_area(7))

# %%
"""
Task 5: Calculating Net Price with User Input and Type Conversion
"""
# Teaching Note: input() always returns a string. To do math, you MUST cast it using int() or float().
price = input('Enter price: ')
tax = input('Enter tax rate: ')
net_price = float(price) * float(tax) / 100
print('Net price:', net_price)

# %%
"""
Task 6: Arithmetic and Comparison Operators
"""
# Teaching Note: `!=` means 'not equal'. Single `=` is assignment, `==` is equality check.
a = 10
b = 20
print(a + b)
print(a * b)
print(a > b)
print(a != b)

# %%
"""
Task 7: Logical Operators
"""
# Teaching Note: `and` requires both sides to be true. `not` inverts the boolean value.
price = 9.99
print(price > 5 and price < 10)
print(not(price > 10))

# %%
"""
Task 8: Using Built-in Math Functions
"""
# Teaching Note: max(), min(), and sum() are extremely fast built-in functions that operate on lists/iterables.
numbers = [3, 8, 1, 6]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# %%
"""
Task 9: Creating Lists
"""
# Teaching Note: Lists enclose elements in square brackets `[]` and can hold mixed data types.
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# %%
"""
Task 10: Accessing List Elements
"""
# Teaching Note: Like strings, lists are zero-indexed (`[0]`) and support negative indices backward from the end (`[-1]`).
letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print(letters[0])
print(letters[-1])

# %%
"""
Task 11: List Slicing
"""
# Teaching Note: `list[start:stop]` creates a sub-list. Omit both (`[:]`) to copy the entire list.
my_list = ['p','r','o','g','r','a','m','i','n','g']
print(my_list[2:5])
print(my_list[:])

# %%
"""
Task 12: Adding and Removing Items
"""
# Teaching Note: `append()` adds one item. `extend()` adds multiple via another list. `del` removes via index.
odd = [1, 3, 5]
odd.append(7)
odd.extend([9, 11])
print(odd)
del odd[1]
print(odd)

# %%
"""
Task 13: List Methods
"""
# Teaching Note: `count()` checks how many times an element appears. `index()` finds the first position of it.
my_list = [3, 8, 1, 6, 8]
print(my_list.count(8))
print(my_list.index(6))

# %%
"""
Task 14: Membership Operators
"""
# Teaching Note: `in` and `not in` quickly test whether a specific element exists within an iterable.
letters = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print('p' in letters)
print('a' not in letters)

# %%
"""
Exercise 1: Write a program to check whether a number is positive, negative, or zero.
"""
# Teaching Note: `if`, `elif`, and `else` blocks control program flow based on conditions.
num = float(input("Enter a number to check: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# %%
"""
Exercise 2: Write a Python program to convert Celsius to Fahrenheit using user input.
"""
# Teaching Note: Remember to cast the string input from input() into a float before running formula math.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# %%
"""
Exercise 3: Create a list of 10 numbers and find the maximum and minimum values.
"""
# Teaching Note: Built-in max() and min() functions are the cleanest way to do this in Python.
ten_numbers = [42, 17, 88, 5, 104, 23, 76, 3, 91, 55]
print(f"List: {ten_numbers}")
print(f"Maximum: {max(ten_numbers)}")
print(f"Minimum: {min(ten_numbers)}")

# %%
"""
Exercise 4: Write a program to remove duplicate elements from a list.
"""
# Teaching Note: Converting a list to a `set` automatically strips duplicates since sets require unique items. 
# Cast it back to a `list` afterward to retain familiar list properties.
duplicates_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
clean_list = list(set(duplicates_list))
print(f"Original: {duplicates_list}")
print(f"Cleaned: {clean_list}")

# %%
"""
Exercise 5: Write a program to count how many times a given element appears in a list.
"""
# Teaching Note: The `.count(item)` list method is tailored exactly for this.
sample_list = ['apple', 'banana', 'apple', 'cherry', 'apple', 'date']
search_element = 'apple'
freq = sample_list.count(search_element)
print(f"'{search_element}' appears {freq} times in the list.")

# %%
"""
Exercise 6: Create a list of student marks and calculate the average.
"""
# Teaching Note: Average = Sum / Count. We use Python's built-in `sum()` and `len()`.
marks = [85, 90, 78, 92, 88, 76]
average = sum(marks) / len(marks)
print(f"Marks: {marks}")
print(f"Average Mark: {average:.2f}")
