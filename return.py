#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:10:02 2023

@author: aepeul
"""

# def toliq_ism_yasa(ism,familiya):
#     """to'liq ism qaytaruvchi funksiya"""
#     toliq_ism=f"{ism} {familiya}"
#     return toliq_ism
# talaba1=toliq_ism_yasa('olim', 'hakimov')
# talaba2=toliq_ism_yasa('hakim', 'olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va { talaba2}")

# def toliq_ism_yasa(ism,familiya,otasini_ismi=''):
#     """to'liq ism qaytaruvchi funksiya"""
#     if otasini_ismi:
#         toliq_ism=f"{ism} {otasini_ismi} {familiya}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1=toliq_ism_yasa('hakim','olimov','haydarovich')
# talaba2=toliq_ism_yasa('nosir', 'karimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
    
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
    
    
# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# print(oraliq(0,11))    
    
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("\n Quyidagi ma'lumotlarni kiriting", end=" ")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Model: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")

#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob=input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#        break

# def mijoz_info(ism,familiya,t_yil,t_joy,email='',tel_raqam=None):
#     mijoz={'ism':ism,
#            'familiya':familiya,
#            't_yil':t_yil,
#            't_joy':t_joy,
#            'email':email,
#            'tel_raqam':tel_raqam}
#     return mijoz
# mijoz1=mijoz_info('ali', 'valiyev', 1995, 'toshkent', 3271126)
# mijoz2=mijoz_info('husan', 'norov', 1993, 'andijon')
# mijozlar=[mijoz1,mijoz2]
# print('Mijozlar royhati toliq')
# for mijoz in mijozlar:
#     if mijoz['raqam':]:
#         raqam=mijoz['raqam']
#     else:
#         raqam='nomalum'
#         print()


# def kattasi(x,y,z):
#     max=x
#     if max<=y:
#         max=y
#     if max<=z:
#         max=z
#     return max

# a=kattasi(23,34,56)
 
# print(f"Sonlarnig ichida {a} eng kattasi bo'ladi")

# def aylana_info(radius,pi=3.14159):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetr":2*radius*pi,
#               "yuza":pi*radius**2}
#     return aylana

# a=aylana_info(5)
# print(a)


# def aylana_info(radius,pi=3.14):
#     aylana={'radius':radius,
#             'diametr':radius*2,
#             'yuzi':2*radius*pi}
#     return aylana
# a=aylana_info(6)
# print("Aylana radiusi {a} ga teng!")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print(avto1)
# # print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#Berilgan oraliqdagi tub sonlar ro'yxatini
# qaytaruvchi funksiya yozing (tub sonlar —faqat birga va 
#o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# a=tub_sonlar_top(1,20)
# print(a)
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))





















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    