        
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

# to reverse a part of the string in place 
a = [1,2,3,4,5]
a[2:4] = reversed(a[2:4])  # This works!
a[2:4] = [0,0]             # This works too.
a[2:4] = a[2:4][::-1]           # This works 


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

# (Python 3.2+) -  The lru_cache decorator allows easy function caching depending
#  on the arguments, it can save time for for functions that are frequently called 
#  with the same arguments.
#Ex:

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# >>> print([fib(n) for n in range(10)])
# # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


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

#####


#Slice notation in short:

[ <first element to include> : <first element to exclude> : <step> ]
list[start:stop:step_size]

#If you want to include the first element when reversing a list, leave the 
# middle element empty, like this:

list[::-1]

