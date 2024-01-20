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
The definition of build_profile() expects a first and last name, and
then it allows the user to pass in as many name-value pairs as they want. The
double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs
it receives into this dictionary.
Note: You’ll often see the parameter name **kwargs used to collect non-specific keyword
arguments.

### Storing Your Function in Modules
One advantage of functions is the way they separate blocks of code from
your main program. By using descriptive names for your functions, your
main program will be much easier to follow. You can go a step further by
storing your functions in a separate file called a module and then importing
that module into your main program. An `import` statement tells Python to
make the code in a module available in the currently running program file.

Storing your functions in a separate file allows you to hide the details of your program's code and focus on its higher-level logic. It also allows you to reuse functions in many different programs. When you store your functions in separate files, you can share those files with other programmers without having to share your entire program.

#### Importing an Entire Module
To start importing functions, we first need to create a module. A module
is a file ending in **`.py`** that contains the code you want to import into your program.

```
chapter8/making_pizzas.py
```

#### Importing Specific Functions
Importing a specific function from a module, require a particular syntax
```
from module_name import function_name
```
You can import as many functions as you want from a module by separating each function's name with a commaa.

```
from module_name import function_name, function_name_2, function_name_3
```

#### Using as to Give a Function an Alias
If the name of a function you're importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias -- an alternate name similar to a nickname for the function. 

Here we give the function `make_pizza()` an alias, `mp()` by importing make_pizza as mp


#### Importing All Functions in a Module
The asterisk in the import statement tells Python to copy every function
from the module pizza into this program file. Because every function
is imported, you can call each function by name without using the dot
notation. However, it’s best not to use this approach when you’re working
with larger modules that you didn’t write: if the module has a function
name that matches an existing name in your project, you can get some
unexpected results. Python may see several functions or variables with the
same name, and instead of importing all the functions separately, it will
overwrite the functions.
The best approach is to import the function or functions you want or import the entire module and usee dot notation. This leads to clear code that's easy to read and understand.

```
from module_name import *
```