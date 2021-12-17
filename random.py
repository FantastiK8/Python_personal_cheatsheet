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
# ORD() https://www.programiz.com/python-programming/methods/built-in/ord
# The ord() function returns an integer representing the Unicode character.
##############################
char = 'a'
ord(char) # gives the interger under which it is saved in the memory
# example of creating an array full of ord intergers of English alphabet
unique_char_arr_ord = [ord_ for ord_ in range(ord('a'), ord('z'))]   
# Example: 
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
# Output
# 53
# 65
# 36


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





##############################
# DIVE AND CONQUER APPROACH:
##############################
# USUALLY RECURSION IS CONNECTED TO DCA APPROACH
# A divide-and-conquer algorithm recursively breaks down a problem into two or more sub-problems 
# of the same or related type, until these become simple enough to be solved directly. The solutions 
# to the sub-problems are then combined to give a solution to the original problem.

# https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/
# 1. Quicksort is a sorting algorithm. The algorithm picks a pivot element and rearranges the array elements so that all elements smaller than the picked pivot element move to the left side of the pivot, and all greater elements move to the right side. Finally, the algorithm recursively sorts the subarrays on the left and right of the pivot element.
# 2. Merge Sort is also a sorting algorithm. The algorithm divides the array into two halves, recursively sorts them, and finally merges the two sorted halves.
# 3. Closest Pair of Points The problem is to find the closest pair of points in a set of points in the x-y plane. The problem can be solved in O(n^2) time by calculating the distances of every pair of points and comparing the distances to find the minimum. The Divide and Conquer algorithm solves the problem in O(N log N) time.
# 4. Strassen’s Algorithm is an efficient algorithm to multiply two matrices. A simple method to multiply two matrices needs 3 nested loops and is O(n^3). Strassen’s algorithm multiplies two matrices in O(n^2.8974) time.
# 5. Cooley–Tukey Fast Fourier Transform (FFT) algorithm is the most common algorithm for FFT. It is a divide and conquer algorithm which works in O(N log N) time.
# 6. Karatsuba algorithm for fast multiplication does the multiplication of two n-digit numbers in at most

#RECURSION EXAMPLE
# Finding all possible combinations of numbers to reach a given sum
from itertools import combinations

def find_sum_in_list(numbers, target):
    results = []
    for x in range(len(numbers)):
        results.extend(
            [   
                combo for combo in combinations(numbers ,x)  
                    if sum(combo) == target
            ]   
        )   

    print results

if __name__ == "__main__":
    find_sum_in_list([3,9,8,4,5,7,10], 15)
Output: [(8, 7), (5, 10), (3, 8, 4), (3, 5, 7)]


##########

# divide and conquer
f(0, mid-1) + current value + f(mid+1,len-1)
# and the answer will be Math.max(aboveCombinedValue, Math.max(leftValueOnly, rightValueOnly)


###########
# another example https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
# Closest Pair of Points using Divide and Conquer algorithm





##########################################
nums.copy()

import math
-math.inf 









#########################
# max()
#########################
#The max() function returns the largest item in an iterable. It can also be used 
# to find the largest item between two or more parameters.
#The max() function has two forms:
#================
# 1. to find the largest item in an iterable
#================
max(iterable, *iterables, key, default)

# max() Parameters:
# iterable - an iterable such as list, tuple, set, dictionary, etc.
# *iterables (optional) - any number of iterables; can be more than one
# key (optional) - key function where the iterables are passed and comparison is performed based on its return value
# default (optional) - default value if the given iterable is empty


# to find the largest item between two or more objects
max(arg1, arg2, *args, key)

##############

Example
numbers = [9, 34, 11, -4, 27]

# find the maximum number
max_number = max(numbers)
print(max_number)

# Output: 34

#####

# In the case of dictionaries, max() returns the largest key. Let's use the key 
# parameter so that we can find the dictionary's key having the largest value.

# Example 3: max() in dictionaries
square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])

print("The key with the largest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9

# Output
# The largest key: 2
# The key with the largest value: -3
# The largest value: 9

#=========================
# 2. max() without iterable
#=========================

# max() Syntax
# To find the largest object between two or more parameters, we can use this syntax:

max(arg1, arg2, *args, key)

# max() parameters:
# arg1 - an object; can be numbers, strings, etc.
# arg2 - an object; can be numbers, strings, etc.
# *args (optional) - any number of objects
# key (optional) - key function where each argument is passed, and comparison is 
# performed based on its return value
# Basically, the max() function finds the largest item between two or more objects.

##################

# Example 4: Find the maximum among the given numbers
# find max among the arguments
result = max(4, -5, 23, 5)
print("The maximum number is:", result)

# Output
# The maximum number is: 23


##############################################################################

#MATH

max = float("-inf")

#####################

combine two list using list.extend()

###################

# For loops in python have an else clause which runs after the loop completes if  a break was not found. (Just because you can doesn't mean you should!).
Example:
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()

#######
#=============================
# floor division
floor = n // k

#-------------------------
# ceiling division

# Solution 1: Convert floor to ceiling with negation
def ceiling_division(n, d):
    return -(n // -d)
# Reminiscent of the Penn & Teller levitation trick, this "turns the world upside down (with negation), 
# uses plain floor division (where the ceiling and floor have been swapped), and then turns the world 
# right-side up (with negation again)"

#--------------------------
#Solution 2: Let divmod() do the work

def ceiling_division(n, d):
    q, r = divmod(n, d)
    return q + bool(r)

# The divmod() function gives (a // b, a % b) for integers (this may be less reliable with floats due 
# to round-off error). The step with bool(r) adds one to the quotient whenever there is a non-zero remainder.

#----------------------------
# Solution 3: Adjust the numerator before the division
def ceiling_division(n, d):
    return (n + d - 1) // d

# Translate the numerator upwards so that floor division rounds down to the intended ceiling. Note, 
# this only works for integers.

#-----------------------------
# Solution 4: Convert to floats to use math.ceil()

def ceiling_division(n, d):
    return math.ceil(n / d)

# The math.ceil() code is easy to understand, but it converts from ints to floats and back. This isn't 
# very fast and it may have rounding issues. Also, it relies on Python 3 semantics where "true division" 
# produces a float and where the ceil() function returns an integer.


###########################################
# HOW TO TERMINATE LOOP OR SKIP A PART OF IT
# - BREAK
# - CONTINUE
# E.G. https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
###########################################
#======================
#raise StopIteration:
#======================
# To prevent the iteration to go on forever, we can use the StopIteration statement.

# In the __next__() method, we can add a terminating condition to raise an error if 
# the iteration is done a specified number of times:
#e.g.:
  class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


  #==========================
  # BREAK
  #==========================
#   in Python, the break statement provides you with the opportunity to exit out of a loop when an external 
#   condition is triggered. You’ll put the break statement within the block of code under your loop statement, 
#   usually after a conditional if statement.

  number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

#============================
# CONTINUE
#============================

# You can use the continue statement to avoid deeply nested conditional code, or to optimize a loop by eliminating 
# frequently occurring cases that you would like to reject.

# The continue statement causes a program to skip certain factors that come up within a loop, but then continue 
# through the rest of the loop.
number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')

################################
# ACCESSING ONLY ODD OR EVEN INDEXES ITEMS FROM A LIST:
#################################
#========================
# OPTION 1: ONLINER LOOP AND % MODULUS
#========================
odd = [num for i, num in enumerate(nums) if i%2 != 0]
even = [num for i, num in enumerate(nums) if i%2 == 0]

#========================
# OPTION 2: ONLINER LOOP AND & OPERATOR
#========================
x = [10, 20, 30, 40, 50, 60, 70]
y = [j for i, j in enumerate(x) if i&1]
# [20, 40, 60]

# Explanation
# Bitwise AND operator is used with 1, and the reason it works is because, odd number when written 
# in binary must have its first digit as 1. Let's check:

23 = 1 * (2**4) + 0 * (2**3) + 1 * (2**2) + 1 * (2**1) + 1 * (2**0) = 10111
14 = 1 * (2**3) + 1 * (2**2) + 1 * (2**1) + 0 * (2**0) = 1110

# AND operation with 1 will only return 1 (1 in binary will also have last digit 1), iff the value is odd.

# P.S: You can tactically use this method if you want to select odd and even columns in a dataframe. 
# Let's say x and y coordinates of facial key-points are given as columns x1, y1, x2, etc... To normalize 
# the x and y coordinates with width and height values of each image you can simply perform:

for i in range(df.shape[1]):
    if i&1:
        df.iloc[:, i] /= heights
    else:
        df.iloc[:, i] /= widths

#========================
# OPTION 3: SLICING
#========================
l = L[1::2]

# And this is all. The result will contain the elements placed on the following positions 
# (0-based, so first element is at position 0, second at 1 etc.):
# 1, 3, 5
# so the result (actual numbers) will be:
# 2, 4, 6

# Explanation
# The [1::2] at the end is just a notation for list slicing. Usually it is in the following form:

# some_list[start:stop:step]


#################################
#ACCESS ODD OR EVEN NUMBERS IN A LIST
################################

#You can make use of bitwise AND operator &:

x = [1, 2, 3, 4, 5, 6, 7]
y = [i for i in x if i&1]
# [1, 3, 5, 7]
# This will give you the odd elements in the list. 

# Explanation
# Bitwise AND operator is used with 1, and the reason it works is because, odd number when written 
# in binary must have its first digit as 1. 

