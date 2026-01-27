# 4. Remove duplicate elements from a list
original_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 1, 3]
print(f"Original List: {original_list}")

# 'set' automatically removes duplicates, then we convert back to 'list'
unique_list = list(set(original_list))
# Sort it to make it look nice (optional)
unique_list.sort()

print(f"List after removing duplicates: {unique_list}")
