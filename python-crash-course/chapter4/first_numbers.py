## Making NUmerical Lists
# Using the range() Function

for value in range(1,5):
    print(value)
    
# Using range to make a list of number
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

## Task: a list of the square of each integer from 1 through 10
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)

## Simple statistics with a list of Number
digits = list(range(0,10))
min(digits)
max(digits)
sum(digits)


# List comprehension
#  a list comprehension combines the for loop and the creaton of new elements into one line, and automatically apend each new element

squares = [value**2 for value in range(1,11)]
print(squares)