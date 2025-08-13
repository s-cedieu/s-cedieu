print("""You enter in a dark room whit two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
     print("There ia a giant bear here eating a cheese cake.")
     print("What do you do?")
     print("1. Take the cake.")
     print("2. Scream at the bear ")

     bear = input("> ")

     if bear == "1":
          print("The bear eats your face off. Good job!")

     elif bear == "2":
          print("The bear eats your legs off. Good job.")

     else:
          print(f"Well, doing {bear} bear is probably better.")
          print("Bears run away.")


elif door == "2":
     print("You stare into the endlees abyss of Cthulhu's retina.")
     print("1. Blueberries.")
     print("2. Yellow jacket clothespins.")
     print("3. Understanding revolvers yelling melodies.")


     insanity = input("> ")

     if insanity == "1" or insanity == "2":
          print("Your body survives powered by a mind of jello.")
          print("Good joob")
     
     else:
          print("The insanity rots your eyes into a pool of muck.")
          print("Good job.")

else:
     print("You stumble around fall into a knife and die. Good job.")
# This is simple game to Prctice if, elif, and else statemant.
