formatter = "{} {} {} {}"
#This line make a variable named formather that equal or the same as four curly brakets
#Also the number of curly braquets mether because every pair off curly braquet is 
# an spot for each one of the things we want to format
print(formatter.format(1, 2, 3, 4))
#This line print or variable the sustitution of the curly bracquets for the numbeer we trying to format
#instead of four curly brakets we have four nuber one for each brakes
print(formatter.format("one", "two", "three", "four"))
#Here its more off the same we are printting our variable and whit the format we are giving
#  changeing the curly brakets for letter numbers 
print(formatter.format(True, False, False, True))
#This line do the same changeing the curly brakets for true and false respectively
print(formatter.format(formatter, formatter, formatter, formatter))
#Hre in this print funtiin we print four times the variable formatter whta give us 12 curly braquests 
print(formatter.format(
     "Del cielo cayo una rosa",
     "de tan bonito color ",
     "alguien lo levanto ",
     "y olia a alcamphor"
))
# Here in this one we just print four line of string