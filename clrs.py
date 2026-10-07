clrs=[]
count=int(input("enter the number of colours:"))
print("enter the colour")
for x in range(count):
    color=input()
    clrs.append(color)
print("first color:",clrs[0],"last color:",clrs[count-1])
