mydict1={}
print("enter elements of first dict")
while True:
    key=input("enter key(or 'q' to quit): ")
    if key=='q':
     break
    value=int(input("enter the value: "))
    mydict1[key]=value
print("enter elements of second dict")
mydict2={}
while True:
      key=input("enter key(or 'q' to quit): ")
      if key=='q':
       break
      value=int(input("enter the value: "))
      mydict2[key]=value
print(mydict1|mydict2)
