        
        
 
 ###################################
 # Switcher example for two imputs at the same time - possible for more
 ###################################      
        
numeral_sys_1 = "Binary"
numeral_sys_2 = "Decimal" 
numeral_dict = {
("Hexadecimal", "Decimal"    ) : 1,
("Hexadecimal", "Binary"     ) : 2,
("Decimal",     "Hexadecimal") : 4, 
("Decimal",     "Binary"     ) : 6,
("Binary",      "Hexadecimal") : 5,
("Binary",      "Decimal"    ) : 3
}
numeral_dict.get((numeral_sys_1, numeral_sys_2), 0)


###################################
# How to shift a block of code left/right by one space in VSCode?
# https://stackoverflow.com/questions/47903209/how-to-shift-a-block-of-code-left-right-by-one-space-in-vscode
 ###################################

# USE: 
# move right:ctrl ] 
# move left: ctrl [


###################################
# STRINGS
###################################
# Python allows concatination of strings/letters


"Hello" + "World" # => "Hello world"


# A string can be treated as a list of characteurs


"Hello World!"[0]  # => H

# possible to use f-strings or formatted string literals 

name = "Kat"
f"My name is {name}." # "My name is Kat."

f"{name} name is {len(name)} characteurs long." # "Kat is 3 characteurs long."

# Same as in Java for comparison of strings use --> is <-- to compare object because 
# String is an object and symbol of equality--> == <-- is used for e.g. numbers.

"Kat" is "Kat" # => True
"Hello" is "Kat" # => False


###################################
# LinkedList 
#https://realpython.com/linked-lists-python/
#
###################################
# Practical Applications: used to implement QUEUES, STACKS, GRAPHS or
# LIFECYCLE MANAGEMENT for an operating system application



####################
# collections.deque
# https://realpython.com/linked-lists-python/
####################
# In Python, there’s a specific object in the collections 
# module that you can use for linked lists called deque 
# (pronounced “deck”), which stands for double-ended queue.

collections.deque #uses an implementation of a linked list 
# in which you can access, insert, or remove elements from 
# the beginning or end of a list with constant O(1) performance.


#First, you need to create a linked list. You can use the 
# following piece of code to do that with deque:

from collections import deque
deque()
#deque([])

#The code above will create an empty linked list. If you want 
# to populate it at creation, then you can give it an iterable 
# as input:

deque(['a','b','c'])
#deque(['a', 'b', 'c'])

deque('abc')
#deque(['a', 'b', 'c'])

deque([{'data': 'a'}, {'data': 'b'}])
#deque([{'data': 'a'}, {'data': 'b'}])

#When initializing a deque object, you can pass any iterable as 
# an input, such as a string (also an iterable) or a list of objects.

#Now that you know how to create a deque object, you can interact 
# with it by adding or removing elements. You can create an abcde 
# linked list and add a new element f like this:

>>> llist = deque("abcde")
>>> llist
#deque(['a', 'b', 'c', 'd', 'e'])

>>> llist.append("f")
>>> llist
#deque(['a', 'b', 'c', 'd', 'e', 'f'])

>>> llist.pop()
#'f'

>>> llist
#deque(['a', 'b', 'c', 'd', 'e'])

#Both append() and pop() add or remove elements from the right side 
#of the linked list. However, you can also use deque to quickly add 
# or remove elements from the left side, or head, of the list:

>>> llist.appendleft("z")
>>> llist
#deque(['z', 'a', 'b', 'c', 'd', 'e'])

>>> llist.popleft()
#'z'

>>> llist
#deque(['a', 'b', 'c', 'd', 'e'])

#Adding or removing elements from both ends of the list is pretty 
# straightforward using the deque object. Now you’re ready to learn 
# how to use collections.deque to implement a queue or a stack.

###################################
# LISTS
###################################

#In Python, you can insert elements into a list using 
#.insert() or .append(). For removing elements from a list, 
# you can use their counterparts: .remove() and .pop().

#The main difference between these methods is that you use 
# .insert() and .remove() to insert or remove elements at 
# a specific position in a list, but you use .append() and 
# .pop() only to insert or remove elements at the end of a list.






##############
# (Python) In the latest python version you can merge two dicts using the merge operator: 
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
x | y
#{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
y | x
#{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}















###################################
# Slicing 
###################################

string[1:] # means skippping the first letter in the string.


