from sys import exit
# import sys: This line imports the sys module, which contains the exit() function.
# sys.exit([status]): This is the function call.
# The status argument is optional. It's an integer that represents the program's exit status.
# A status of 0 typically indicates successful execution, while a non-zero status (e.g., 1) indicates an error or abnormal termination. 
# Behavior: When sys.exit() is called, the program terminates immediately, and no further code in the script is executed.
# It raises a SystemExit exception, which can be caught and handled if necessary, although this is less common for simple program exits.

def gold_room():
    print("This room is full of gold. How much do yo take? ")
    choice= (input("> "))
    
    if "0" in choice or "1" in choice:
        how_much =int (choice)

    else:
        dead("Dead men learn to type a number ")

    if how_much < 50:
        print("Nice your not a greedy, you win")
        exit(0)

    else:
        dead("You greedy bastard")
# Here we have a funtion the first thing this funtion does is print a question after we decre 
# a varibale named choice as equal to input and we make an if statement we said if 0 or 1 are the 
# answers the variable how much will check if its an int (number ) after whit elif and else we make
# diferents path that will executed depending on the answer the user give us.
def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you gonna move the bear?")
    bear_moved =False
    # Here we have another funtion and after we declare the funtion and we print the prompt we 
    # want the user to see we declare a variable named bear move and we declare it as false 
    while True:
        choice = input("> ")
        
        if choice == "take honey":
             dead("The bear look at you and slap your face off")

        elif choice == "taunt the bear" and not bear_moved:
             print("The bear has move from the door")
             print("You can go through it now")

             bear_moved = True

        elif choice == "taunt bear"  and bear_moved:
             print("the bear gets pist off and chews your leg off")

        elif choice == "open door" and bear_moved:
             gold_room()

        else:
            print("I got no idea what that means.")
# After we use while loop and we set it as true after we take the input and depending on the answwer
# we the program see if it is the correct aswer but also after we write the corrrect aswer there is
# an option to open a door that will take us to another room and the way we call this other funtion 
# or room its by putting it beside the line we want to execute the room and close parentesis 
def cthulhu_room():
    print("Here you see the evil cthulhu.")
    print("He it whatever stares at you you go insane.")
    print("Do you flee for life or eat your head?")

    choice =input("> ")
     
    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty")
        
    else:
        cthulhu_room()

# Also by decraring choice as the input from the user whit the if statment ets we can check if a specific
# number or lether phrase or sentence are inside of choise by say it explicitly inside of double quotes 
# also and only in this room we made a litre type of loop couse at the end of the funtion if the user 
# give of something weird we can just restar the room.

def answer():
    print("Ok lets see what we got here i have a cuestion for you")
    print("Please read the question and answer the correct number depending on your choice")
    print("which filosofer says this frase:" \
          "The best way to keep a prisioner from escaping is to make sure he never knows he's in prison")
    print("1: Fyodor Dostoevsky.\
           2: Seneca")
   
    choice =input("> ")
    answerr = True

    if "1" in choice and answerr:
        print("Your right this frase apaers in his book; Ten Attribut.\
              Noise")
        print("Here is your reward")
        gift()
        
    elif "2" in choice and answerr:
        print("Wrong answer but don't worry we have more questions.")
        flex()

    else:
        dead("The worse answer always gonna be the silent.")

# This is my own funtion after the message i disply whit print i ask a question whit print whit two options
# and depending on the answer we have other two room i create this funtion sttar by decraring choice as input 
# and after declare my variable answerr as true after whit the statement we check if the answer we want was 
# introduce in the input and depending on the answer the user have three posible option whit the other two 
# path i create the third one is dead.

def gift():
    print("""A winding path, unseen, unknown,
Where sunlight streams, and shadows groan.
Each step I take, a whispered prayer,
For courage found in thin, cool air.""")
    exit(0)

# Here i print a message and after i call the funtion exit from sys librarie that funtion help you count and know 
# whit kinf a error you are receiving 0 mean no error or succes any number else is a type of error byt also i print
# a poem as a reward for the user if he gets the correct answer
def flex():
    print("What is the chiken so silly?")

    choice =input("> ")
    if "Becauseeee" in choice:
        print("Are you plying whit me?")
        print("I'm joking! Good job!")
        exit(0)

    elif "because" in choice:
        print("It's not because it's; Becauseeee")
        
    else:
        dead("I don't know why i even asking this fool")
# This other funtion just tell a joke and depending on the answers it will print a diferent message.

def dead(why):
    print(why, "Good job!")
    exit(0)
# This funtion call dead its all over our program and its a simple funtion it takes one argument
# inside name dwhy and after it prints this variable it print the good job also the variable why
# will change couse why its just a place holder for the massege you will get when you fail and 
# also this massage can change.

def start():
    print("You are in a dark room.")
    print("There's a door to your right and left.")
    print("Which one do you take.")
    
    choice = input("> ")
    
    if choice == "left":
        bear_room()

    elif choice == "right":
        cthulhu_room()
        
    elif choice== "secret":
        answer()

    else:
        dead("You stumble araund the room until you starve.")
start()
# And lastly this is basically our main funtion is the encharge of initialize every thing four
# me couse is the only one call in the last line of code also the first one to be print and in 
# this funtion we store the necesary for the program to star couse this is the funtion how connect all the rooms.