def power(n, num):
    # This function takes two arguments and returns the power
    # of any number num raised to nth number.
    if n == 1:
        return num
    else:
        return num * power(n - 1,num)



