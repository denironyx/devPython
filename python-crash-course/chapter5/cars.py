## IF STATEMENTS

# A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    
# at the heart of every if statement is an expression that can be evaluated as True or False and is called conditional test.