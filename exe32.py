the_count =[1,2,3,4,5]
fruits =['apples', 'orange', 'pears', 'apricots']
change =[1,'pennies', 2, 'dimes', 3, 'quarters']
# In Python, a list is a built-in data structure used to store an ordered, mutable collection of items.
# Lists are highly versatile and can contain elements of various data types, including integers, floats, strings,
# booleans, or even other lists.

# len(list): Returns the number of items in the list.
# list.sort(): Sorts the list in ascending order.
# list.reverse(): Reverses the order of elements.
# list.count(value): Returns the number of occurrences of a specific value.
# list.clear(): Removes all elements from the list.
# This first kind of loop goes through a list

for number in the_count:
     print(f"This is the number {number}")


# Same above.
for fruit in fruits:
     print(f"A fruit of type {fruit}")

# Also we can go through mixed list too
# Notice we have to use {} since we don't know whats inside.
for i in change:
     print(f"I got {i}")
# We can also build list to firs star whiht a empty one.
# The range() function in Python generates a sequence of numbers, primarily used for iteration in for loops.
# It returns a "range object," which is an immutable sequence type that efficiently represents the range by storing only the start,
# stop, and step values rather than generating all numbers in memory at once. 
# This funtion has three uses 1 it will count from the number it beggins until the number before you put.
# It only work whit integers
# 2 we ccan use range to increment or dicrement numbers in a loop
# also it's inmutable after we creat a range the values cannot be change.
elements =[]

# Then use the range funtion to do 0 to counts 5

for i in  range(0, 6):
  print(f"Adding  to the list.")
     # append it's a funtion that list understand
  elements.append(i)

for i in elements:
     print(f"Elements was: {i}")




