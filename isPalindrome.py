def isPalndrome(n):
    x = 0
    if n == 0:
        return 0
    else:
        x += 10*(isPalndrome(n / 10) + (n % 10))
        return x



print(isPalndrome(1321))