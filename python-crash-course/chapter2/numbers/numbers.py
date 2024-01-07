                ## Numbers 
# Numbers are used quite often in programming to keep score in games, represent data in visualization
# store informatin in web application

# Integers
2 + 3
3 - 2


# multiplication
2 * 3

# exponents
2 ** 3

# floats
# Python calls any number with a decimaal point a float. This term is used in most programming languages, and it refers to 
# the fact that a decimal point can appear at any position in a number.

0.1 + 0.1

0.2 + 0.2

2 * 0.2

# integers and floats
# when you divide any two numbers, even if they are integers that result in a whole, you will get a float.

4 / 2

2 / 4

6 / 6

# if you mix an integer with a float together, you get a float

1 + 0.2

1 + 3.0

# python defaults to a float in any operation that uses a float, even if the output is a whole number

                ## Underscores in Numbers
# you can group digits using underscores to make large numbers more readable - python ignores the underscores when storing these kind of values
a_billion = 1_000_000_000
print(a_billion)

                ## Multiple assignment
# You can assign values to more than one variable using just a single line.
# This is useful, when you are initializing a set of numbers

x, y, z = 0, 1, 2
print(f"values are: \n\tx: {x}\n\ty: {y}\n\tz: {z}")

                ## Constants
# A constant is a like a variable whose value stays the same throughout the life of a program
# Rule of thumbs to use capital letter to indicate a variable should be treated as a constant and never be changed

MAX_CONNECTIONS = 5000

# The python community philosophy is contained in "The Zen of Python"