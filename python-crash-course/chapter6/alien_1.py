## Dictionaires

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

#  Working with dictionaire 
# dictionary is a collection of key-value pairs. Each key is connected to a value.

new_points = alien_0['points']
print(f"You just earned {new_points} points")

## Adding New Key-value pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. 
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

## Starting with an empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

## Modifying Values in a Dictionary
# to modify a value in a dictionary, give the namme of the dictionary with the key in square brackets and then the new value you want associated

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

###


###

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to thhe right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new positioin is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

## Removinig Key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

### Nesting 
# Sometimes you'll want to store multiple dictionaries in a list or a list of items as a value in a dictionary
# A list of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print(".....")