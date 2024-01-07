# *? Organizing a list
# Imagine you have a list cars and want to sort that list alphabetically.

# Sorting a list permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
cars.sort()
print(cars)

# you can also sort in reverse order
cars.sort(reverse=True)
print(cars)

# Sorting a list Temporaririly with the sorted() function
# The sorted function lets you display your list in a particular order, but doesn't affect the actual order of the list

cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("Here is the original list:")
print(cars)

# Printing a list in reverse
print(cars)

cars.reverse()
print(cars)

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru', 'lexus']
len(cars)