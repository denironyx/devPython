## Functions

In this chapter you’ll learn to write functions, which are named blocks of code
that are designed to do one specific job. When you want to perform a particular task
that you’ve defined in a function, you call the function
responsible for it. If you need to perform that task
multiple times throughout your program, you don’t need to type all the
code for the same task again and again; you just call the function dedicated
to handling that task, and the call tells Python to run the code inside the
function.

### Defining a Function


#### Keyword Arguments
A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion( you won't end up with a harry and Hamster)


#### Default Values
When writing a function, you can define a default value for each parameter.
If an argument for a parameter is provided in the function call, Python uses
the argument value. If not, it uses the parameter’s default value. So when
you define a default value for a parameter, you can exclude the corresponding
argument you’d usually write in the function call.

#### Return Values
A function doesn't always have to display its output directly. Instead, it can process some data and then return a value or set of values.  The value the funciton returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow you to move much of your program's grunt work into functions, which can simplify the body of your program.

##### Returning a Simple Value

##### Making an Argument Optional
But middle names aren't always needed, and this function as written would not work if you tried to call it with only a first name and a last name.

#### Passing a List
You’ll often find it useful to pass a list to a function, whether it’s a list of
names, numbers, or more complex objects, such as dictionaries. When you
pass a list to a function, the function gets direct access to the contents of
the list. Let’s use functions to make working with lists more efficient.
```
chapter8/greet_users.py
```

#### Modifying a List in a Function
When you pass a list a function, the function can modify the list. Any changes made to the list insidee the function's body are permanet, allowing you to work efficiently even when you're dealing with large amounts of  data.
```
chapter8/printing_models.py
```

#### Passing an Arbitrary Number of Arguments
Sometimes you won't know ahead of time how many arguments a function needs to accept. Fortunately, python allows a function to collect an arbitrary number of arguments from the calling statement.
```
chapter8/pizza.py
```
For example, consider a function that builds a pizza. It needs to accept a
number of toppings, but you can’t know ahead of time how many toppings
a person will want. The function in the following example has one parameter,
*toppings, but this parameter collects as many arguments as the calling
line provides:

The asterisk in the parameter name *toppings tells Python to make an
empty tuple called toppings and pack whatever values it receives into this
tuple. The print() call in the function body produces output showing that
Python can handle a function call with one value and a call with three
values.

#### Mixing Positional and Arbitrary Arguments
If you want a function to accept several different kinds of arguments, the
parameter that accepts an arbitrary number of arguments must be placed
last in the function definition. Python matches positional and keyword
arguments first and then collects any remaining arguments in the final
parameter.

```
chapter8/pizza.py
```
Note: generic parameter name *args, which collects arbitrary positional arguments like this

#### Using Arbitrary Keyword Arguments
Sometimes you’ll want to accept an arbitrary number of arguments, but you
won’t know ahead of time what kind of information will be passed to the
function. In this case, you can write functions that accept as many key-value
pairs as the calling statement provides. One example involves building user
profiles: you know you’ll get information about a user, but you’re not sure
what kind of information you’ll receive.

```
chapter8/user_profile.py
```