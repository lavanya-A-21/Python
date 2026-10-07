cl1=set()
cl2=set()
n1=int(input("enter the number of colors in list1: "))
print("enter the colors to list1:")
for x in range (n1):
    color=input()
    cl1.add(color)
n2=int(input("enter the number of colors in list2: "))
print("enter the colors to list2:")
for x in range (n2):
    color=input()
    cl2.add(color)
diff=cl1.difference(cl2)
print("color in list1 not in list2:",diff)

    
