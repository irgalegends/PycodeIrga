#menu beli buah,output=nama buah,kg dan total harga
vegetables_dict={"a":1,"b":2,"c":3,"d":4}
vegetables_buy={}

while True:
    print("     ---------menu---------"+"\n"+"\n"+
          "add vegetables    (a)"+"\n"+
          "remove vegetables (r)"+"\n"+
          "see vegetables    (s)"+"\n"+
          "buy vegetables    (b)"+"\n" 
          )
    print("$",end="")
    option=input()
    
    if option == "a":
          while True:
                print("enter new menu:",end="")
                key_A=input()
                print("enter price/kg:",end="")
                value_A=int(input())
                if key_A == "":
                    continue
                elif value_A == "":
                    continue
                if key_A in vegetables_dict:
                      print("the data already exists","\n")
                else:
                      vegetables_dict[key_A]=value_A
                print("next? y/n","",end="")
                option_1=input() 
                if option_1 == "n":
                      break
                else:
                    continue

    elif option == "r":
          while True:
                print("vegetables-->"+str(vegetables_dict)+"\n")
                print("select menu to delete:",end="")
                data1=input()
                if data1 in vegetables_dict:
                      del vegetables_dict[data1]
                else:
                      print("data not found...","\n")
                      break

                print("next? y/n","",end="")
                option_1=input()
                if option_1 == "n":
                      break
                
    elif option == "s":
          if not vegetables_dict:
                      print("empty data !!!","\n")
          else:
                print("vegetables:")
                for key,value in vegetables_dict.items():
                      print(key,"=",str(value))
                            
    elif option == "b":
        print("menu:","\n")
        for key,value in vegetables_dict:
              print(key,"=",value,"\n")
              print("pilih sayur:")
              while True:
                    menu=input("pilih menu:")
                    if menu == "":
                          continue
                    elif menu not in vegetables_buy:
                          print("menu tidak terdaftar!!")
                    jumlah=int(input("jumlah(kg):"))
                    
                    
                    
                    
                          
              
            
                
    else:
          print("menu not found...","\n")
    
    
    

    