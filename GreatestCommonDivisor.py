def GCD(n, m):
    #Inorder to solve this problem recursively , we need to use the 
    # Euclidean algorithm

    if n % m == 0:
        return m
    else:
        return GCD(m,n % m)



print(GCD(144,12))
