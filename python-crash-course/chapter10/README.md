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