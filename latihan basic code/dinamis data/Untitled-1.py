def number(x):
        if x==1:
            return 5
        else:
            return number(x-1)+5
            
for i in range(1,4):
    print(number(i))
