def break_words(stuff):
     """This funtion will break up words for us."""
     words =stuff.split(' ')
     return words 
# This funtion is use to split the sentence or separate them In Python,
# the split() method is primarily used with strings to divide them into a list of substrings.
# It operates based on a specified delimiter or separator.

def sort_words(words):
     """Sorts the words."""
     return sorted(words)
# This funtion takes the split list from what use to be a sentence and swich their places remeber that
# the previus funtion takes a sentence and make them a list of substrings this funtion then take the 
# substrings and change their order or place.
def print_first_word(words):
     """Prints the first word after popping it off."""
     word =words.pop(0)
     print(word)
# This funtion is sample it takes the first word from our substrings and popping it on the terminal.
# In Python, pop() is a method available for both lists and dictionaries, used to remove and return an item.
def print_last_word(words):
     """Print the last word after popping it off."""
     word = words.pop(-1)
     print(word)
# This funtion is sample it takes the last word from our substrings and popping it on the terminal.
# In Python, pop() is a method available for both lists and dictionaries, used to remove and return an item.
def sort_sentence(sentence):
     """Takes in a full sentence and returns the sorted words."""
     words = break_words(sentence)
     return sort_words(words)
# This funtion takes our two fisrt funtion and split and sorted the list of substrings and return the sorted words to the programer.
     
def print_first_and_last(sentence):
     """Prints the first and last words of the sentense."""
     words= break_words(sentence)
     print_first_word(words)
     print_last_word(words)
# This funtion split the list of substrings and print the first and last word from the substring list.

def print_first_and_last_sorted(sentence):
     """Sorts the words the prints the first and last one."""
     words = sort_sentence(sentence)
     print_first_word(words)
     print_last_word(words)

# And lastly this funtion takes the remaind of the list and print the last and first lether from that reamainder.

