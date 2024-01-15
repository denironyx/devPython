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