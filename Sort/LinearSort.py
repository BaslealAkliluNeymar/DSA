def LinearSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1- i):
            if arr[i] < arr[j]:
                arr[i],arr[j] == arr[j],arr[i]

    return arr



arr = [1,2,3,4,5,6,7,8,9]
print(LinearSort(arr))