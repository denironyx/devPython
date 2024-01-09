## List work well for storing collections of items that can change throughout the life of a program. 
# The ability to modify list is particularly important when you're working with a list on a website or a list of characters in a game.

## When you want to create a list of items that can't be changed, tuple does that. It's immuntable

## Defining a tuple
# a tuple uses parenthesis instead of square brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

## trying to change the items in the tuple
dimensions[0] = 250

## Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)
    
## writing over a Tuple
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions: ")
for dimension in dimensions:
    print(dimension)
    