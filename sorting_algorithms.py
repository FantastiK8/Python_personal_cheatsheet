##########################
#### MERGE SORT ##########
##########################

# Merge Sort in place
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

