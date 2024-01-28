def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    small = []
    duplicate = []
    large = []
    pivot = arr[len(arr) - 1]

    for i in arr:
        if i < pivot:
            small.append(i)
        elif i == pivot:
            duplicate.append(i)
        else:
            large.append(i)
    return QuickSort(small) + duplicate + QuickSort(large)  



arr = [1,3,4,6,4,2,1,3,4,5,3]
print(QuickSort(arr))