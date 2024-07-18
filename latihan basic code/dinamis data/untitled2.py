# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:22:43 2024

@author: CPU
"""

dict1={}
while True:
    key1=input("key:")
    value=int(input("value:"))
    dict1[key1]=value
    x=input("y/n:")
    if x=="n":
        print(dict1)
        break
        
    