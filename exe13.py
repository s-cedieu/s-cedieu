from sys import argv
# This is an example of using argv to get command line arguments in Python.
# The script expects three command line arguments after the script name.
# You can run this script from the command line like this:
# python3.6 ex13.py first second third
# Make sure to replace 'first', 'second', and 'third' with actual values.
# Importing argv from sys module to handle command line arguments
# The first line is how you call a libary in python we said form were want it and we import it 

#WARNING! Pay attention! You have been running python scripts without command line
#arguments. If you type only python3.6 ex13.py you are doing it wrong! Pay close
#attention to how I run it. This applies any time you see argv being used.
# Read the wyss for how to run this 
script, first, second, third, = argv
# Here we have a variable that is equal to a same meaning the argv variable break the four of 
# them and asighnt thema each one a meaning basically what the argv do is unpacking the four variables 
#Line 3 unpacks argv so that, rather than holding all the arguments, it gets assigned to four variables you
#can work with: script, first, second, and third. This may look strange, but “unpack” is probably
#the best word to describe what it does. It just says, “Take whatever is in argv, unpack it, and assign it
#to all of these variables on the left in order.”
#After that we just print them out like normal.

print("The script is called :", script)
print("Your first variable is :", first)
print("Your second variable is :", second)
print("your third variable is :", third)
