result=[]
start=int(input("enter starting range:"))
end=int(input("enter ending range:"))
if start<1000or end> 9999 or start>end:
    print("invalid range.please enter a valid 4-digit range.")
else:
    for num in range(start,end+1):
      if num%2 == 0:
          root= int(num**0.5)
      if root*root == num:
          result.append(num)
print("four digit even perfect square numbers in the given range:")
print(result)
