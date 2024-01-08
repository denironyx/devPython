                        ##> Looping Through an Entire List
# Looping allows you to take the same action, or set of actions, with every items in a list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
for magician in magicians:
    print(f"{magician.title()}, that is a great trick!!!")
    print(f"I can't wait to see your next trick, {magician.title()}.")
    print("-------------------------------------------")
    
# Doing something after a for loop
# any lines of code after the for loop that are not indented are executed once without repetitioin

for magician in magicians:
    print(f"{magician.title()}, that is a great trick!!!")
    print(f"I can't wait to see your next trick, {magician.title()}.")
    print("-------------------------------------------")
    
print("Thank you, everyone. That was a great magic show!")

# when you are processing data using a for loop, this is a good way to summarize an operation that was performed on an entire data set

##  Avoiding Indentation Errors
# Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.