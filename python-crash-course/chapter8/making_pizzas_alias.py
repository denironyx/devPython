print('\n--- Using as to Give a Function an Alias ----')
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(16, 'pepperoni', 'mushrooms', 'extra cheese', 'chicken')

print('\n--- Using as to Give a Module an Alias ----')
import pizza as pz 

pz.make_pizza(16, 'pepperoni')
pz.make_pizza(16, 'pepperoni', 'mushrooms', 'extra cheese', 'chicken')

print('\n--- Importing All Functions in a Module ----')
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(16, 'pepperoni', 'mushrooms', 'extra cheese', 'chicken')