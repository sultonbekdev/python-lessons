#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:34:07 2023

@author: aepeul
"""

# file=open("pi.text")
# PI=file.read()
# print(PI)
# # file.close()
# with open('pi.txt') as file:
#     pi=file.read()
# print(pi)    

# pi=pi.rstrip() #qator ohiridagi bo'shliqni olib tashlaydi.
# pi=pi.replace('\n', '')    
# pi=float(pi)
# print(pi)   

with open('data/pi.txt') as fayl:
    pi=fayl.read()
print(pi)   

filename='data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)
        
with open(filename) as file:
    talabalar=file.readlines()
print(talabalar)

talabalar=[talaba.rstrip() for talaba in talabalar]   
print(talabalar)     
        

faylnomi='ustozlar.txt'
ism="Hasanboy"
tyil=1994
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')       
    fayl.write(str(tyil)+'\n')
    
with open(faylnomi, 'a') as fayl:
    fayl.write('Batirov Sultonbek\n')  
    fayl.write('1995')
    
import pickle

talaba1={'ism':'Sultonbek','familiya':'Batirov','tyil':1995}
talaba2={'ism':'Alibek','familiya':'Sarov','tyil':1998}

with open('info','wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)











    
        
        
        
        
        
        
        
        
        
        
        
        

                    