from sys import argv
from os.path import exists
# Here we are using to libraries one to use the funtion argv and another to use the exists funtion 
# The second one can be use to check if a file exist 

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file} ")

# We could do this in one line how?

in_file = open(from_file) 
# This funtion open its use to open a file 
indata = in_file.read()
# This funtion let us read the content of a file 
print(f"The length is {len(indata)} bytes long")
#In Python, len() is a built-in function that returns the number of items in an object.
#  This function can be used with various types of objects, including: 

print(f"Does the ouput file exist? {exists(to_file)}")
# This line check if the output file exist so exist gonna return us true cause i alredy make the file 
input()

out_file = open(to_file, 'w')
# Here this line is saying this varible is equal to open the file we gonna send the copy to 
out_file.write(indata)
# And write in the file the thing we read in the first part 

print("Alright, all done.")

out_file.close() ,in_file.close()
# This line is enchrge of closeing both file's

# Useing close here save us from data loseing and also leave the file open consume memory that we are not necesary using 
# also help whit error prevention.
# Concatanete erefers to the action of convineing one or more string its like smash two or more string into one single string