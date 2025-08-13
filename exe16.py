from sys import argv

script,filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# This first part are encharge of print and erase the content of the previus file 
input("?")

print("Opening the file...")
target = open (filename, 'w')
#this variable named target is encharge of open the file we give in the argv funtion
print("Truncating the file.  Goodbye!")
target.truncate()
# Truncate are encharge of  resizeing a file to a especified lenght in this case truncate 
# are use to only have three lines into the file 

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Target are encharge of set only three lines into the file 
print("and finally, we close it.")
target.close()