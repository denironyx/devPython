## checking for inequality
# ?!= when two values are not equal
requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")
    
if requested_toppings != 'mushrooms':
    print("Hold the anchovies!")

# Testing Multiple Conditions
# The if-elif-else chain is powerful, butt it's only appropriate to use when you just need one test to pass.

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese'  in requested_toppings:
    print('Addinig extra cheese.')   