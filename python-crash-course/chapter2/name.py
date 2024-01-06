# A string is as series of characters. Anything inside quotes is considered a string in Python
# and you can use a single or double quotes around your string

string = "This is a string!"
print(string)

string = 'This is also a string!'
print(string)

# Changing Case in a String with Methods (title, upper, etc)
name = "ada lovelace"
print(name.title()) # the title method is acting on the variabale name
print(name.upper())

# A method is an action that Python can perform on a piece of data.
# Every method is followed by a set of parentheses, because methods often need additional information to do their work.

print(name.lower())

# Using Variables in Strings
first_name = "Dennis"
last_name = "Irorere"

full_name = f"{first_name} {last_name}"
print(full_name)

# working f-strings (format - f)
print(f"Hello, {full_name.title()}!")
print(f"Hello, {full_name.upper()}!")