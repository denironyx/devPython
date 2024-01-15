## How the input() function works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

## Letting the User Choose when to Quit
# we can make a script run as long as the user wants by putting most of the progrm inside a while loop

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
## Using a flag
# allows one to define one variable that determines whether or not the entire program is active. 
# It typically acts as a signal to the program.
