def number(x):
        if x==1:
            return 5
        else:
            rekursif=number(x-1)+5

print(number(1))
