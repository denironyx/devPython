## Numerical comparisons
age = 19
age == 19

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
    
# it passes because the value answer 17 is not equal to 42

## CHecking Multiple Conditions
# You may want to check multiple conditions at the same time

# Using AND to Check MUltiple Conditions

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

# Using OR  to Check MUltiple Conditions

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

## checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings