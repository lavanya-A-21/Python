n=int(input("enter the number of n terms:"))
if n<=0:
    print("fibonacci series up to",n,"is not defined.")
elif n==1:
    print("the first numbers in the fibonacci series=")
    print(0)
elif n==2:
     print("the second numbers in the fibonacci series=")
     print("0,1")   
else:
    first=0
    second=1
    print("the first",n,"numers in the fibonacci series=")
    print(first,",",second,end=",")
    for i in range(2,n):
        fib=first+second
        first=second
        second=fib
        if i == n-1:
            print(fib)
        else:
            print(fib,end=",")
