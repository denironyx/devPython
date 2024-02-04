# Chapter 10

## Files and Exceptions
This chapters will teach you to handle errors so your programs don't crash when they encounter unexpected situations. You'll learn about exceptions, which are special objects Python creates to manage errors that arise while a program is running.

Learning to work with files and save data will make your programs
easier for people to use. Users will be able to choose what data to enter and
when to enter it. People can run your program, do some work, and then
close the program and pick up where they left off later. Learning to handle
exceptions will help you deal with situations in which files don’t exist and
deal with other problems that can cause your programs to crash. This will
make your programs more robust when they encounter bad data, whether it comes from innocent mistakes or from malicious attempts to break your programs. With the skills you’ll learn in this chapter, you’ll make your programs
more applicable, usable, and stable.

### Reading from a File

An incredible amount of data is available in text files. Text files can contain
weather data, traffic data, socioeconomic data, literary works, and
more. Reading from a file is particularly useful in data analysis applications,
but it’s also applicable to any situation in which you want to analyze
or modify information stored in a file. For example, you can write a
program that reads in the contents of a text file and rewrites the file with
formatting that allows a browser to display it.

##### Reading an Entire File
To begin, we need a file with a few lines of text in it. Let’s start with a file
that contains pi to 30 decimal places, with 10 decimal places per line
`chapter10/file_reader.py`

### Writing to a File
One of the simplest ways to save data is to write it to a file. When you write
text to a file, the output will still be available after you close the terminal
containing your program’s output. You can examine output after a program
finishes running, and you can share the output files with others as well. You
can also write programs that read the text back into memory and work with
it again later.

### Exceptions
Python uses special objects called exceptions to manage errors that arise during
a program’s execution. Whenever an error occurs that makes Python
unsure what to do next, it creates an exception object. If you write code
that handles the exception, the program will continue running. If you don’t
handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.
Exceptions are handled with try-except blocks. 

Exceptions are handle with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly errorr messages that you write.

##### Handling the ZeroDivisionError Exception

The error reported at u in the traceback, ZeroDivisionError, is an exception
object. Python creates this kind of object in response to a situation
where it can’t do what we ask it to. When this happens, Python stops the
program and tells us the kind of exception that was raised. We can use this
information to modify our program.


##### Using Exceptions to Prevent Crashes
Handling errors correctly is especially important when the program has more work to do after the error occurs. 
It’s bad that the program crashed, but it’s also not a good idea to let
users see tracebacks. Nontechnical users will be confused by them, and in
a malicious setting, attackers will learn more than you want them to know
from a traceback. For example, they’ll know the name of your program
file, and they’ll see a part of your code that isn’t working properly. A skilled
attacker can sometimes use this information to determine which kind of
attacks to use against your code.

##### The else block
We can make this program more error resistant by wrapping the line that
might produce errors in a try-except block. The error occurs on the line
that performs the division, so that’s where we’ll put the try-except block

#### Handling the FileNotFoundError Exception
One common issue when working with files is handling missing files. The
file you’re looking for might be in a different location, the filename may
be misspelled, or the file may not exist at all. You can handle all of these
situations in a straightforward way with a try-except block.

#### Working with Multiple Files



#### Failing Silently
In the previous example, we informed our users that one of the files
was unavailable. But you don’t need to report every exception you catch.
Sometimes you’ll want the program to fail silently when an exception occurs
and continue on as if nothing happened. To make a program fail silently, you
write a try block as usual, but you explicitly tell Python to do nothing in the
except block. Python has a `pass` statement that tells it to do nothing in a block

#### Deciding Which Errors to Report
How do you know when to report an error to your users and when to fail
silently? If users know which texts are supposed to be analyzed, they might
appreciate a message informing them why some texts were not analyzed. If
users expect to see some results but don’t know which books are supposed
to be analyzed, they might not need to know that some texts were unavailable.
Giving users information they aren’t looking for can decrease the
usability of your program. Python’s error-handling structures give you finegrained
control over how much to share with users when things go wrong;
it’s up to you to decide how much information to share.

Well-written, properly tested code is not very prone to internal errors,
such as syntax or logical errors. But every time your program depends on
something external, such as user input, the existence of a file, or the availability
of a network connection, there is a possibility of an exception being
raised. A little experience will help you know where to include exception
handling blocks in your program and how much to report to users about
errors that arise.

#### Storing Data
Many of your programs will ask users to input certain kinds of information. You might allow users to store preferences in a game or provide data for a visualization. Whatever the focus of your program is, you'll store the information users provide in data structures suchh as lists and dictionaries. When users close a program, you'll almost always want to save the information they entered. A simple way to do this involves storing your data using the json module.

##### using json.dump() and json.load()
Let’s write a short program that stores a set of numbers and another program
that reads these numbers back into memory. The first program will
use json.dump() to store the set of numbers, and the second program will use
json.load().

##### Saving and Reading User-Generated Data
Saving data with json is useful when you're working with user-generated data, because if you don't store store your user's information somehow. You'll lose it when the program stops running. 


##### Refactoring 
Often, you’ll come to a point where your code will work, but you’ll recognize
that you could improve the code by breaking it up into a series of functions
that have specific jobs. This process is called refactoring. Refactoring
makes your code cleaner, easier to understand, and easier to extend.