# Dictionary Methods in Python
'''
# Creating a sample dictionary
sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. keys() - Returns a view object of all keys
print("Keys:", sample_dict.keys())

# 2. values() - Returns a view object of all values
print("Values:", sample_dict.values())

# 3. items() - Returns a view object of key-value pairs
print("Items:", sample_dict.items())

# 4. get() - Returns the value for a specified key
print("Get 'name':", sample_dict.get("name"))

# 5. update() - Updates the dictionary with another dictionary or key-value pairs
sample_dict.update({"country": "USA"})
print("After update:", sample_dict)

# 6. pop() - Removes the specified key and returns its value
removed_value = sample_dict.pop("age")
print("Removed 'age':", removed_value)
print("After pop:", sample_dict)

# 7. popitem() - Removes and returns the last inserted key-value pair
last_item = sample_dict.popitem()
print("Popped item:", last_item)
print("After popitem:", sample_dict)

# 8. setdefault() - Returns the value of a key, and sets it if the key does not exist
default_value = sample_dict.setdefault("gender", "Female")
print("Set default 'gender':", default_value)
print("After setdefault:", sample_dict)

# 9. clear() - Removes all items from the dictionary
sample_dict.clear()
print("After clear:", sample_dict)

# 10. copy() - Returns a shallow copy of the dictionary
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
print("Original dictionary:", original_dict)
print("Copied dictionary:", copied_dict)
'''
# Set Methods in Python

# Creating a sample set
sample_set = {1, 2, 3, 4, 5}

# 1. add() - Adds an element to the set
sample_set.add(6)
print("After add:", sample_set)

# 2. remove() - Removes a specified element from the set
sample_set.remove(3)
print("After remove:", sample_set)

# 3. discard() - Removes a specified element, but does not raise an error
# if the element is not found
sample_set.discard(10)  # No error even if 10 is not in the set
print("After discard:", sample_set)

# 4. pop() - Removes and returns an arbitrary element from the set
popped_element = sample_set.pop()
print("Popped element:", popped_element)
print("After pop:", sample_set)

# 5. clear() - Removes all elements from the set
sample_set.clear()
print("After clear:", sample_set)

# 6. union() - Returns a new set with elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

# 7. intersection() - Returns a new set with elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 8. difference() - Returns a new set with elements in the first set but not in the second
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# 9. symmetric_difference() - Returns a new set with elements in either set
# but not in both sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# 10. issubset() - Checks if a set is a subset of another set
is_subset = {1, 2}.issubset(set1)
print("Is subset:", is_subset)

# 11. issuperset() - Checks if a set is a superset of another set
is_superset = set1.issuperset({1, 2})
print("Is superset:", is_superset)

# 12. isdisjoint() - Checks if two sets have no elements in common
is_disjoint = set1.isdisjoint({6, 7})
print("Is disjoint:", is_disjoint)