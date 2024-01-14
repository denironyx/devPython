## Writing Clear Prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

#the operator += takes the string that was assigned to prompt and adds the new string onto the end.

### Using int() to Accept Numerical Input
age = input("How old are you? ")
print(age)

age >= 18

## to fix this
age = input("How old are you? ")
age = int(age)
age >= 18