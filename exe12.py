age = input("How old are you? ")
# here we have a variable that takes an input and input
# it's a piece of information that the user will provide back to us;
# it's usually a question to get back a value, which can be any type of data,
# such as a string or an integer, etc.
# The input() function in Python serves to gather user input during program execution.
# It prompts the user to enter data via the keyboard and then reads the entered line of text
# Here's how input() functions:
# 1. Prompts the User: It can take an optional string argument, which serves
#    as a prompt message displayed to the user, guiding them on what data to enter.
# 2. Reads Input: After the user types their response and presses Enter, input()
#    captures the input as a string.
# 3. Returns Input: The function returns the entered string, which can be stored in
#    a variable for further processing in the program.
# 4. Handles Data Types: The input is always returned as a string, so if
#    you need a different data type (like an integer), you must convert it explicitly
#    using functions like int() or float().
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.8")