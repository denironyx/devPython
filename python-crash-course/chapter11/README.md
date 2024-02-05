## Testing your Code
When you write a function or a class, you can also write tests for that code. Testing proves that your code works as it's supposed to in response to all the input types it's designed to receive. When you write tests, you can be confident that your code will work correctly as more people begin to use your programs.

#### Testing a function 
We can see that the names generated here are correct. But let’s say we
want to modify get_formatted_name() so it can also handle middle names.
As we do so, we want to make sure we don’t break the way the function
handles names that have only a first and last name. We could test our code
by running names.py and entering a name like Janis Joplin every time we
modify get_formatted_name(), but that would become tedious.
```chapter11/names.py```

#### Unit Tests and Test Cases
The module unittest from the Python standard library provides tools for
testing your code. A **unit test** verifies that one specific aspect of a function’s behavior is correct. A **test case** is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle. A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function. Achieving full coverage on a large project can be daunting. It’s often good enough to write
tests for your code’s critical behaviors and then aim for full coverage only if
the project starts to see widespread use.

#### A Passing Test
The syntax for setting up a test case takes some getting used to, but once
you’ve set up the test case it’s straightforward to add more unit tests for your
functions. To write a test case for a function, import the unittest module
and the function you want to test. Then create a class that inherits from
unittest.

