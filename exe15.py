from sys import argv
# Here we have the funtion argv from the sys library this funtion is similar
# to the input funtion but this one take more arguments from the user with just one funtion 

script, filename= argv

txt = open((filename))

# Here we have the open funtion that basically does is open a file or a program that we give the name 
print(f"Here's your filename {filename}:")
print(txt.read())
# And here are another of the new funtions read that basically read something that is incide of a file or program.

print("Type the filename again ")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close