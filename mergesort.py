# Mergesort implementation using recursion

# Recursion module
def mergesort(arr):
    h = len(arr)
    l = 0

    # Base condition for recursion to return a single element list 
    if len(arr) <= 1:
        return arr

    # Splitting in two for divide and conquer strategy
    mid = int((l + h) / 2)

    # recursively splitting the list and merging from ground up in order
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

# Merge two lists with final list in ascending order
def merge(a1, a2):

    # Merge two lists into a single sorted list 


    # Empty final list declaration having size of first and second list
    am = [0] * len(a1) + [0] * len(a2)
    index = 0

    while True:
        if a1:
            if a2:
                if a1[0] <= a2[0]:
                    # Popping list from front using pop(0)
                    am[index] = a1.pop(0)
                    index += 1
            else:
                # if list 2 is empty, pop list2
                am[index] = a1.pop(0)
                index += 1

        if a2: 
            if a1:
                if a1[0] >= a2[0]:
                    am[index] = a2.pop(0)
                    index += 1

            else:
                am[index] = a2.pop(0)
                index += 1

        if not a1 and not a2:
            break

    return am




lst = [64, 25, 12, 22, 11, 20,19,97,78,125,2,5,45, 8, 322, 145,6,89,97, 44,7, 23,1, 68,43,21, 20]

a1 = [25, 44, 47] # i

a2 = [23, 45, 67] # j
print(mergesort(lst))



