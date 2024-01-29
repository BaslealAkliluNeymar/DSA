#This is the merge function ; it is not a merge sort algorithm
def merge(a,b,lena,lenb):
    i = 0
    j = 0
    k = 0
    c = [None] * (len(a) + len(b))
    while(i < lena and j < lenb):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1 
    for i in range(i,lena):
        c[k] = a[i]
        k += 1
    for j in range(j,lenb):
        c[k] = a[j]
        k += 1

    
    return c


a = [2,8,15,18,19]
b = [5,9,12,17]
print(merge(a,b,len(a),len(b)))