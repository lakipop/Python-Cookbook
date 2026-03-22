# %%
"""
Practical 03: Python Tuples, Sets and Dictionaries
"""

# %%
"""
Part 1: Python Tuples
1.2 Creating a Tuple
"""
# Teaching Note: Tuples are ordered and immutable. Created with parentheses `()`.
rgb = ('red', 'green', 'blue')
print(rgb[0])
print(rgb[1])
print(rgb[2])

# %%
"""
1.3 Tuple with Duplicate Values and Length
"""
# Teaching Note: Tuples allow duplicate values because they are indexed. `len()` gets the count.
thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)
print(len(thistuple))

# %%
"""
1.4 Single-Item Tuple (Important!)
"""
# Teaching Note: A single-item tuple MUST have a trailing comma, otherwise Python treats it as just a value in parentheses.
numbers = (3,)
print(type(numbers))
numbers = (3)
print(type(numbers))

# %%
"""
1.5 Tuple with Mixed Data Types
"""
# Teaching Note: Tuples can store different data types seamlessly.
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# %%
"""
1.6 Changing Tuple Values (Using List Conversion)
"""
# Teaching Note: Since tuples are immutable, to change a value, cast it to a list, edit the list, and cast it back to a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# %%
"""
1.7 Adding Items to a Tuple
"""
# Teaching Note: You cannot `.append()` to a tuple. Instead, use the `+=` operator with another tuple.
thistuple = ("apple", "banana", "cherry")
thistuple += ("orange",)
print(thistuple)

# %%
"""
1.8 Removing Items from a Tuple
"""
# Teaching Note: Similar to mutating, removing requires casting to a list, using `.remove()`, and casting back.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# %%
"""
1.9 Iterating Through Tuples
"""
# Teaching Note: You can loop through a tuple directly by its items or by using its indices via `range(len())`.
for item in thistuple:
    print(item)
    
for i in range(len(thistuple)):
    print(thistuple[i])

# %%
"""
1.10 Joining Tuples
"""
# Teaching Note: The `+` operator directly concatenates tuples.
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
print(tuple1 + tuple2)

# %%
"""
Part 2: Python Sets
2.2 Creating Sets
"""
# Teaching Note: Sets are unordered collections of UNIQUE items. Created using `{}` or `set()`.
skills = {'Python', 'Databases', 'Software Design'}
empty_set = set() # Note: {} creates an empty dictionary, not an empty set!

# %%
"""
2.3 Checking Empty Set
"""
# Teaching Note: Empty collections evaluate to `False` in Python conditional statements.
skills = set()
if not skills:
    print("Empty sets are falsy")

# %%
"""
2.4 Iterating Through a Set
"""
# Teaching Note: You can iterate over sets, but the order is NOT guaranteed.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# %%
"""
2.5 Adding Elements
"""
# Teaching Note: `.add()` inserts one element. `.update()` adds elements from another iterable (like a list or set).
thisset.add("orange")
thisset.update({"mango", "papaya"})
print(thisset)

# %%
"""
2.6 Removing Elements
"""
# Teaching Note: `.remove()` errors if the element doesn't exist. `.discard()` fails silently if the element doesn't exist.
color_set = {'red', 'yellow', 'white'}
color_set.remove('yellow')
color_set.discard('white')
print(color_set)

# %%
"""
2.7 Set Operations
"""
# Teaching Note: Math operations natively supported. Union `|`, Intersection `&`, Difference `-`, Symmetric Difference `^`.
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B) # Union (All unique items)
print(A & B) # Intersection (Items in both)
print(A - B) # Difference (In A, but not B)
print(A ^ B) # Symmetric Difference (In either, but not both)

# %%
"""
2.8 Subset and Superset
"""
# Teaching Note: `.issubset()` checks if all elements are in the target. `.issuperset()` checks if it contains all target elements.
print({1,2}.issubset({1,2,3}))
print({1,2,3}.issuperset({1,2}))

# %%
"""
2.9 Nested Sets (Using frozenset)
"""
# Teaching Note: Standard sets are mutable, so they can't be hashed and put inside other sets. `frozenset` makes them immutable/hashable.
rainbow = ('red', 'green', 'blue')
other = ('black', 'white')
nested_set = set((frozenset(rainbow), frozenset(other)))
print(nested_set)

# %%
"""
Part 3: Python Dictionaries
3.2 Creating Dictionaries
"""
# Teaching Note: Dictionaries store key-value pairs formatted as `{"key": "value"}`.
person = {"name": "Jessa", "country": "USA", "age": 20}
print(person)

# %%
"""
3.3 Accessing Values
"""
# Teaching Note: Access via bracket `["key"]` (errors if key missing) or `.get("key")` (returns None if missing).
print(person["name"])
print(person.get("country"))

# %%
"""
3.4 Adding and Updating Items
"""
# Teaching Note: Simply assigning a new key or calling `.update()` mutates the dictionary in place.
person["weight"] = 50
person.update({"height": 6})
print(person)

# %%
"""
3.5 Iterating Dictionaries
"""
# Teaching Note: `.items()` returns tuples of (key, value) which unpack perfectly into a loop.
for key, value in person.items():
    print(key, ":", value)

# %%
"""
3.6 Removing Items
"""
# Teaching Note: `.pop(key)` removes a specific key. `.popitem()` removes the last inserted pair.
person.pop("age")
person.popitem()
print(person)

# %%
"""
3.7 Nested Dictionaries
"""
# Teaching Note: Values inside dictionaries can be dictionaries themselves, accessed via chained brackets.
address = {"city": "Houston", "state": "Texas"}
person = {"name": "Jessa", "address": address}
print(person['address']['city'])

# %%
"""
3.8 Sorting Dictionaries
"""
# Teaching Note: `sorted()` against a dictionary targets keys. Sorting `.items()` gives a list of alphabetically sorted tuples.
d = {'c': 45, 'b': 95, 'a': 35}
print(sorted(d.items()))

# %%
"""
Activity 1: Create a tuple of at least 5 subjects and print them using a loop.
"""
# Teaching Note: Standard tuple looping over iteration items.
subjects = ("Math", "Science", "History", "English", "Art")
for subject in subjects:
    print(subject)

# %%
"""
Activity 2: Create two sets of numbers and perform all set operations.
"""
# Teaching Note: Using the symbols `|`, `&`, `-`, and `^` directly applies set mapping.
s1 = {10, 20, 30}
s2 = {20, 30, 40}
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Diff:", s1 ^ s2)

# %%
"""
Activity 3: Create a dictionary to store student details and update/remove values.
"""
# Teaching Note: Using reassignment `[] =` to add/update, and `del` to remove specific keys outright.
student = {"id": 1, "name": "John", "grade": "A"}
student["grade"] = "A+"      # Update
student["age"] = 21          # Add
del student["id"]            # Remove
print(student)

# %%
"""
Activity 4: Create a nested dictionary to represent a student and their marks.
"""
# Teaching Note: Nest the marks dict directly as the value of the "marks" key.
nested_student = {
    "name": "Alice",
    "marks": {
        "math": 90,
        "science": 85
    }
}
print(nested_student["marks"]["math"])

# %%
"""
Activity 5: Convert a tuple into a list, modify one element, and convert it back.
"""
# Teaching Note: The standard mutability workaround mechanism.
colors_tup = ("Red", "Blue", "Green")
colors_list = list(colors_tup)
colors_list[1] = "Yellow"
colors_tup = tuple(colors_list)
print(colors_tup)

# %%
"""
Activity 6: Join two tuples and display the result.
"""
# Teaching Note: Directly `+` two sets defined as tuples natively merges them into a brand new ordered tuple.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# %%
"""
Activity 7: Add multiple elements to an existing set.
"""
# Teaching Note: `.update()` handles adding sequences to a set, while `.add()` is for singular objects.
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)

# %%
"""
Activity 8: Create a tuple with mixed data types and print its length.
"""
# Teaching Note: Native mix arrays evaluate exactly the same structurally as singular-type tuples.
mixed_tuple = (1, "string", 3.14, True)
print(f"Length: {len(mixed_tuple)}")

# %%
"""
Activity 9: Iterate through a tuple using index-based looping.
"""
# Teaching Note: Pass the tuple's length natively via `range(len())` to provide iterable indices.
tup_names = ("Lakindu", "Shehan", "Silva")
for i in range(len(tup_names)):
    print(f"Index {i}: {tup_names[i]}")

# %%
"""
Activity 10: Perform union, intersection, difference, and symmetric difference on two sets.
"""
# Teaching Note: Method-based alternative to the math symbol operations (`|`, `&`, etc.).
set_a = {"A", "B", "C"}
set_b = {"B", "C", "D"}
print(set_a.union(set_b))         # Same as |
print(set_a.intersection(set_b))  # Same as &
print(set_a.difference(set_b))    # Same as -
print(set_a.symmetric_difference(set_b)) # Same as ^

# %%
"""
Activity 11: Check whether a given element exists in a set.
"""
# Teaching Note: Using the natively fast `in` keyword on hash tables. O(1) lookup speed.
target = "C"
print(target in set_a)

# %%
"""
Activity 12: Check whether one set is a subset of another.
"""
# Teaching Note: Can also use the `<=` operator in Python for subset checks natively!
small_set = {1, 2}
large_set = {1, 2, 3, 4}
print(small_set.issubset(large_set))
# Or smaller_set <= larger_set

# %%
"""
Activity 13: Create two disjoint sets and verify whether they are disjoint.
"""
# Teaching Note: Disjoint means zero intersecting items. `.isdisjoint()` checks natively.
dj1 = {1, 2}
dj2 = {3, 4}
print(f"Are disjoint? {dj1.isdisjoint(dj2)}")

# %%
"""
Activity 14: Create a nested set using frozenset.
"""
# Teaching Note: Sets need hashable (immutable) elements. `frozenset` freezes standard enumerables into hashable instances.
frozen_inner = frozenset([1, 2])
outer_set = {frozen_inner, 3, 4}
print(outer_set)

# %%
"""
Activity 15: Remove a key-value pair from a dictionary using pop().
"""
# Teaching Note: pop() removes the entry and safely returns the target variable it destroyed.
dict_pop = {"A": 1, "B": 2, "C": 3}
extracted = dict_pop.pop("B")
print("Removed:", extracted, "| Remaining:", dict_pop)

# %%
"""
Activity 16: Clear all elements from a dictionary.
"""
# Teaching Note: Using the inplace `.clear()` method empties mapping configurations entirely.
dict_clear = {"x": 100, "y": 200}
dict_clear.clear()
print(dict_clear)

# %%
"""
Activity 17: Merge two dictionaries into one.
"""
# Teaching Note: `dict1.update(dict2)` writes the second dict cleanly over the first in place.
# Python 3.9+ allows the bitwise OR operator `d1 | d2`.
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2) 
print(d1)

# %%
"""
Activity 18: Create and access a nested dictionary.
"""
# Teaching Note: Standard bracket or .get() stacking extracts deeper levels individually.
config = {
    "network": {
        "ip": "192.168.1.1",
        "port": 8080
    }
}
print(config["network"]["port"])

# %%
"""
Activity 19: Sort a dictionary by its keys.
"""
# Teaching Note: `sorted()` directly handles iterable sequences. Passing items() gives alphabetically sorted key-value tuples.
unsorted_dict = {"z": 100, "a": 10, "m": 50}
sorted_items = sorted(unsorted_dict.items())  # Returns list of tuples sorted by key
sorted_dict = dict(sorted_items)              # Optionally build a new dict
print(sorted_dict)

# %%
"""
Activity 20: Count the number of key-value pairs in a dictionary.
"""
# Teaching Note: The standard overarching `len()` method functions natively against top-level dictionary keys.
final_dict = {"one": 1, "two": 2, "three": 3}
print(f"Pair Count: {len(final_dict)}")
