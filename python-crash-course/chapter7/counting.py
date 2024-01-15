## Introducing while loops

# The while loop in Action
current_number = 1 
while current_number <= 5:
    print(current_number)
    current_number += 1
    
# we start counting from 1 by assigning current_number the value 1, the value of current_number and then adds 
# 1 to that value with current_number += 1. ( The += operator is shorthand for current_number = current_number +1)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)