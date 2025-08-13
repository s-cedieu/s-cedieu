import sys
script, input_encoding, error = sys.argv
# This two lines just use the sys funtion and the argv funtion to take three inputs at the comand line.


def main(language_file, encoding, errors):
     line =language_file.readline()
# Here we have a funtion that requires three arguments one is taking the file  one encode the file
# and the other one is encharge of telling us if we have an error after we have a variable named 
# line that read each line of the file.

     if line:
          print_line(line,encoding,errors)
          return main(language_file,encoding, errors)
# I use something new. You will learn about this in the second half of the book, so consider this a
# teaser of interesting things to come. This is an if-statement, and it lets you make decisions
# in your Python code. You can test the truth of a variable and, based on that truth, run a piece
# of code or not run it. In this case I’m testing whether line has something in it. The readline
# function will return an empty string when it reaches the end of the file and if line simply
# tests for this empty string. As long as readline gives us something, this will be true, and the
# code under (indented in, lines 9–10) will run. When this is false, Python will skip lines 9–10.

def print_line(line,encoding,errors):
     next_lang = line.strip()
     raw_bytes = next_lang.encode(encoding, errors=errors)
     cooked_string = raw_bytes.decode(encoding,errors=errors)
# Here we have another funtion that requires three arguments only one is changeing from the other threes 
# This funtion have three variables inside and each one of them do something important, the variable name 
# next lang is encharge of strip the file that's mean erase all the blank space and the things that are 
# inside of an string but we dont need or use basically the errors wwe make when we left an extra space or something like that.
# After we have the rawbytes variable that is encharge of encode each line In Python, the encode() method is used to convert a string
# (which is a sequence of Unicode characters) into a sequence of bytes using a specified encoding scheme. This is crucial when dealing
# with data that needs to be transmitted over a network, written to a file, or stored in a database, as these typically require byte 
# sequences rather than raw strings.
# After we have our third funtion this funtion is encharge of decoing each line In Python, "decoding" refers to the process of converting
# a sequence of bytes (binary data) into a human-readable string (text). This is necessary because computers store data as bytes,
# but humans typically interact with text.
     print(raw_bytes, "<===>", cooked_string)
# this print funtion just print the encode and decode version of each name we have in our file 


languages = open("languages.txt", encoding = "utf -8")
# This line just open our file and encoding our file whit utf UTF-8 is a character encoding capable of encoding all possible characters,
# or code points, in the Unicode standard. It uses a variable number of bytes (1 to 4) per character, making it both flexible and
# efficient. Essentially, it's a way to represent text (like letters, numbers, symbols, and even emojis) in a way that computers can 
# understand and display correctly, regardless of the language or character set. 

main(languages, input_encoding,error)
# And here i'm not sure but i will eventualy 