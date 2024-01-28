def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1],arr[j] = arr[j],arr[j + 1]

    return arr



arr = [1,3,4,6,4,2,1,3,4,5,3]
print(BubbleSort(arr))