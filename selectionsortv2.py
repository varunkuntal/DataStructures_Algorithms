def selectionsortv2(arr):
    comparisons = 0
    swaps = 0
    curr_index = 0
    curr_min = 0
    min_index = 0
    length = len(arr)

    try:
        while curr_min < length:
            # initially set lowest value as base value
            lowest = curr_min
            # To check lowest with rest of elements, index check until the end with while loop
            curr_index = curr_min + 1
            while curr_index < length:
                # if lowest index value greater than current index value, set new lowest to current index
                if arr[curr_index] < arr[lowest]:
                    lowest = curr_index
                    comparisons += 1
                curr_index += 1
            # If lowest index value changes from initially set as base value, swap them
            if lowest != curr_min:
                arr[curr_min], arr[lowest] = arr[lowest], arr[curr_min]
                swaps += 1

            curr_min += 1
        return arr, comparisons, swaps

    except Exception:
        print("Error occurred, more info below! Exiting now.")

lst = [64, 25, 12, 22, 11, 20,19,97,78,125,2,5,45, 8, 322, 145,6,89,97, 44,7, 23,1, 68,43,21, 20]
results = selectionsortv2(lst)
print("Sorted Array: ", results[0])
print("Total Comparisons: ", results[1])
print("Total Swaps: ", results[2])
