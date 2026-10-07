import operator
mydict={}
while True:
    key=input("enter key(or 'q' to quit): ")
    if key=='q':
        break
    value=int(input("enter the value:"))
    mydict[key]=value
    print('original dictionary:',mydict)
    sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
    print("dictionary is ascending order by value:",sd)
    sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
    print('Dictionary in descending order by value:',sd)
