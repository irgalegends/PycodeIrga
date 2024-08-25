#rekursi code
#rumus ---->  ex: 7,9,11,13,15 dengan pola +2 ,maka if n==1 return 2 \\ rekursi=func(n-1)+2
# banyak deret, nilai awal deret ,pola deret
#output 5,10,15,20,25,30
data_number=[]

def number(x):
        if x==1:
            return user_pola_deret
        else:
            rekursif=number(x-1)+user_pola_deret

def minus(y):
    if y==1:
        return 1
    else:
        rekursif=minus(y-1)+1

while True:
    print("pilih menu:","\n 1) Pola deret positif(a)","\n 2) Pola Deret Negatif(b) \n")
    user_input=input("your choice:")

    if user_input=="a":
         while True:
              user_banyak_deret=int(input("banyak deret:"))
              if user_banyak_deret=="":
                   continue
              user_nilai_awal=int(input("nilai awal:"))
              if user_nilai_awal=="":
                   continue
              user_pola_deret=int(input("pola deret:"))
              if user_pola_deret=="":
                   continue
              
              

              
                   
                   

    

#output 6,5,4,3,2,1