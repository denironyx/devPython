filename = 'programming.txt'

with open(filename, 'w') as file_object: # w replace everything.
    file_object.write("I love programming, very much.\n")
    file_object.write("I love creating machine learning solutions.\n")
    file_object.write("Someday I will build something that matters in the universe.\n")
    
with open(filename, 'a') as file_object: # a append to what already exist.
    file_object.write("----Appending starts here.----\n")
    file_object.write("I love programming, very much.\n")
    file_object.write("I love creating machine learning solutions.\n")
    file_object.write("Someday I will build something that matters in the universe.")