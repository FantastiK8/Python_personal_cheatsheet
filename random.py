##############################
# TRANSLATE() FUNCTION          
# for removing punctuation symbols from a string/sentence.
##############################

import string
s = "string....!"
translator = str.maketrans('','', string.punctuation)
s = s.translate(translator)
#output: s = "string"

##############################
# .ISSPACE()
#############################
char = 'c'
char.isspace() # --> returns boolean False because the char is 'c' not a space

##############################
# PYTHON RETURNING IN ONE LINE IF STATEMENT
#############################
return "empty" if len(arr) == 0 else "not empty"

##############################
# ONE LINE FOR LOOP
##############################
print([i**2 for i in range(10)])

#CREATING A LIST
list = [i**2 for i in range(10)]

##############################
# ORD()
##############################

char = 'a'
ord(char) # gives the interger under which it is saved in the memory
# example of creating an array full of ord intergers of English alphabet
unique_char_arr_ord = [ord_ for ord_ in range(ord('a'), ord('z'))]   



##############################
# __slots__
##############################
(Python) Save RAM, use __slots__ . You can use __slots__ when defining your python classes to save up to 40-50% memory usage if you don't need to dynamically set class properties: https://book.pythontips.com/en/latest/__slots__magic.html 

An iterator is any object in Python which has a next (Python2) or __next__ method defined
    • Python ships with a module that contains a number of container data types called Collections. 
    • Unlike dict, with defaultdict you do not need to check whether a key is present or not
    • __slots__ can improve the efficiency of a python class by up to 40%!


##############################
# FIDN OUT IF ARRAY IS EMPTY
##############################
arr = []
if not arr:
    pass