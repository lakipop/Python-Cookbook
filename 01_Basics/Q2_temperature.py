# 2. Convert Celsius to Fahrenheit
try:
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"{celsius}°C is equal to {fahrenheit}°F")
except ValueError:
    print("Please enter a valid numeric temperature!")
