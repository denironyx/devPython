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