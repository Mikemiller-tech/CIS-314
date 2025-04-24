import random

# Creating a tuple and a list with 10 elements
tuple_data = ("Math", "Science", "History", "English", "Art", "Music", "Physics", "Biology", "Chemistry", "PE")
list_data = list(reversed(tuple_data))  # Reversed order

# Print the 3rd element
print("3rd element in tuple:", tuple_data[2])
print("3rd element in list:", list_data[2])

# Print elements in random order
print("Randomized tuple:", random.sample(tuple_data, len(tuple_data)))
print("Randomized list:", random.sample(list_data, len(list_data)))

# Add an 11th element
list_data.append("Computer Science")  # Lists can be modified
print("List after adding 11th element:", list_data)

# Tuples are immutable, need to recreate it
tuple_data = tuple_data + ("Computer Science",)
print("Tuple after adding 11th element:", tuple_data)

# Remove the first element
list_data.pop(0)
print("List after removing first element:", list_data)

# Tuples are immutable, so removing an element is not possible
tuple_data = tuple_data[1:]
print("Tuple after removing first element:", tuple_data)

# Remove the same element from both structures
element_to_remove = "History"
list_data.remove(element_to_remove)
print("List after removing element:", list_data)

# Since tuples are immutable, create a new tuple without the removed element
tuple_data = tuple(item for item in tuple_data if item != element_to_remove)
print("Tuple after removing element:", tuple_data)
