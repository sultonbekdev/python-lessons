#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:58:32 2023

@author: aepeul
"""

#talaba_0 = {
 #   'ism':'alijon',
  #  'familiya':'shamshiyev',
   # 'yosh':22,
    #'fakultet':'matematika',
   # 'kurs':4
    #}
#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
 #   print(f"Kalit: {kalit}")
  #  print(f"Qiymat: {qiymat} \n")
    
#telfonlar={'ali':'iphone x',
           #'vali':"galaxy s9",
           #'olim':'mi 10 pro',
           #'orif':'nokio 3310'}    

#for k, q in telfonlar.items():
 #   print(f"{k.title()} ning telefoni {q}")
    
    
#mahsulotlar = {
 #   'olma':10000,
  #  'anor':20000,
   # 'uzum':40000,
    #'anjir':25000,
   # 'shaftoli':30000
    #}    
#print(mahsulotlar.keys())

#print("Do'kondagi mahsulotlar \n")
#for mahsulot in mahsulotlar:
 #   print(mahsulot.title())

#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
  #  if mahsulot in bozorlik:
 #       print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")



#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
 #       print(f"Iltimos do'konga {buyum} ham olib keling!")
        
#print("Do'konimizdagi mahsulotlar ro'yxati")
#for mahsulot in sorted(mahsulotlar):
  #  print(mahsulot.title())





telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
    
    
    

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

#print('3 ta taom buyurtma bering.')
#buyurtmalar = []
#for n in range(3):
 #   buyurtmalar.append(input(f"{n+1}-taom:").lower())

#for buyurtma in buyurtmalar:
 #   if buyurtma in menu:
  #      print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
   # else:
    #    print(f"Kechirasiz, bizda {buyurtma} yo'q.")

kerak_taom=[]
for n in range(5):
    kerak_taom.append(input(f"{n+1} - taom:"))
    
for order in kerak_taom:
    if order in menu:
       print(f"{order.title()} {menu[order]} so'm")
       
else:
       print(f"Kechirasiz bizda {order} yo'q")



















