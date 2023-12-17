def fibonnaci(n):
    # This function gives the nth fibonnaci number.
    # for n = 3 , 1,1,2 , the result would be 2 
    sum = 0
    if n == 1 or n == 0:
        return 1
    else:
        return fibonnaci(n - 2) + fibonnaci(n - 1 )


