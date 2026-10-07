string=input("enter the string:")
n=len(string)

first=string[0]
last=string[n-1]
a=last + string[1:n-1] + first
print("new string:",a)
