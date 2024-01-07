                                ## Introducing Lists
# A list is a collection of items in a particular order. A list can include, letters, numbers, names, whatever. 
# The items of a list doesn't have to be related in any particular way., because a list ussually contains morethan one elements
# good practice to make the name of a list plural: letters, digits, or names
# [] - square brackets indicates a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

## Accessng the Elements in a list
# List are ordered collections, so you can access any element in a list by telling python the position, or index of the item desired.

print(bicycles[0])

# add the title method
print(bicycles[0].title())

# Index Positions Start at 0, not 1
# The reason has to do with the how the list operations are implemented at a lower level.
print(bicycles[1])
print(bicycles[3])

# special syntax for accessing the last element in a list
print(bicycles[-1])

# This syntax is quite useful, because you'll often want to access the last items in a list without knowing exactly how long the list is.

messages = f"My first bicycle was a {bicycles[-1].title()}."
print(messages)