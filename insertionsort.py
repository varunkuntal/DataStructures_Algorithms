def insertionsort(arr):
    for i in range(1, len(arr)):
        # Iterating through each value into key for later comparison and shifting value 
        k = i - 1
        key = arr[i]
        while k >= 0 and key < arr[k]:
            print(k, i)
            print("shifting: old & new values: ", arr[k+1], arr[k])
            arr[k+1] = arr[k]
            print(arr)
            k = k - 1
        print("arr[k], key = ", k, arr[k], key)
        arr[k+1] = key

    print(arr)

lst = [64, 25, 12, 22, 11]
insertionsort(lst)
