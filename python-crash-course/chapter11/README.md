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

```chapter11/test_name_function.py```

#### A Failing Test
What does a failing test look like? Let’s modify get_formatted_name() so it can
handle middle names, but we’ll do so in a way that breaks the function for
names with just a first and last name, like Janis Joplin.

```chapter11/test_name_function.py```

##### Responding to a Failed Test
What do you do when a test fails? Assuming you’re checking the right conditions,
a passing test means the function is behaving correctly and a failing
test means there’s an error in the new code you wrote. So when a test
fails, don’t change the test. Instead, fix the code that caused the test to fail.
Examine the changes you just made to the function, and figure out how
those changes broke the desired behavior.

#### Adding New Tests
Now that we know get_formatted_name() works for simple names again, let’s
write a second test for people who include a middle name. We do this by
adding another method to the class NamesTestCase

### Testing a Class 
In the first part of this chapter, you wrote tests for a single function. Now
you’ll write tests for a class. You’ll use classes in many of your own programs,
so it’s helpful to be able to prove that your classes work correctly. If you have
passing tests for a class you’re working on, you can be confident that improvements
you make to the class won’t accidentally break its current behavior.

### A Class to Test
Testing a class is similar to testing a function—much of your work involves
testing the behavior of the methods in the class. But there are a few differences,
so let’s write a class to test. Consider a class that helps administer
anonymous surveys

Assert Methods Available from the unittest Module

- assertEqual(a, b) Verify that a == b
- assertNotEqual(a, b) Verify that a != b
- assertTrue(x) Verify that x is True
- assertFalse(x) Verify that x is False
- assertIn(item, list) Verify that item is in list
- assertNotIn(item, list) Verify that item is not in list
 
### The setUp() Method
In *test_survey.py* we created a new instance of AnonymousSurvey in each test
method, and we created new responses in each method. The unittest.TestCase
class has a setUp() method that allows you to create these objects once and
then use them in each of your test methods. When you include a setUp()
method in a TestCase class, Python runs the setUp() method before running
each method starting with test_. Any objects created in the setUp() method
are then available in each test method you write.

The method setUp() does two things: it creates a survey instance u,
and it creates a list of responses v. Each of these is prefixed by self, so
they can be used anywhere in the class. This makes the two test methods
simpler, because neither one has to make a survey instance or a response.
The method test_store_single_response() verifies that the first response in
self.responses—self.responses[0]—can be stored correctly, and test_store
_three_responses() verifies that all three responses in self.responses can be
stored correctly.

When we run test_survey.py again, both tests still pass. These tests would
be particularly useful when trying to expand AnonymousSurvey to handle multiple
responses for each person. After modifying the code to accept multiple
responses, you could run these tests and make sure you haven’t affected the
ability to store a single response or a series of individual responses.