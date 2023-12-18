def factorial(n):
    if n > 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        return 'Factorial of a negative number is not defined!'


print(factorial(-5))

