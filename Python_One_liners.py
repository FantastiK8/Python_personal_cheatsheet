# https://wiki.python.org/moin/Powerful%20Python%20One-Liners

################
# ONE LINER FOR LOOP:
# IT GIVES A LIST BACK IF IT IS IN [] BRACKETS
# CAN USE sum(FOR LOOP WITH IF ELSE WITHOUT [] BRACKETS)
################
#=====================
#FOR, IF ELSE
[i if i % 2 != 0 else i * 100 for i in range(1,10)]
[1, 200, 3, 400, 5, 600, 7, 800, 9]

######
# LAMBDA
#Using: [False, True][Expression]
map(lambda i: [i*100, i][i % 2 != 0], range(1,10))
[1, 200, 3, 400, 5, 600, 7, 800, 9]
#=======================
#FOR, IF
[ i for i in range(1, 10) if i%2]


#CHECK IF IT WORKS AND HOW IT WORKS:
m = [i if i%2 else i*100 for i in range(1, 10) if not i%3]
n = [i if i%2 else i*100 for i in range(1, 10)]
print(m)
print(n)

#######

# ONE LINER AS A FILTER:
#######################

# https://scripteverything.com/python-for-loop-one-liner/
# 2D ARRAY/LIST
data = [[11, 20, 35],
        [110, 230, 390],
        [1280, 2870, 3110]]

#To create a list of averages for each row of the data grid above, we would create our one-liner 
# for loop (list comprehension) as follows:

average_per_row = [sum(row) / len(row) for row in data]  

print(average_per_row)

# [22.0, 243.33333333333334, 2420.0]

# VERSUS:

average_per_row = []
for row in data:
    average_per_row.append(sum(row) / len(row))

# Notice what has happened with our single line of code:
# First, we have everything wrapped in the familiar list square brackets annotation, then within 
# those brackets we have our operation on what we want to do with each for-loop iteration.

# Next, as I want to perform a simple average calculation on each row, I know that at each 
# iteration of the for-loop will result in each row being returned, and I’ve labelled this 
# returned variable with the appropriate label row. Therefore, at each iteration of the for-loop 
# I’m receiving the following data:

#The result from this calculation is then stored as a new element in my new list:

1st iteration = [11, 20, 35] = 66 / 3 = 22
2nd iteration = [110, 230, 390] = 730 / 3 = 243.33333333333334
3rd iteration = [1280, 2870, 3110] = 7260 / 3 = 2420

Result = [22, 243.33333333333334, 2420]


######################################
# Ternary Operator
##############
# You may recall that Python provides a conditional expression (otherwise known as a ternary operator) 
# which allows for an if-else statement to be placed on one line, like so:

result = x if C else y

# By using this same concept, I can insert the ternary operator within my list comprehension like so 
# to be able to filter and provide the result I need for elements within the for-loop that I’d 
# like to completely change:

average_per_row = [sum(row) / len(row) if type(row[0]) is not str else None for row in data]

# Notice the ternary operation used inside the list comprehension:

sum(row) / len(row) if type(row[0]) is not str else None

# This conditional expression will perform the simple average operation if the type of the first 
# element within each returned list is not of type string, otherwise if it is it will return None.

# Now my result is as follows:

average_per_row = [sum(row) / len(row) if type(row[0]) is not str else None for row in data]

print(average_per_row)

# [None, 22.0, 243.33333333333334, 2420.0]


#############################
# GETTING ONE NUMBER SUMMED FROM EACH ITTERATION:

max_odd = sum(num for i, num in enumerate(nums) if i%2 != 0)
max_even = sum(num for i, num in enumerate(nums) if i%2 == 0)





