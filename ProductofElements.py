def productofElements(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr.pop() * productofElements(arr)


