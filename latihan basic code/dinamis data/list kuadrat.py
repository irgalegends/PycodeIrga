#list kuadrat
import time
data_number=[1,2,3,4,5,6,7,8,9,10]


def pangkat(var):
    new_var=[]
    for i in var:
        print("process",i,"to",var[-1])
        time.sleep(0.4)
        new_var.append(i**2)
    print("\n"+"return list =",str(new_var))

pangkat(data_number)     
   
    
        
    