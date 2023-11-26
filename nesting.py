#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:36:30 2023

@author: aepeul
"""
car0={'model':'lacetti',
      'rang':'oq',
      'yil':'2018',
      'narh':'13000',
      'km':'50000',
      'korobka':'avtomat'
      }

car1={'model':'nexia 3',
      'rang':'qora',
      'yil':'2015',
      'narh':'90000',
      'korobka':'mexanika'
      }

car2={'model':'gentra',
      'rang':'qizil',
      'yil':'2019',
      'narh':'15000',
      'km':'20000',
      'korobka':'meanika'
      }
car=car0
print(f"{car['model'].title()}, \
      {car['rang']} - rang, \ {car['yil']} - yil, {car['narh']} - narh")
      
cars=[car0,car1,car2]
for car in cars:
     print(f"{car['model'].title()}, \
           {car['rang']} - rang, \ {car['yil']} - yil, {car['narh']} - narh")
           
print(cars[0]['model'])           

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")


malibus=[]
for n in range(10):
    new_car={'model':'malibus',
          'rang':'none',
          'yil':'2020',
          'narh':'none',
          'km':0,
          'korobka':'avto'
          }
    malibus.append(new_car)

for malibu in malibus[:3]:
    malibu['rang']='qizil'

for malibu in malibus[3:6]:
    malibu['rang']='qora'
    
for malibu in malibus:
    if malibu["korobka"]=="avto":
        malibu['narh']=60000
    else:
        malibu['narh']=40000
print(malibus)

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi.", end='')
    for til in tillar:
        print(til, end='')
        
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

#for ism,info in hamkasblar.items():
    print(f"{ism.title()} {info['familiya'].title()}",
          f"{info['tyil']} - yilda tug'ilgan! \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
          
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
# shaxslar=[buxoriy,qodiriy,vohidov,navoiy]
# for shaxs in shaxslar:
#     ism=shaxs['ism']
#     asarlar=shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari! ")
# for asar in asarlar:
#        print(asarlar)

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)


































    








































