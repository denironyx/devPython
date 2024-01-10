## IF STATEMENTS

# A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    
# at the heart of every if statement is an expression that can be evaluated as True or False and is called conditional test.
car = 'bmw'
car == 'bmw'

# ignore Case when checking for equality
car = 'Audi'
car == 'audi'
car.lower() == 'audi' # the test car is now case insenstive