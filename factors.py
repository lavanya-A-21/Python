num=int(input("enter the number:"))
factors=[]
for i in range(1,num+1):
    if num % i == 0:
        factors.append(i)
print(f"factors of{num}are:{factors}")
