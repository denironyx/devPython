file_name = 'pi_digits.txt'

# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

## Making a list of lines from a file
with open(file_name) as file_object:
    lines = file_object.readlines() # he readlines() method takes each line from the file and stores it
    
for line in lines: #e use a simple for loop to print each line from lines
    print(line.rstrip())