from sys import argv
# Fisrt we have argv funtion that we import from sys librerie.

script, input_file =argv
# This is the name we give to the two arguments we said that are equal to argv.

def print_all(f):
     print(f.read())
# Here we have our first funtion print all that takes an argument named f 
# and under we have the print funtion that is encharge of reading the argument name f.

def rewind(f):
     f.seek(0)
# Here is or second funtion named rewind that takes an argument to named f 
# and here we have the seek funtion to seek the argument or the file we gonna input wiht 
# the argv funtion and seek is encharge of change the the position of the file pointer.


def print_a_line(line_count, f):
     print(line_count, f.readline())
# Here we have our third funtion print a line this funtion takes two argument the first one count line 
# and this is encharge of counting the number of lines and the argument f is encharge of reading the 
# line whit the read line funtion so basically this funtion goes to each line of the txt file we input whit the argv funtion.

current_file = open(input_file)
# Here we have a variable named current file that takes the file we input for the argv funtion and wiht the open 
# funtion we open that file.

print("First let's print the whole file:\n")
# This line just print a message and make a new line with the comand \n for new line.

print_all(current_file)
# After our file it's open the funtion print all take it here as an argument and remenber its an open file 
# so another thing the funtion does is read the file couse we use the funtion read couse this funtion is
# encharge of print the file and read it.

print("Now lets rewind, kind of like a tape")
# This just print a message.

rewind(current_file)
# This is another of our funtion this funtion is encharge of change the place of the cursor, in this program we are using it
# to put an space betwen the lines in the test file with the seek funtion.

print("Let's print three lines. ")
# This just print a message.

current_line = 1
# Here we have the variable line and we are seting it at 1.

print_a_line(current_line, current_file)
# Here whit this funtion we are reading the current line of the current file whiht the readline funtion 
# and remenber taht we set curret line to 1 so this will read the first line of the test file.

current_line = current_line =+ 1
print_a_line(current_line, current_file)
# Here we are basically doing the same exept for +1 this mean that we are adding one to current line so it will go to line two
# and we changed for the study drill to =+ what what provides a shrot hand way to update a variable by adding 1 in this case 
# to go to line two.

current_line = current_line =+ 1
print_a_line(current_line, current_file)
# This line does the same as the last one but the reason we still adding 1 instead of adding two is couse when this line its 
# executed we are not at line 1 we are at line two so if we want to go to line three we just have to add 1.