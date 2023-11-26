#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:32:32 2023

@author: aepeul
"""

#yosh=int(input("Yoshingiz nechida? "))
#if yosh<=4:
 #   print("Sizga kirish bepul")
#elif yosh<=12:
 #   print("Sizga kirish 5000 so'm")    
#elif yosh<=18:
 #   print("sizga kirish 8000 so'm")    
#else:
 #   print("Sizga kirish 10000 so'm")    
    
yosh=int(input("Yoshingiz nechida? "))
if yosh<=4:
    narx=0
elif    yosh<=12:
    narx=5000 
elif yosh<=18:
     narx=8000   
else:
   narx=10000
print(f"Sizga kirish {narx} so'm")     

#kun=input("Bugun qandey kun? ")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
 #   print("Bugun dam olish kuni")
#else:
 #   print("bugun ish kuni")    
    
#kun=input('Bugun nima kun? ')    
#harorat=float(input("Havo harorati nechi? "))
#if kun.lower()=="yakshanba" or kun.lower()=='shanba' and harorat>=30:
#    print("Cho'milgani ketdik")
#elif kun.lower()=='yakshanba' or kun.lower()=="shanba" and harorat<30:
 #   print("bugun havo sovuq")

#narx=15000
#choy=True
#salat=True
#if choy and salat:
 #   narx=narx+10000
#elif choy or salat:
   # narx=narx+5000
#print(f"Jami {narx} so'm")

#cost=10000
#tea=1
#bread=0
#juice=1
#asarty=1

#if tea:
 #   cost=cost+2000
 #   print("Mijoz choy oldi")
#if bread:
 #   cost=cost+3000
#    print("Mijoz non oldi")
#if  juice:
 #   cost=cost+5000
  #  print("Mijoz kampot oldi")
#if asarty:
 #   cost=cost+10000
 #   print("Mijiz asarti oldi")
#print(f"Jami {cost} so'm")    

#menu=['osh', 'shashlik', 'norin', 'manti', 'somsa']
#ovqat=input("Nima ovqat yeysiz >>>")
#if ovqat.lower() in menu:
 #    print("Buyurtma bajarildi")
#else:
 #    print("uzur")    
 
#menu=['osh', 'shashlik', 'norin', 'manti', 'somsa']
#ovqat=input("Nima ovqat yeysiz >>>")
#if ovqat.lower() not in menu:
 #    print("uzur")
#else:
 #    print("Buyurtma bajarildi")    
    
    
#menu=['osh', 'shashlik', 'norin', 'manti', 'somsa']    
#buyutma=['norin', 'manti', 'somsa', 'mastava']   
#if buyutma: 
#  for taom in menu:
#   if taom in menu:
#      print(f"menuda {taom} bor") 
#else:
# print(f"menuda {taom} yo'q")
    
    

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]
#
#if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
 #   for taom in buyurtmalar:
  #      if taom in menu:
   #         print(f"Menuda {taom} bor")
    #    else:
     #       print(f"Kechirasiz, menuda {taom} yo'q")
#else: # agar ro'yxat bo'sh bo'lsa
 #   print("Savatchangiz bo'sh!")

#son=float(input("Just son kiriting? "))
#if son%2:
 #   print('emas')
#else:
 #   print('raxmat')    
 
#yosh=int(input("yoshingizni kiriting "))
#if yosh<=4 or yosh>=60:
#     narx=0
#elif yosh<=18:
 #    narx=10000  
#elif  yosh>=18:
 #   narx=20000
  #  print(f"chipta {narx} so'm")

#x=int(input("Birinchi son kiriting! "))
#y=int(input("Ikkinchi son kiriting! "))
#if x==y:
#    print("teng")
#elif x>y:
#    print(f"{x} katta {y} dan")
#elif x<y:
#    print(f"{y} katta {x} dan")    


#user=['ali','vali','karim','salim','xasan']
#login=input("Yangi login tanlang ")
#if login in user:
#    print(f"bundey {login.lower()} mavjud")
#else:
 #   print("xush omadi!")


son=int(input("istalgan soni tanleng "))
for n in range(2,10):
 if not son%n:
     print(f"{son} ni {n} ga qoldiqsiz bo'linadi")
    


































































 
 