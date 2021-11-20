        
 ###################################
 # NOTE NOTE NOTE BIG O!!!
 ################################### 
 # BIG O for lists and operations with them.
 # https://wiki.python.org/moin/TimeComplexity 
 # 
 #       
 
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
# Single LinkedList 
#https://realpython.com/linked-lists-python/
# "How to Use Doubly Linked Lists" is at the same website but much lower
# another link with some same logic for single linkedlists https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# https://stackabuse.com/python-linked-lists/
###################################
# Practical Applications: used to implement QUEUES, STACKS, GRAPHS or
# LIFECYCLE MANAGEMENT for an operating system application
# LinkedList are not itterable!!! and can only acces the first node directly.
# the first node has link to the next one and the next one to the next one...
# untill the last one has next NONE

# Linked lists differ from lists in the way that they store elements in memory. 
# While lists use a contiguous memory block to store references to their data, 
# linked lists store references as part of their own elements.

# Node has info about DATA (value) and NEXT (following node)


# How to Create a Linked List
# The only information you need to store for a linked list is where the list starts 
# (the head of the list).

# Node Class needs info about two main elements of every single node: 
# data and next. You can also add a __repr__ to both classes to have a more helpful 
# representation of the objects:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    # With the modification (including nodes), creating linked lists to use in the examples
    #  below will be much faster.
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

#Have a look at an example of using the above classes to quickly create a linked list 
#with three nodes:

>>> llist = LinkedList()
>>> llist
None

>>> first_node = Node("a")
>>> llist.head = first_node
>>> llist
a -> None

>>> second_node = Node("b")
>>> third_node = Node("c")
>>> first_node.next = second_node
>>> second_node.next = third_node
>>> llist
a -> b -> c -> None


######## HOW TO traverse/itterate linkedList ?
# create an __iter__ to add the same behavior to linked lists that you would 
# expect from a normal list:

def __iter__(self):
    node = self.head
    while node is not None:
        yield node        # to find what is yield doing https://realpython.com/introduction-to-python-generators/#understanding-the-python-yield-statement
        node = node.next
# The method above goes through the list and yields every single node. The most important 
# thing to remember about this __iter__ is that you need to always validate that the 
# current node is not None. When that condition is True, it means you’ve reached the 
# end of your linked list.

# After yielding the current node, you want to move to the next node on the list. 
# That’s why you add node = node.next. Here’s an example of traversing a random list 
# and printing each node:

>>> llist = LinkedList(["a", "b", "c", "d", "e"])
>>> llist
a -> b -> c -> d -> e -> None

>>> for node in llist:
...     print(node)
a
b
c
d
e

# you might see the traversing defined into a specific method called traverse(). 
# However, using Python’s built-in methods to achieve said behavior makes this linked 
# list implementation a bit more Pythonic.

####
# INSERTING A NODE
# Insertiong a node at the BEGINING: add_first() for the class LinkedList:
def add_first(self, node):
    node.next = self.head
    self.head = node

# In the above example, you’re setting self.head as the next reference of the new node 
# so that the new node points to the old self.head. After that, you need to state that 
# the new head of the list is the inserted node.

#Here’s how it behaves with a sample list:

>>> llist = LinkedList()
>>> llist
None

>>> llist.add_first(Node("b"))
>>> llist
b -> None

>>> llist.add_first(Node("a"))
>>> llist
a -> b -> None

# Inserting at the END: 
# Inserting a new node at the end of the list forces you to traverse the whole linked list 
# first and to add the new node when you reach the end. You can’t just append to the end 
# as you would with a normal list because in a linked list you don’t know which node is last.

def add_last(self, node):
    if self.head is None:
        self.head = node
        return
    for current_node in self:
        pass
    current_node.next = node

# First, you want to traverse the whole list until you reach the end (that is, until the 
# for loop raises a StopIteration exception). Next, you want to set the current_node as 
# the last node on the list. Finally, you want to add the new node as the next value of 
# that current_node.

def add_last(self, node):
    if self.head is None:
        self.head = node
        return
    for current_node in self:
        pass
    current_node.next = node

>>> llist = LinkedList(["a", "b", "c", "d"])
>>> llist
a -> b -> c -> d -> None

>>> llist.add_last(Node("e"))
>>> llist
a -> b -> c -> d -> e -> None

>>> llist.add_last(Node("f"))
>>> llist
a -> b -> c -> d -> e -> f -> None


### Inserting a new node BETWEEN other nodes:
# Here’s a method that adds a node after an existing node with a specific data value:

def add_after(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    for node in self:
        if node.data == target_node_data:
            new_node.next = node.next
            node.next = new_node
            return

    raise Exception("Node with data '%s' not found" % target_node_data)

>>> llist = LinkedList()
>>> llist.add_after("a", Node("b"))
Exception: List is empty

>>> llist = LinkedList(["a", "b", "c", "d"])
>>> llist
a -> b -> c -> d -> None

>>> llist.add_after("c", Node("cc"))
>>> llist
a -> b -> c -> cc -> d -> None

>>> llist.add_after("f", Node("g"))
Exception: Node with data 'f' not found

### Now, if you want to implement add_before(), then it will look something like this:

def add_before(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        return self.add_first(new_node)

    prev_node = self.head
    for node in self:
        if node.data == target_node_data:
            prev_node.next = new_node
            new_node.next = node
            return
        prev_node = node

    raise Exception("Node with data '%s' not found" % target_node_data)

>>> llist = LinkedList()
>>> llist.add_before("a", Node("a"))
Exception: List is empty

>>> llist = LinkedList(["b", "c"])
>>> llist
b -> c -> None

>>> llist.add_before("b", Node("a"))
>>> llist
a -> b -> c -> None

>>> llist.add_before("b", Node("aa"))
>>> llist.add_before("c", Node("bb"))
>>> llist
a -> aa -> b -> bb -> c -> None

>>> llist.add_before("n", Node("m"))
Exception: Node with data 'n' not found


### HOW TO REMOVE NODES
# To remove a node from a linked list, you first need to traverse the list until you find 
# the node you want to remove. Once you find the target, you want to link its previous and 
# next nodes. This re-linking is what removes the target node from the list.

# That means you need to keep track of the previous node as you traverse the list. Have a 
# look at an example implementation:

def remove_node(self, target_node_data):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        self.head = self.head.next
        return

    previous_node = self.head
    for node in self:
        if node.data == target_node_data:
            previous_node.next = node.next
            return
        previous_node = node

    raise Exception("Node with data '%s' not found" % target_node_data)

>>> llist = LinkedList()
>>> llist.remove_node("a")
Exception: List is empty

>>> llist = LinkedList(["a", "b", "c", "d", "e"])
>>> llist
a -> b -> c -> d -> e -> None

>>> llist.remove_node("a")
>>> llist
b -> c -> d -> e -> None

>>> llist.remove_node("e")
>>> llist
b -> c -> d -> None

>>> llist.remove_node("c")
>>> llist
b -> d -> None

>>> llist.remove_node("a")
Exception: Node with data 'a' not found





















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
# LISTS and ARRAYS
# https://note.nkmk.me/en/python-list-append-extend-insert/
# https://www.programiz.com/python-programming/methods/list/copy
# this link has valid explanations of each METHOD of list https://www.programiz.com/python-programming/methods/list/remove
# this link has many other things from python!!! https://www.learnbyexample.org/python-list/
###################################

#####Python List METHODS:

# Python List index()
# Python List append()
# Python List extend()
# Python List insert()
# Python List remove()
# Python List count()
# Python List pop()
# Python List reverse()
# Python List sort()
# Python List copy()
# Python List clear()


# Add an item to the end: append()
# Combine lists: extend(), + operator
# Insert an item at specified index: insert()
# Add another list or tuple at specified index: slice
# NOTE insert() is an O(n) operation and is not efficient. 

# For removing elements from a list: 
# Remove a specific item from the list .remove() 
# Remove the last item .pop(). BUT ALSO WORKS AT SPECIFIC POSSITION .pop(index)
# 
#examples: 
### .append()

l = list(range(3))
print(l)
# [0, 1, 2]

l.append(100)
print(l)
# [0, 1, 2, 100]

l.append('new')
print(l)
# [0, 1, 2, 100, 'new']

# A list is also added as one item, not combined.
l.append([3, 4, 5])
print(l)
# [0, 1, 2, 100, 'new', [3, 4, 5]]

### extend(), + operator
# You can combine another list or tuple at the end of the list with extend().
#  All items are added to the end of the original list.

l = list(range(3))
print(l)
# [0, 1, 2]

l.extend([100, 101, 102])
print(l)
# [0, 1, 2, 100, 101, 102]

l.extend((-1, -2, -3))
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3]

#In the case of a string, each character is added one by one.

l.extend('new')
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w']


# insert().
# Set the index for the first parameter and the item to be inserted for 
# the second parameter. The index at the beginning is 0 (zero-based indexing).
# For negative values, -1 means one before the end.
# NOTE that insert() is an O(n) operation and is not efficient. 

# NOTE The deque type is provided in the standard library collections module 
# as a type to add an item to the head with O(1). For example, if you want to treat data as a queue (FIFO), it is more efficient to use deque.

l = list(range(3))
print(l)
# [0, 1, 2]

l.insert(0, 100)
print(l)
# [100, 0, 1, 2]

l.insert(-1, 200)
print(l)
# [100, 0, 1, 200, 2]

# the list is added as a single item, not combined.

l.insert(0, [-1, -2, -3])
print(l)
# [[-1, -2, -3], 100, 0, 1, 200, 2]


##Add another list or tuple at specified index: slice
#If you specify a range using slice and assign another list or tuple, 
# all items will be added.

l = list(range(3))
print(l)
# [0, 1, 2]

l[1:1] = [100, 200, 300]
print(l)
# [0, 100, 200, 300, 1, 2]

#You can also replace the original item. All items in the specified 
# range are replaced.

l = list(range(3))
print(l)
# [0, 1, 2]

l[1:2] = [100, 200, 300]
print(l)
# [0, 100, 200, 300, 2]

###
#The remove() method removes the first matching element (which is passed as 
# an argument) from the list.

#Example
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)


# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]



####=======================
# The copy() method returns a shallow copy of the list.

#Example
# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()

print('Copied List:', numbers)

# Output: Copied List: [2, 3, 5]


#---------------
# Copy List Using Slicing Syntax
# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]


# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)

# Output

# Old List: ['cat', 0, 6.7]
# New List: ['cat', 0, 6.7, 'dog']



#--------
# List copy using = operator
# NEVER USE = operator for coping lists!!!!
# If you modify new_list, old_list is also modified. It is because 
# the new list is referencing or pointing to the same old_list object.

old_list = [1, 2, 3]

# copy list using =
new_list = old_list


# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)

#output
# Old List: [1, 2, 3, 'a']
# New List: [1, 2, 3, 'a']



#==========================
# The index() method returns the index of the specified element in the list.
# Syntax of List index()
# The syntax of the list index() method is:

# list.index(element, start, end)
# list index() parameters
# The list index() method can take a maximum of three arguments:

# element - the element to be searched
# start (optional) - start searching from this index
# end (optional) - search the element up to this index


animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')

print(index)

#===========
# List count()
# The count() method returns the number of times the specified element appears in the list.
# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]
# check the count of 2
count = numbers.count(2)
print('Count of 2:', count)

# Output: Count of 2: 3

#===========
# List reverse()
# The reverse() method reverses the elements of the list.

#Example
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()
print('Reversed List:', prime_numbers)
# Output: Reversed List: [7, 5, 3, 2]


####
# Example 2: Reverse a List Using Slicing Operator
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]


# updated list
print('Updated List:', reversed_list)
# Output
# Original List: ['Windows', 'macOS', 'Linux']
# Updated List: ['Linux', 'macOS', 'Windows']

####

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

#==================
### SORT AND SORTED!!!!
# NOTE: The simplest difference between sort() and sorted() is: sort()
#  doesn't return any value while, sorted() returns an iterable list.
#The sort() method sorts the elements of a given list in a specific ascending 
# or descending order.

#Example
prime_numbers = [11, 3, 7, 5, 2]

# sort the list
prime_numbers.sort()
print(prime_numbers)

# Output: [2, 3, 5, 7, 11]

#####
# sort() Syntax
# The syntax of the sort() method is:
list.sort(key=..., reverse=...)
#Alternatively, you can also use Python's built-in sorted() function for 
# the same purpose.
sorted(list, key=..., reverse=...)

# sort() Parameters
# By default, sort() doesn't require any extra parameters. However, it has two 
# optional parameters:

# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison. 

# sort() Return Value
# The sort() method doesn't return any value. Rather, it changes the original list.

# If you want a function to return the sorted list rather than change the original 
# list, use sorted().

# Sort in Descending order
# The sort() method accepts a reverse parameter as an optional argument.

# Setting reverse = True sorts the list in the descending order.

list.sort(reverse=True)
# Alternatively for sorted(), you can use the following code.

sorted(list, reverse=True)

##Example: Sort the list using key
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')




#====================

fitted_bol_arr = [None] * len(nums) # WILL GIVE an array in the 
#size of nums and all will be None or False depending what you want

#### USE WHILE LOOP when you want to change the "i" index to different one.


##############
# (Python) In the latest python version you can merge two dicts using the merge operator: 
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
x | y
#{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
y | x
#{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}







############################
# HOW TO MAKE CLASS for example own LinkedList itterable!
# by default our own created classes are not iterable.
# CREATE ITERATOR WITHIN YOUR CLASS
# https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
############################

#you always need a __iter__ method for the iterator class.
# IF you do not use LinkedList but list you would probalby use 
# self._index = 0 in iterator in __init__ viz the above link tutorial

class LinkedListIterator:
    def __init__(self, head):
        self.current = head
     
    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def add(self, item): 
        new_node = Node(item) ## i suppose a new class to initialise node?
        new_node.set_next(self.head)
        self.head = new_node
#Now that your class is iterable, you can use "for...in" loop:

test_list = LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
for item in test_list:
    print(item)





###################################
#  How to Use Generators and yield in Python
# https://realpython.com/introduction-to-python-generators/#understanding-the-python-yield-statement
# Understanding the Python Yield Statement is rather in the first middle end of the tutorial
###################################



###################################
# How to use MODULO operator %
#  https://realpython.com/python-modulo-operator/
###################################




###################################
#  statement del
#https://www.programiz.com/python-programming/del
###################################

# delete obj_name
del obj_name
##

#Example 1: Delete an user-defined object
# In the program, we have deleted MyClass using del MyClass statement.
class MyClass:
    a = 10
    def func(self):
        print('Hello')

# Output: 
print(MyClass)

# deleting MyClass
del MyClass

# Error: MyClass is not defined
print(MyClass)

##
# Example 2: Delete variable, list, and dictionary

my_var = 5
my_tuple = ('Sam', 25)
my_dict = {'name': 'Sam', 'age': 25}

del my_var
del my_tuple
del my_dict

# Error: my_var is not defined
print(my_var)

# Error: my_tuple is not defined
print(my_tuple)

# Error: my_dict is not defined
print(my_dict)

####
# Example 3: Remove items, slices from a list
# The del statement can be used to delete an item at a given index. It can also be 
# used to remove slices from a list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# deleting the third item
del my_list[2]

# Output: [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list)

# deleting items from 2nd to 4th
del my_list[1:4]

# Output: [1, 6, 7, 8, 9]
print(my_list)

# deleting all elements
del my_list[:]

# Output: []
print(my_list)

####
# Example 4: Remove a key:value pair from a dictionary
person = { 'name': 'Sam',
  'age': 25,
  'profession': 'Programmer'
}

del person['profession']

# Output: {'name': 'Sam', 'age': 25}
print(person)

####
# del With Tuples and Strings
# You can't delete items of tuples and strings in Python. It's because tuples 
# and strings are immutables; objects that can't be changed after their creation.

my_tuple = (1, 2, 3)

# Error: 'tuple' object doesn't support item deletion
del my_tuple[1]

#However, you can delete an entire tuple or string.

my_tuple = (1, 2, 3)

# deleting tuple
del my_tuple





###################################
#  RANDOM
###################################




###################################
#  
###################################



###################################
#  
###################################


###################################
# Slicing 
###################################

string[1:] # means skippping the first letter in the string.

######
## How to start a for loop at index 1 in Python
a_list = ["a", "b", "c"]

#Iterate through `a_list` starting at index `1`
for item in a_list[1:] :
    print(item)
# OUTPUT
# b
# c