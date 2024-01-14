# Consider  a program that determines whether people are tall enough to ride a roller coaster

height = input("How tall are you, in inches? ")
height = int(height)

if height > 48:
    print("\n You're tall enough to ride!")
else:
    print("\n You're not tall enough to ride!")