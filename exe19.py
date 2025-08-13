def cheese_and_crackers(cheese_count, boxes_of_crackers):
     print(f"You have {cheese_count} cheses.")
     print(f"You have {boxes_of_crackers} boxes of crackees!")
     print("Man that's enough for a party.")
     print("Get a blanket. \n")
# In this 5 lines above we are doing a couple of things first we are makeing our aun funtion
# and the way we do it is using the word def for define and after we give the funtion a name this name can be whatever 
# and after we put 2 arguments inside of the parentecis its not a fundamental part of a funtion to give 2 arguments,
# our funtion can be whit out arguments or whit more than two arguments but this program take two so every time we
# call the funtion we have to give two arguments inside of the parentecis and it can be words, names, variables, numbers 
# or math operation etc.
# The second line print the amount of chess thats gonna depends onthe number, word..... etc that we give or use.
# The third line does the same but with the second argument that count the amount of boxes of clackers.
# The fourt line just print a message.
# And last this line print another message but after it prints a new line whit the comand \n.


print("We can just give the funtion numbers directly")
cheese_and_crackers(20,30)
# Here is our first way of giveing arguments to our funtion and it is with just numbers two argguments, two numbers

print("Or we can use variables from our script: ")
amount_of_chese = 10
amount_of_clackers = 50
cheese_and_crackers(amount_of_chese, amount_of_clackers) 
# This 4 lines above of this line just does a couple of things first we print a message with the print funtion.
# After we define a variable named amount of chese and we said that its equal to 10.
# And here we have another variable named amount of clackers that we just define as equal to 50.
# And lastly we have our funtion takeing the two variables as arguments.
print("we can even do math inside too: ")
cheese_and_crackers(10+20, 5+6)
# Here we are doing math inside of the funtion and we are passing the math
# as our arguments and i know it's kinda obvuis but you can do that whit */-

print("And we can convine the two variables whit math")
cheese_and_crackers(amount_of_chese +100 , amount_of_clackers + 1000)
# Here we are convined the two ways of giving argument to a funtion into one
# we are useing tha variables with math in the same funtion


print("This is mine. ")
# This print funtion is here just to enfasize that this part is ours 
mine = amount_of_chese*5 , amount_of_clackers*5 
# This variable called mine its equal to the variable amaount of cheses multiply by 5
# And the variable amount of clackers multiply by 5
yours = amount_of_chese*5 ,amount_of_clackers*5
# This variable called yours its equal to the variable amaount of cheses multiply by 5
# And the variable amount of clackers multiply by 5
cheese_and_crackers(mine,yours)
# This is the name of the funtion here we are putin two variables inside.