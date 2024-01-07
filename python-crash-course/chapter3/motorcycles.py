                            #> Changing, Adding, and Removing Elements
# Most lists you create will be dynamic, meaning you'll build a list and then add and remove elements frorm it as your program run its course.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# to change element in the list
motorcycles[0] = 'ducati'
print(motorcycles)

## adding elements to a list [append method]
## you might want to asdd to a list because, a new users registered to website you've built. You do so by appending elements to the end of the list

motorcycles.append('honda')
print(motorcycles)

# The append method makes it easy to build list dynamically. For example you can start a list empty and then add items to the list

motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('ducati')
print(motorcycles)

## Inserting ELement into a list
#> You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
#The insert() method opens a space at position 0 and stores the value 'ducati' at that location. This operation shifts every other value in the list one position to the right:
print(motorcycles)

## Removing Elements from a List
# Often, you'll want to remove an item or a set of items from a list. For example, when a player shoots down an alien from the sky 
# # you'll most likely want to removee it from the list of active aliens

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)

## Removing an Item usin the pop() method
# sometimes you'll want to use the value of an item after you remove eit from a list
# in a web application, you might want to remove a user from a list of active members and the add that user to a list of inactive members.
# the pop() method removes the last item in a list, but it lets you work with that item after removing it.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# we pop a value from the list and store that value in the variable popped_motorcycle.
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

## Popping Item from an Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# *! note: Each time you use pop(), the item you work with is no longer stored in the list.

# *? Removing an Item by Value
# Sometimes you won't knwo the position of the value you want to remove from a list. You can use the remove method with the value of the item to do this

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Using the value being remove

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

messages = f"The {too_expensive.title()} is the most expensive in the list here {motorcycles}."
print(messages)
