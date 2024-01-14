## If statements
# If the conditional test evalauates to True, python executes the code following the if statement
# If the test evaluates to False, Python ignores the code following the if statement

age = 19
if age >= 18:
    print("You are old enough to vote!")

# if-else statements

age = 17
if age >= 18:
    print("You are old enough to  vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too youngg to vote.")
    print("Please register to vote as soon as you turn 18!")
    
# admission cost is $25
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    

print(f'Your admission cost is ${price}.')

## Using a while True
while True:
    age = int(input("Enter age (enter -1 to exit): "))

    if age == -1:
        break  # Exit the loop if -1 is entered

    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    else:
        price = 40

    print(f"The price for age {age} is ${price}")