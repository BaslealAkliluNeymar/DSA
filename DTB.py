def DTB(n):
    if n == 0:
        return 0
    else:
        return (n % 2) +  10 * DTB(int(n / 2))
        

print(DTB(16))
