# Inefficient Selection Sort Algorithm
def selectionsort(arr):
    comparisons = 0
    swaps = 0
    ci = 0 
    cm = 0
    length = len(arr)
    try:
        # # 
        while cm < length:
            ci = cm + 1
            while ci < length:
                comparisons += 1
                if arr[ci] < arr[cm]:
                    arr[ci], arr[cm] = arr[cm], arr[ci]
                    swaps += 1
                ci += 1
            cm += 1

        return arr, comparisons, swaps

    except Exception as e:
        print("Error occurred, more info below. Exiting now!")


lst = [64, 25, 12, 22, 11, 20,19,97,78,125,2,5,45, 8, 322, 145,6,89,97, 44,7, 23,1, 68,43,21, 20]

results = selectionsort(lst)

print("Sorted Array: ", results[0])
print("Comparisons: ", results[1])
print("Swaps: ", results[2])


