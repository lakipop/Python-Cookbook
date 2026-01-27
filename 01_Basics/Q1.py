# 1. Check if a number is positive, negative, or zero
try:
    number = float(input("Enter a number: "))
    
    if number > 0:
        print("The number is Positive.")
    elif number < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")
except ValueError:
    print("Please enter a valid number!")
