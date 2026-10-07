curr=int(input("Enter the currentyear:"))
fut=int(input("Enter the future year:"))
print("Leap year:")
for curr in range (curr,fut+1):
    if((curr %4==0)and curr%100!=0 or curr%400==0):
        print(curr)
    
