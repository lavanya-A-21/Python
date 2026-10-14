import operator
mydict={}
while True:
    key=input("enter akey(or'q'to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict[key]=value
print('original dict:',mydict)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print('Dictionary in descending order by value:',sd)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print('dict in descending order by value:',sd)
