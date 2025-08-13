print("Let's practice everything. ")
print('You\'d need ro know\' bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
# This jut print a messge whit some especial spaces caraters line \n for new line and \t for new tab.
poem ="""
\tThe lovely word 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere thee is none.
"""
# Here we have a variable named poem that have big string inside and in python when we want to print
# a long message we should use three pair of double quotes also here we are using again the new tab \t and new line\n

print("-------------")
print(poem)
print("-------------")
# Here we are playing whit print this three lines of code aloe us to put the variable poem inside of the other two variables

five= 10-2+3-6
print(f"This should be five: {five}")
# Here we have a varible named five that is equal to a math operation that gonna ended up giving us 5 
# and after we have a print funtion that print a mesagge and also whit the f format funtion we store the variable five inside 

def secret_formula(started):
     jelly_beans=started *500
     jars = jelly_beans /1000
     crates = jars /100
     return jelly_beans, jars, crates
# Here we have our funtion taht takes one argument that down we can see that its is equal to 10000 
# the first thing our funtion does is make variable named jelly beans that is equal to the strted 
# (10000) multiplying by 500 what give us 5000000 after we have another funtion named jars that 
# is equal to the variable named jelly beans which is 5000000 divided by 1000 that are equal to 5000
# after we have our third variable named creates that are equal to jars which is 5000 divided by 100
# What left us 50 and finali whit the funtion return we give back all the values 

start_point =10000
beans, jars, crates =secret_formula(start_point)
# This two lines let us make the sttarting point 10,000
# Remember taht this is another way to format a string
print("Whit a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point /10
# This line divide all the values we obteing from the funtion and dived them by 10 this is why
# the second whay give us less thah the firs one 

print("We can also do that this way:")
formula= secret_formula(start_point)
# This is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.". format(*formula))