def recursiveRange(n):
    # This function gets the sum of all positive integers upto and 
    # including n.
    if n >= 0:
        if n == 0:
            return 0
        else:
            return n + recursiveRange(n - 1)


