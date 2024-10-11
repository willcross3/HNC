def x(n):
    print(n)
    if n == 1:
        return n 
    if n % 2 == 0:
        return(x(n//2))
    else:
        return(x(n*3+1))
    
print(x(27))