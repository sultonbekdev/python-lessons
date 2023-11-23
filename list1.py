#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:37:40 2023

@author: aepeul
"""
cars=['bmw','mercedes benz','volvo','general motors','tesla','audi']
cars.sort()
print(cars)

#reverse=True - teskarisiga joyleydi

cars=['Bmw','mercedes benz','volvo','general motors','tesla','audi']
cars.sort(reverse=True)
print(cars)

cars=['Bmw','mercedes benz','volvo','general motors','tesla','audi']
print(sorted(cars))

mehmonlar=['Odil', 'Hamid', 'Temur', 'Avazbek','Farruh','Shamshiddin']
print('sorted qaytargan royxat: ', sorted(mehmonlar))
print('sort qaytargan qiymat: ', mehmonlar)
print(sorted(mehmonlar,reverse=True))

ages=[12,23,45,66,34,13,90]
ages.sort()
print(ages)
print(sorted(ages,reverse=True))

#bazan ro'yxatni aylantirish mumkin buning uchun .reverse() ishlatiladi

names=['Lop','Khan','Ilo','Uil','Saq']
names.reverse()
print(names)

#ro'yhatni uzunligini bilish len()

fruits=['apple','pear','melon','graps','persic']
print("Elementlar soni:",len(fruits))

# Range() funksiyasi bu yordamida malun ketma ketlikda elementlarni yaratishimiz mn
#list() orqali saqlab olamiz

numbers=list(range(0,10))
print(numbers)

juft_sonlar=list(range(0,10,2))
toq_sonlar=list(range(1,10,2))
print("Juft sonlar",juft_sonlar)
print("toq sonlar",toq_sonlar)

a=list(range(10))
print(a)

narxlar=[1200,1400,2000,6000,3500]
qimmat=max(narxlar)
arzon=min(narxlar)
summa=sum(narxlar)
print('eng qimmat maxsulot narxi',qimmat,'eng arzoni',arzon, 'jami', summa)

cars=['Bmw','mercedes benz','volvo','general motors','tesla','audi']
my_cars=cars[2:]
print(my_cars)

#sonlardan nusxa olish
sonlar=[1,2,4,6,0,8,9]
sonlar2=sonlar
sonlar2.append(9)
print(sonlar2)

num=[1,2,3,4,5,6]
num2=num[:]
num2.append(7)
num2.append(8)
print("bu sonlar ro'yxati", num)
print('bu num2 royxati', num2)

# Tuple o'zgarmas qiymat () bilan yoziladi
tomonlar=(1, 23, 5)
tomonlar=list(tomonlar)
tomonlar.append(7)
print(tomonlar)

#topshiriqlar
davlatlar=['uzb','tj','kz','ru','usa','kr']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
print(sorted(davlatlar,reverse=True))

a=list(range(120,1200,2))
b=sum(a)
print(a)
print(b)
eng_katta=max(a)
eng_kichik=min(a)
print(eng_katta-eng_kichik)
print(len(a))
print(a[:20])
print(a[-20:])
print(a[530-550])

taomlar=[]
taomlar.append('osh')
taomlar.append('lagmon')
taomlar.append('shovla')
taomlar.append('kabob')
taomlar.append('somsa')
print(taomlar)
print(sorted(taomlar))
nonushta=taomlar
print(nonushta)
print(taomlar)
nonushta.remove('osh')
nonushta.remove('lagmon')
nonushta.append('tuxum')
nonushta.append('salat')
print(taomlar)
nonushta=('shovla', 'kabob', 'somsa', 'tuxum', 'salat')
nonushta=tuple(nonushta)
nonushta[0]="qaymoq"
print(nonushta)















