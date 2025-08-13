people = 19
cats =9
dogs = 10

if people < cats:
     print("Too many cats, the word is doomed!.")

if people >cats:
     print("Not so many cats the word is saved.")

if people < dogs:
     print("The word is drooledon!.")

if people >dogs:
     print("The word is dry.")

# An if stament is use to create a branch into your code that said is this bool
# is true go ahead an do the lines indented to the if statement and is id not true
# the program will ignore the branch a go to the next one.

dogs +=5
# What does += mean? The code x += 1 is the same as doing x = x + 1 but involves less
# typing. You can call this the “increment by” operator. The same goes for -= and many other
# expressions you’ll learn later.
if people <= dogs:
     print("People are less or equal to dogs.")

if people >= dogs:
     print("People are greather or equal to dogs.")

if people == dogs:
     print("Peaple are equal to dogs.")

#1. What do you think the if does to the code under it?

# I think that the if statement cheks if a condition is true
# or false and then make an action depening on the instrucction we give to thr program 

#2. Why does the code under the if need to be indented four spaces?

# Couse is indented to define its scope and indicate that it belongs to that specific block.
# While the Python language itself does not strictly enforce four spaces, this is a widely adopted
# and recommended convention within the Python community.


#3. What happens if it isn’t indented?

# The pep 8 waht is an especific style that pythno use will give us an error couse the compiler
# don't gonna know to which block of code this line belong

#4. Can you put other Boolean expressions from Exercise 27 in the if-statement? Try it.

# Yes and yes

#5. What happens if you change the initial values for people, cats, and dogs?

# We just have to change it from every where but the variables can have any name
