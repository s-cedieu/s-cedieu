people = 829
cars = 982
trucks =7084
# Here we have three simple variables that have number t their meaning 
if cars > people:
     print("We should take the cars.")
# This if statement says that if the variables named cars are greather
# than the number of people go ahead and print the corresponding message elif
# waht means if the first brnch not run go ahed and  run this line and then stop
# so basically the aventage that we have on using elif is if the first branch is not
# true and the second its true the program will stop but if we use another if statement
# it will go trou each line no mether if is true or false.
elif cars < people:
     print("We should not take the cars.")

else:
     print("We can't decide")

if trucks > cars:
     print("That's too many trucks")

elif trucks < cars:
     print("Maybe we can take the trucks.")

else:
     print("We still can decide.")

if people > trucks or cars > people:
     print("Let's just take the trucks.")
else:
     print("Fine let's just stay home then.")
# And finally our lst statement is else this is our last option this will run if there is no mere branches.


# 1. if statement:
# The if statement is the foundation of conditional logic. It checks a single condition.
# If the condition following if evaluates to True, the indented block of code immediately below it is executed.
# If the condition is False, the code block is skipped.

# 2. elif statement:
# elif stands for "else if". It allows you to check for multiple conditions sequentially.
# An elif statement is only evaluated if the preceding if condition (and any previous elif conditions) evaluated to False.
# If an elif condition is True, its corresponding indented code block is executed, and the rest of the elif/else chain is skipped.

# 3. else statement:
# The else statement provides a fallback block of code that executes if none of the preceding if or elif conditions in the same chain were True.
# It does not require a condition itself, as it acts as a "catch-all" for all other cases.