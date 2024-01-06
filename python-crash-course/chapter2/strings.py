        ## Adding whitespace to Strings with Tabs or Newline

# In programming, white space refers to any nonprinting character, such as spaces, tab and end-of-line symbols
#You can use whitespace to organize your output so it's easier for users to read

print("Python")
print("\tPython")

# To add a new line in string, use the character combination \n
print("Languages: \nPython\nC\nJavascript\nR")

# Can combine tabs and newlines in a single string
print("Languages:\n\tPython\n\tC\n\tJavascript\n\tR")

            ## Stripping Whitespace

# Extra whitespace can be confusing in running programs. 
favourite_language = "R and Python "
favourite_language
favourite_language.rstrip()
favourite_language = favourite_language.rstrip() # remove the whitespace permanently
favourite_language


