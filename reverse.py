def reverse(n):
    x = 0
    ten = 1
    if n < 10:
        return n
    else:
        x += (n%10)  * ten * 10 + reverse(n//10)
        return x


print(reverse(123))
