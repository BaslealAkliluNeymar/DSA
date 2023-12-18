def reverse(n):
    x = 0
    if n < 10:
        return n
    else:
        x = (x * 10) + (n%10)
        reverse(n /10)
        return x

    return x


print(reverse(123))
