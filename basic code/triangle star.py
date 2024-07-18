#upper triangle
j=0
char=str("^")
n=int(float(input("your n:")))
for i in range(n+1):
    for j in range(i):
        print(char,end="")
    print()
#mid 
if j ==(i-1):
      print(char*(n+1))
#bottom triangle
for i in range(n,-1,-1):
    for j in range(i):
        print(char,end="")
    print()  

    
