from sys import argv
# Here we have alibrary where we get the argv funtion from 

script, user_name, last_name, = argv
# The argv funtion its use to unblok varius variebles in this 
# case we have only two beside script this funtion give  every variable a meaning 
prompt = '%% '
# Here we have a variable named prompt thats equal to the percent symbol twice 

print(f"Hi {user_name}, I'm the {script} script. ")
print(f"I'd like to ask you a few questions {user_name}. ")
print(f"Do you like me {user_name}?")


likes = input(prompt)
# here we are using the input funtion to do two things first we are saying taht likes its equal
# to the input we gonn take and at the same time we are saying input gonna prompt each time we give an input 
print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"Where kind of computer do you have?")
computer = input(prompt)

print(f"What's your last name ?")
last_name = input(prompt)


print(f""""
Alright, so you said {likes} about liking me.
You lives in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Your last name is {last_name} rihgt.
""""")
