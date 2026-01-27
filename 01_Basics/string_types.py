# 1. Standard Strings (Single or Double Quotes)
# Best for short, single-line text
s1 = "Hello, Python!"
s2 = 'Hello, World!'

print("--- Standard Strings ---")
print(f"s1: {s1}")
print(f"s2: {s2}")

# 2. Multi-line Strings (Triple Quotes)
# Best for paragraphs, long text, or text with enters/line breaks
# This is what you were trying to do with s3!
s3 = """This is a string 
that spans multiple 
lines easily.""" 

print("\n--- Multi-line String ---")
print(s3)

# 3. Formatted Strings (f-strings)
# Best for combining variables and text together
name = "Lakindu"
age = 22
s4 = f"My name is {name} and I am {age} years old."

print("\n--- Formatted String ---")
print(s4)

# Proving they are all the SAME type
print("\n--- Verification ---")
print(f"Type of s1: {type(s1)}")
print(f"Type of s3: {type(s3)}")
print(f"Type of s4: {type(s4)}")
