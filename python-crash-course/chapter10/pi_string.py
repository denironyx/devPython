file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines() # he readlines() method takes each line from the file and stores it

pi_string = ''    
for line in lines: #e use a simple for loop to print each line from lines
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))