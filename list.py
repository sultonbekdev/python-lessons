#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:49:16 2023

@author: aepeul
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [12000, 18000, 10900, 22000]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []
print("Birinchi meva: ", mevalar[0])
print("Olmaning narhi:", narhlar[1])

print("Birinchi Meva", mevalar[-1].upper())
print("shirin meva", mevalar[2].capitalize())

print(narhlar[0]+narhlar[1])
narhlar[0]=13000
narhlar[2]=11000
narhlar[3]=narhlar[3]+2000
print(narhlar)

cars=[]
cars.append('Tiko')
cars.append('Nexiya-3')
cars.append('Damas')
cars.append('Lasetti')
print(cars)
cars.insert(0, 'Malubi')
print(cars)
cars.insert(3, 'Mers')
print(cars)

del cars[3]
print(cars)

hayvonlar=['it', 'sichqon', 'mushuk', 'sigir', 'it']
hayvonlar.remove('it')
print(hayvonlar)

bozorlik=['yog', 'guruch', 'un', 'kartoshka','piyoz', 'non']
mahsulot=bozorlik.pop(-2)
print('Men bozordan ' + mahsulot + " sotib oldim")
print("Qolgan maxsulotlar", bozorlik)

# topshiriqlar

friends=['Jasur','Xasanboy','Oybek']
print("Salom " + friends[0] + ' bugun choyxonaga boramizmi?')
print(friends[-1] + ' sen ham borasanmi?')

numbers=[-2, -5,4,6,9,2]
numbers.insert(2, 6)
print(numbers[-2] + numbers[2])
del numbers[1]
print(numbers)
numbers.remove(2)
print(numbers)
numbers.append(1)
print(numbers)
numbers.pop(0)
print(numbers)

t_shaxslar=['Alisher N', 'Amur Temur', 'Z.Bobur']
z_shaxslar=['Yulduz U','Shovkat M', 'Ahat Q']
print('Men tarixiy shaxslardan '  +  t_shaxslar[1]+' bilan' + '\n zamonaviy shaxslardan esa ' +
z_shaxslar[1] + ' bilan uchrashishni hohlar edim.')
print(f"{t_shaxslar[1]} bilan {z_shaxslar[1]} boshqa davr insonlari")
print(f" Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan zamonaviylardan esa \n{z_shaxslar.pop(1)} bilan uchrashishni istamayman")

mehmonlar=[]
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
print(mehmonlar)














