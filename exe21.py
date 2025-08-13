def add(a,b):
     print(f"ADDING {a} + {b} ")
     return a + b 
# Here we have a funtion that take's two argument and with the funtion return we do a adding operation.

def subtract(a,b):
     print(f"Subtracting {a} - {b}")
     return a - b
# Here we have a funtion that take's two argument and with the funtion return we do a subtracting operation.


def multiply(a,b):
     print(f"MULTIPLYING {a} * {b}")
     return a * b
# Here we have a funtion that take's two argument and with the funtion return we do a multiplying operation.


def divide(a,b):
     print(f"DIVIDEING {a} / {b}")
     return a / b
# Here we have a funtion that take's two argument and with the funtion return we do a divideing operation.


print("Let's do some math wiht just funtions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Here we have a couple of variables that we convine whit our funtion and
# also we just give the meanding of the two arguments that those funtion takes.
print(f"Age: {age}, Height: {height}, Weight: {weight} and IQ: {iq}")

# This is a puzzle for extra credit.
print("Here is a puzzle ")

def me(t):
     d = iq/2
     i = weight * d
     p = height - i
     t = age + p
     return t
# This funtion is bad design but its an experiment so if i want to go back to the previus
# and correct version i just have to delete the funtion prototype and just put t in the first print funtion.

c = me(0)
# Return solo se puede usar dentro de una funcion 

# Its seem like i can put any number inside of the parentesis as number an python will give me the correct answer 
print(f"That becomes: {c} Can you do it by hand")

print("Yesssss")

def meo(a, b):
     print(f"{a } + {b}")
     return a + b 

j = meo(100,50)
f= j/2
print(f)

# Here i make my second funtion and i use funtion return and arguments to do it SOLI DEO GLORIA!