## Chapter 7: Users Input and While Loops 
Most programs are written to solve an end user’s problem. To do so, you usually need
to get some information from the user. For a simple example, let’s say someone wants to find
out whether they’re old enough to vote.

In this chapter I learnt how to accept user input so my program
can then work with it.  To do this, I learnt how to use the input() function.


## Introducing while loops

The `for` loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true.

#### Using flag
If many possible events might occur to stop the program, trying to test all these conditions in one while  statement becomes complicated and difficult.
For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program
is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop running
when any of several events sets the value of the flag to False.
Example:
```
chapter7/parrot.py
```

#### Using break to Exit a Loop
To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the `break` statement. The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren't, so the program only executes code that you want it to , when you want it to

```
chapter7/cities.py
```
#### Using continue in a loop
Rather than breaking out of a loop entirely without executing the rest of its
code, you can use the `continue` statement to return to the beginning of the
loop based on the result of a conditional test. For example, consider a loop
that counts from 1 to 10 but prints only the odd numbers in that range:

```
chapter7/counting.py
```

#### Using a while Loop with Lists and Dictionaries
The next time through the `while` loop, we’d receive another input value
and respond to that. But to keep track of many users and pieces of information,
we’ll need to use lists and dictionaries with our `while` loops.

`for` loop is effective for looping through a list, but you shouldn’t modify
a list inside a for loop because Python will have trouble keeping track of the
items in the list.

##### Moving Items from One List to Another
Using a `while` loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users. Here's what that code might look like:

```
chapter7/confirmed_users.py
```

#### Removing All Instances of Specific Values from a List
to remove all instances of a value from a list?

```
chapter7/pets.py
```

#### Filling a Dictionary with User Input
You can prompt for as much input as you need in each pass through a while
loop. Let’s make a polling program in which each pass through the loop
prompts for the participant’s name and response. We’ll store the data we
gather in a dictionary, because we want to connect each response with a
particular user

```
chapter7/mountain_poll.py
```