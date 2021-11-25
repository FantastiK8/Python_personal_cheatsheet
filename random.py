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


