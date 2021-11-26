##########################
#### MERGE SORT ########## https://stackabuse.com/merge-sort-in-python/ EXPLANATION
# Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, 
# calls itself for the two halves, and then merges the two sorted halves. The merge() 
# function is used for merging two halves. The merge(arr, l, m, r) is a key process that 
# assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays 
# into one. See the following C implementation for details.
##########################

# Merge Sort in place 
#  this link provide various approaches with various time complexity big O 
# https://www.geeksforgeeks.org/in-place-merge-sort/

# another option not included in the link: probably O = (n * log n)

# New indexing function that includes the right index.
def get_partial_list(origin_list, left_index, right_index): # Added
    return origin_list[left_index:right_index+1]

def MERGE(A,start,mid,end):
    L = get_partial_list(A,start,mid)
    R = get_partial_list(A,mid+1,end)
    i = 0
    j = 0
    k = start
    for l in range(k,end+1):            # changed
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  

def mergeSort(A,p,r):
    if r - p > 0:                          # changed
        mid = int((p+r)/2)
        mergeSort(A,p,mid)
        mergeSort(A,mid+1,r)             # changed
        MERGE(A,p,mid,r)

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
mergeSort(A,0,len(A)-1)                 # changed
print A

#========================
#You can check the dividing process by using this code.

def MERGE(A,start,mid,end):
    # Do nothing
    pass

def mergeSort(A,p,r):
    if r - p > 1:
        mid = int((p+r)/2)
        print A[p:mid],A[mid:r]
        mergeSort(A,p,mid)
        mergeSort(A,mid,r)
        MERGE(A,p,mid,r)

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
mergeSort(A,0,len(A))

#######################
# Merge Sort out-place
# Python program for implementation of MergeSort
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),
 
# Output: 
# Given array is
# 12 11 13 5 6 7 

# Sorted array is
# 5 6 7 11 12 13




##########################
####  SORT ##########
##########################

