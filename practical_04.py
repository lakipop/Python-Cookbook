# %%
"""
Practical 04: Flow Controls and Functions
"""

# %%
"""
Part 1: Python Conditional Statements
1.1 if Statement
"""
# Teaching Note: The `if` statement executes the indented block only when the condition evaluates to True.
number = 10
if number > 0:
    print('Number is positive')

# %%
"""
1.2 if-else Statement
"""
# Teaching Note: The `else` block catches everything that fails the initial `if` statement condition.
number = -5
if number > 0:
    print('Positive number')
else:
    print('Negative number')

# %%
"""
1.3 if-elif-else Statement
"""
# Teaching Note: `elif` allows you to chain multiple conditions. Python executes the first True block and skips the rest.
number = 0
if number > 0:
    print('Positive')
elif number == 0:
    print('Zero')
else:
    print('Negative')

# %%
"""
1.4 Nested if Statements
"""
# Teaching Note: You can nest `if` statements inside each other. Indentation is strictly enforced.
number = 5
if number >= 0:
    if number == 0:
        print('Number is zero')
    else:
        print('Number is positive')
else:
    print('Number is negative')

# %%
"""
Part 2: Python Loops
2.1 for Loop
"""
# Teaching Note: `for` loops iterate over a sequence (list, tuple, string, range).
print("Using range():")
for i in range(5):
    print(i)

print("\nIterating through a list:")
languages = ['Swift', 'Python', 'Go']
for lang in languages:
    print(lang)

# %%
"""
2.2 for Loop with else
"""
# Teaching Note: The `else` block in a `for` loop executes ONLY if the loop finishes normally (without hitting a break statement).
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print('No items left')

# %%
"""
2.3 while Loop
"""
# Teaching Note: A `while` loop runs as long as the condition is True. Remember to update the variable manually to avoid infinite loops!
i = 1
while i <= 5:
    print(i)
    i += 1

# %%
"""
2.4 while Loop with else
"""
# Teaching Note: Just like `for..else`, `while..else` runs the else block when the condition naturally becomes False.
counter = 0
while counter < 3:
    print('Inside loop')
    counter += 1
else:
    print('Inside else')

# %%
"""
2.5 Infinite Loop
"""
# Teaching Note: A loop that never naturally evaluates to False runs forever. We use `break` to manually exit.
while True:
    print('This loop runs forever... but we forced it to break.')
    break # Prevents actual infinite loop here

# %%
"""
Part 3: Loop Control Statements
3.1 break Statement
"""
# Teaching Note: `break` instantly stops and exits the loop entirely.
for i in range(5):
    if i == 3:
        break
    print(i)

# %%
"""
3.2 continue Statement
"""
# Teaching Note: `continue` instantly skips the rest of the current iteration and jumps to the next loop cycle.
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

# %%
"""
3.3 pass Statement
"""
# Teaching Note: `pass` does absolutely nothing. It is used as a placeholder where syntax requires code but you have nothing to write yet.
n = 10
if n > 10:
    pass
print('Hello')

# %%
"""
Part 4: Python Functions
4.2 Defining and Calling a Function
"""
# Teaching Note: Functions are defined using `def` followed by the name and `()`. Call it later by name.
def greet():
    print('Hello World')

greet()

# %%
"""
4.3 Functions with Arguments
"""
# Teaching Note: Variables passed into the function definition `()` are called parameters. The actual values passed in are arguments.
def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(5, 4)

# %%
"""
4.4 Return Statement
"""
# Teaching Note: `return` sends data back out of the function so a variable can capture it. 
def find_square(num):
    return num * num

result = find_square(3)
print(result)

# %%
"""
4.5 Default Parameters
"""
# Teaching Note: If you don't supply an argument, Python will automatically load the default value provided in the function header.
def greet_person(name, message='Hi'):
    return f"{message} {name}"

print(greet_person('John'))
print(greet_person('John', 'Hello'))

# %%
"""
4.6 Keyword Arguments
"""
# Teaching Note: You can explicitly name your arguments when calling. This allows you to supply them out of order.
def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

print(get_net_price(price=100, discount=0.06))

# %%
"""
4.7 Recursive Functions
"""
# Teaching Note: A recursive function calls itself. It MUST have a base condition to eventually stop.
def count_down(start):
    print(start)
    next_num = start - 1
    if next_num > 0:
        count_down(next_num)

count_down(3)

# %%
"""
Activity 1: Write a program to check whether a number is even or odd.
"""
# Teaching Note: The modulo operator `%` gets the remainder. Evens have a remainder of 0 when divided by 2.
num = 14
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# %%
"""
Activity 2: Print the multiplication table of a given number using a loop.
"""
# Teaching Note: `range(1, 11)` yields a sequence from 1 through 10. We iterate multiplying our target by the loop variable.
target = 7
print(f"Multiplication Table for {target}:")
for i in range(1, 11):
    print(f"{target} x {i} = {target * i}")

# %%
"""
Activity 3: Write a function to find the factorial of a number.
"""
# Teaching Note: Factorial is the accumulation of descending multiplications. 5! = 5 * 4 * 3 * 2 * 1.
def find_factorial(n):
    result_fact = 1
    for i in range(1, n + 1):
        result_fact *= i
    return result_fact

print(f"Factorial of 5 is {find_factorial(5)}")

# %%
"""
Activity 4: Write a recursive function to calculate the sum of first n natural numbers.
"""
# Teaching Note: Recursion involves passing n-1 back into the function until the base case (`n == 1`) is hit.
def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n - 1)

calc = 10
print(f"Sum of first {calc} natural numbers is {recursive_sum(calc)}")

# %%
"""
Activity 5: Write a function that accepts keyword arguments for student details.
"""
# Teaching Note: `**kwargs` allows packaging arbitrary numbers of keyword arguments into a dictionary inside the function.
def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

print_student_info(name="Alice", age=21, grade="A+", university="UOR")
