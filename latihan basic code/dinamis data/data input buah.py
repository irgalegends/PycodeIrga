#menu beli buah,output=nama buah,kg dan total harga
vegetables_dict={"a":1,"b":2,"c":3,"d":4}
vegetables_buy_only={}
price_item_dict={}

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
        for (vegetables,price) in vegetables_dict.items():
              print(vegetables,"=",price)

        while True:
            menu=input("\n"+"pilih menu:")  #input menu       
            if menu == "":#bug1
                  continue
            elif menu not in vegetables_dict:#bug2
                  print("menu tidak terdaftar!!")
                  continue

            jumlah=int(input("jumlah(kg):")) #input jumlah
            if jumlah == "":#bug1
                  continue
            vegetables_buy_only[menu]=jumlah
            price_item=vegetables_dict.get(menu,0)*jumlah #total per item
            price_item_dict[menu]=price_item #dict per item
            
            select=input("next? (y/n)") #worker
            if select == "y":
                  continue
            elif select == "n":
                  print("purchased products:")
                  for (vegetables,quantity) in vegetables_buy_only.items():
                        print(vegetables,"\t",f"(quantity:{quantity})")
                        print("\t"+" price= Rp"f'{price_item_dict.get(vegetables,0)}',"\n")

                  print(f"TOTAL PURCHASES: Rp{sum(list(price_item_dict.values()))}")
            else:
                  print("please chosee y/n only!!")


            

            
                
    else:
          print("menu not found...","\n")
    
    
    

    