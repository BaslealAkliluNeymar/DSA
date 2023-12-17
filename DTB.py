def DTB(n):
    if n == 1:
        return 0
    else:
        return (n % 2 ) +  10 * DTB(n / 2)
        

print(DTB(16))
