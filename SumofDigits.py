def SumOfDigits(n):
    # This function adds the digits of a number recursively.
    sum = 0
    if n < 1:
        return 0
    else:
        return n % 10 + SumOfDigits(n / 10)

