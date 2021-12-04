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


max = float("-inf")