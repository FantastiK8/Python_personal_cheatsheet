        
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



##### putting all char in a sentence/string into small letters.
sentence = "Hello World"
str.lower(sentence) 
#output: sentence = "hello world"


##############################
# BUFFER???





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
#  Statements 
###################################
# PASS
# RETURN
# CONTINUE
# YIELD
#############

# PASS

# https://www.educative.io/edpresso/what-is-pass-statement-in-python
# In Python, pass is a null statement. The interpreter does not ignore a pass statement, 
# but nothing happens and the statement results into no operation.
# The pass statement is useful when you don’t write the implementation of a function 
# but you want to implement it in the future.

#So, to avoid compilation errors, you can use the pass statement.

# This functions prints the number if its not 2
def display(number):
  
  if number is 2:
    pass # Pass statement
  else:
    print ("Number: ", number)
    
display(2)
display(3)

#or#

def addition(num1, num2):
  # Implementation will go here 
  pass # Pass statement

addition(2, 2)

#or#

'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

# RETURN
# CONTINUE
# YIELD



###################################
#  OPERATORS
# https://www.w3schools.com/python/python_operators.asp
###################################
# Python Assignment Operators
# Assignment operators are used to assign values to variables:

Operator	Example		
*=	        x *= 3	x = x * 3	
/=	        x /= 3	x = x / 3	
%=	        x %= 3	x = x % 3	
//=	        x //= 3	x = x // 3	
**=	        x **= 3	x = x ** 3	
&=	        x &= 3	x = x & 3	
|=	        x |= 3	x = x | 3	
^=	        x ^= 3	x = x ^ 3	
>>=	        x >>= 3	x = x >> 3	
<<=	        x <<= 3	x = x << 3

#---------------
# Python Logical Operatiors
# "not" Reverse the result, returns False if the result is true 
not(x < 5 and x < 10)
#----------------

Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

#Operator "in" 	Returns True if a sequence with the specified value is present in the object	
x in y

# Operator "not in"	Returns True if a sequence with the specified value is not present in the object	
x not in y
#-----------------
#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description
& 	        AND	                    Sets each bit to 1 if both bits are 1
|	        OR	                    Sets each bit to 1 if one of two bits is 1
 ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
~ 	        NOT	                    Inverts all the bits
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, 
                                    and let the rightmost bits fall off



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

