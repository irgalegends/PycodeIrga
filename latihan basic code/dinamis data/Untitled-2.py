dict1={"a":1,"b":2,"c":3,"d":4}
dict2=list(dict1.keys())
for x,y in dict1.items():
    if x == 0:
    print(x,":",y)
    