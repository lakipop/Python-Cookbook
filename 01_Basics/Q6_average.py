# 6. Calculate Average of Student Marks
marks = [85, 92, 78, 90, 88, 76, 95]

print(f"Student Marks: {marks}")

# Logic: Sum of all elements / Number of elements
total_marks = sum(marks)
number_of_subjects = len(marks)

average = total_marks / number_of_subjects

print(f"Total: {total_marks}")
print(f"Average: {average:.2f}") # .2f rounds to 2 decimal places
