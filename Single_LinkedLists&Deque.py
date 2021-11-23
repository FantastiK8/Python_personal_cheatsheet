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

#============================
# HOW TO COPY/CLONE LINKED LIST
# https://www.techiedelight.com/clone-given-linked-list/

# 1. Naive Approach

import copy 
class _ListNode:
    def __init__(self, value, next_):
        self._value = copy.deepcopy(value)
        self._next = next_
        return
class List:
    def __init__(self):
        self._front = None
        self._count = 0
        return
    def addToFront(self, value):
        if self._front == None:
            self._front = _ListNode(value, None)
        else:
            buffer = _ListNode(value, self._front)
            self._front = buffer

    def addToEnd(self, value):
        current = self._front
        if current:
            while current._next != None:
                current = current._next
            current._next = _ListNode(value, None)
        else:
            self._front = _ListNode(value, None)

    def __str__(self):
        buffer = self._front
        result = ""
        while buffer._next != None:
            result+= buffer._value + " > "
            buffer = buffer._next
        result+= buffer._value
        return result

    def copy(self):
        result = List()
        buffer = self._front
        while buffer._next != None:
            result.addToEnd(buffer._value)
            buffer= buffer._next
        result.addToEnd(buffer._value)
        return result

##test:
x = List()
x.addToFront("f")
x.addToFront("e")
x.addToFront("d")
x.addToFront("c")
x.addToFront("b")
x.addToFront("a")
print(x)

##### OR
# This impleentation is little unsatisfying because the 3-step link-in is repeated
# - once for the first node and once for all the other nodes. 
# Can be prevented see next option 2 lower.


# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Function takes a linked list and returns its complete copy
def copyList(head):
 
    current = head      # used to iterate over the original list
    newList = None      # head of the new list
    tail = None         # point to the last node in a new list
 
    while current:
        # special case for the first new node
        if newList is None:
            newList = Node(current.data, None)
            tail = newList
        else:
            tail.next = Node()
            tail = tail.next
            tail.data = current.data
            tail.next = None
        current = current.next
 
    return newList
 
 
if __name__ == '__main__':
 
    # construct a linked list
    head = None
    for i in reversed(range(4)):
        head = Node(i + 1, head)
 
    # copy linked list
    copy = copyList(head)
 
    # print duplicate linked list
    printList(copy)

#----------------
# 2. Using push() function
# does not repeat 3-step link-in. this implementation
# allocate and instert the new nodes and avoid repeating that code

# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Function takes a linked list and returns a complete copy of that
# list using a dummy node using the `push()` function
def copyList(head):
 
    current = head      # used to iterate over the original list
    newList = None      # head of the list
    tail = None         # point to the last node in a new list
 
    while current:
 
        # special case for the first node
        if newList is None:
            newList = Node(current.data, newList)
            tail = newList
        else:
            tail.next = Node(current.data, tail.next)    # add each node at the tail
            tail = tail.next    # advance the tail to the new last node
        current = current.next
 
    return newList
 
 
if __name__ == '__main__':
 
    # construct a linked list
    head = None
    for i in reversed(range(4)):
        head = Node(i + 1, head)
 
    # copy linked list
    dup = copyList(head)
 
    # print duplicate linked list
    printList(dup)
 
#-----------------
#3. Using Dummy Node
# Another strategy is to use a temporary dummy node to take care of the first node case. 
# The dummy node is temporarily the first node in the list, and the tail pointer starts 
# off pointing to it. All nodes are added off the tail pointer.

# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')
 
 
# Function takes a linked list and returns a complete copy of that
# list using a dummy node
def copyList(head):
 
    current = head          # used to iterate over the original list
    dummy = Node()          # build the new list of this dummy node
 
    # point to the last node in a new list
    tail = dummy            # start the tail pointing at the dummy
 
    while current:
        tail.next = Node(current.data, tail.next)    # add each node at the tail
        tail = tail.next    # advance the tail to the new last node
        current = current.next
 
    return dummy.next
 
 
if __name__ == '__main__':
 
    # construct a linked list
    head = None
    for i in reversed(range(4)):
        head = Node(i + 1, head)
 
    # copy linked list
    dup = copyList(head)
 
    # print duplicate linked list
    printList(dup)



#============================
# N'TH NODE!
# n’th node from the end of a Linked List
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
#============================
# For example, input LinkedList = [a, b, c, d] 
# n = 3, then output is “b”
###
#Method 1 (Use length of linked list) 
###
# 1) Calculate the length of Linked List. Let the length be len. 
# 2) Print the (len – n + 1)th node from the beginning of the Linked List. 
# Double pointer concept : First pointer is used to store the address of the variable 
# and second pointer used to store the address of the first pointer. If we wish to 
# change the value of a variable by a function, we pass pointer to it. And if we 
# wish to change value of a pointer (i. e., it should start pointing to something 
# else), we pass pointer to a pointer.

# Simple Python3 program to find
# n'th node from end
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
      
class LinkedList:
    def __init__(self):
        self.head = None
  
    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Function to get the nth node from 
    # the last of a linked list 
    def printNthFromLast(self, n):
        temp = self.head # used temp variable
          
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
          
        # print count 
        if n > length: # if entered location is greater 
                       # than length of linked list
            print('Location is greater than the' +
                         ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)
  
# Driver Code        
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(35)
llist.printNthFromLast(4)

# Output: 35

# or for the same method recursive code: 
def printNthFromLast(head, n):
      
    i = 0
    if (head == None):
        return
    printNthFromLast(head.next, n)
    i+=1
    if (i == n):
        print(head.data)
      
###
# Method 2 (Use two pointers) 
# COMPLEXITY: Time Complexity: O(n) where n is the length of linked list. 
###
# Maintain two pointers – reference pointer and main pointer. Initialize both 
# reference and main pointers to head. First, move the reference pointer to 
# n nodes from head. Now move both pointers one by one until the reference 
# pointer reaches the end. Now the main pointer will point to nth node from 
# the end. Return the main pointer.
# Below image is a dry run of the above approach: 
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/

# Python program to find n'th node from end using slow
# and fast pointer
  
# Node class 
class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def printNthFromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head 
      
        count = 0 
        if(self.head is not None):
            while(count < n ):
                if(ref_ptr is None):
                    print "% d is greater than the 
                           no. pf nodes in list" %(n)
                    return
   
                ref_ptr = ref_ptr.next
                count += 1
      
        if(ref_ptr is None):
            self.head = self.head.next
            if(self.head is not None):
                 print "Node no. % d from last is % d " 
                                   %(n, main_ptr.data)
        else:
            
  
          while(ref_ptr is not None):
              main_ptr = main_ptr.next 
              ref_ptr = ref_ptr.next
  
          print "Node no. % d from last is % d " 
                                     %(n, main_ptr.data)
  
  
# Driver program to test above function
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
  
llist.printNthFromLast(4)
# Output
# Node no. 4 from last is 35 





#============================
#Python Algorithms — Implementing a FIFO Queue Using a Linked List
#https://medium.com/dm03514-tech-blog/python-algorithms-implementing-a-fifo-queue-using-a-linked-list-57cf700a6395











#=========================
# Concatenating two linked lists