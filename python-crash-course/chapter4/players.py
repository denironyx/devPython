## Working with Part of a List
# slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])

print(players[1:4])
print(players[0:4])
print(players[2:])
print(players[-3:])

## Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)
    
## Copying a list
my_foods = ['pizza', 'falafel', 'carror cake']
friend_foods = my_foods[:]
print("My favourite foods are: ")
print(my_foods)

print("\n My friends favourite foods are: ")
print(friend_foods)

### appending
my_foods.append("cannoli")
friend_foods.append("ice cream")


print("My favourite foods are: ")
print(my_foods)

print("\n My friends favourite foods are: ")
print(friend_foods)