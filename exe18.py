# This one it's like your script wiht argv

def print_two(*args):
     arg1, arg2 =args
     print(f"arg1 {arg1}, arg2 {arg2}")
     # This is our first funtion and its almost the same as the argv funtion
     # but we use this when we want to use the argv in our aun funtion 


# Ok those arg are poinles 
def print_two_again(arg1,arg2):
     print(f"arg1 {arg1}, arg2 {arg2}")
     # This is a easy wey to do the same, we have a funtion how takes two
     # arguments and whit the print f we print the two arguments inside of the print funtion 


# This print only one argument
def print_one(arg1):
     print(f"arg1 {arg1}")
     # This is the same as the last one but it only prints one argument 


def print_none():
     print("I got nothing")




def stervenci1(name,last_name):
     print(f" My name is {name} and my last name is {last_name}")
     # This is my funtion it does the sme as the first and second funtion of the book But its more user friendly.
     # Also somethin i just understand abaut funtion is you can create them and define them end give them the arguments in the bothom
     # Also you can put them above the funtion that creat them its like c you have to put the prototype before you call or use the funtion. 
     # Its seem like you can create a variable and don't use it even if it's inthe script. 
     
stervenci1("Stervency" , "Cedieu")
print_two("Stervency", "Cedieu")
print_two_again("Stervency", "Cedieu")
print_one("First")
print_none()




