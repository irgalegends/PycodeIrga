#rekursi code
#rumus ---->  ex: 7,9,11,13,15 dengan pola +2 ,maka if n==1 return 2 \\ rekursi=func(n-1)+2
# banyak deret, nilai awal deret ,pola deret
#output 5,10,15,20,25,30
data_number=[]

while True:
    print("pilih menu:","\n 1) Pola deret positif","\n 2) Pola Deret Negatif")
    def number(x):
        if x==1:
            return 5
        else:
            rekursif=number(x-1)+5

for i in range(0,user+1):
    data_number.append(number())
x=0


#output 6,5,4,3,2,1
#def minus(y):
    #if y==1:
        #return 1
    #else:
        #rekursif=minus(y-1)+1