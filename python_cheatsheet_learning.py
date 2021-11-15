        
        
 
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
# Slicing 
###################################

string[1:] # means skippping the first letter in the string.


