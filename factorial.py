def recur_factorial(n):
    if n==1:
        return(n)
    else:
        return n*recur_factorial(n-1)
num=8
if num<0:
    print("sorry factorial does not exitst for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of",num, "is", recur_factorial(num))
    
