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
        for key,value in vegetables_dict.items():
              print(key,"=",value)

        while True:
            menu=input("\n"+"pilih menu:")  #input menu       
            if menu == "":
                  continue
            elif menu not in vegetables_dict:
                  print("menu tidak terdaftar!!")
                  continue

            jumlah=int(input("jumlah(kg):")) #input jumlah
            if jumlah == "":
                  continue

            select=input("next? (y/n)") #worker
            if select == "y":
                  vegetables_buy[menu]=jumlah
            elif select == "n":
                  print("purchased products:")
                  sum_list=[]
                  for (key,value) in vegetables_buy.items():
                        sum1=value*jumlah#salah/////////
                        sum_list.append(sum1)
                        print(key,"\t",f"(quantity:{jumlah})")
                        print(f'"\t"+"price= Rp{sum1}')

                  print(f"TOTAL PURCHASES: Rp{sum(sum_list)}")
            else:
                  print("please chosee y/n only!!")


            

            
                
    else:
          print("menu not found...","\n")
    
    
    

    